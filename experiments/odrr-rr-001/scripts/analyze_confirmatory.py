#!/usr/bin/env python3
import csv
import math
import random
import statistics
import sys
from collections import defaultdict

ALPHA = 0.05
SESOI = 0.75
N_PERM = 100000
N_BOOT = 10000
SEED = 20260907


def percentile(xs, q):
    xs = sorted(xs)
    if not xs:
        return float("nan")
    k = (len(xs) - 1) * q
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return xs[int(k)]
    return xs[f] * (c - k) + xs[c] * (k - f)


def bootstrap_ci(ds, level=.95, n=N_BOOT, seed=SEED):
    rng = random.Random(seed)
    vals = []
    for _ in range(n):
        samp = [rng.choice(ds) for _ in ds]
        vals.append(statistics.fmean(samp))
    a = (1 - level) / 2
    return percentile(vals, a), percentile(vals, 1 - a)


def signflip_p(ds, n=N_PERM, seed=SEED):
    obs = abs(statistics.fmean(ds))
    if len(ds) <= 20:
        total = 2 ** len(ds)
        ge = 0
        for mask in range(total):
            val = statistics.fmean(d if (mask >> i) & 1 else -d for i, d in enumerate(ds))
            ge += abs(val) >= obs - 1e-12
        return ge / total
    rng = random.Random(seed)
    ge = 0
    for _ in range(n):
        val = statistics.fmean(d if rng.random() < .5 else -d for d in ds)
        ge += abs(val) >= obs - 1e-12
    return (ge + 1) / (n + 1)


def load_key(path):
    key = {}
    for r in csv.DictReader(open(path, newline="", encoding="utf-8")):
        key[r["stimulus_id"]] = r["condition"]
    return key


def compute(data_path, key_path):
    key = load_key(key_path)
    transitions = defaultdict(list)
    qc_stable_mere = []
    qc_stable_change = []
    qc_rearranged_change = []

    for r in csv.DictReader(open(data_path, newline="", encoding="utf-8")):
        if str(r["technical_ok"]).lower() not in {"1", "true"}:
            continue
        sid = r["stimulus_id"]
        condition = key[sid]
        orientation_index = int(r["orientation_index"])

        # Study-level outcome-neutral quality controls.
        if orientation_index != 1:
            if condition == "QC_ROT_STABLE":
                qc_stable_mere.append(float(r["mere_rotation"]))
                qc_stable_change.append(float(r["grouping_change"]))
            elif condition == "QC_REARRANGED":
                qc_rearranged_change.append(float(r["grouping_change"]))

        # Primary ODRR is calculated only for blinded TARGET / CONTROL sources.
        if condition not in {"TARGET", "CONTROL"} or orientation_index == 1:
            continue
        coherence = float(r["coherence"])
        grouping_change = float(r["grouping_change"])
        mere_rotation = float(r["mere_rotation"])
        odrr = (coherence + grouping_change + (10 - mere_rotation)) / 3
        transitions[(r["participant_token"], sid)].append(odrr)

    if not qc_stable_mere or not qc_stable_change or not qc_rearranged_change:
        raise ValueError("quality-control data missing")

    qc = {
        "rot_stable_median_mere_rotation": statistics.median(qc_stable_mere),
        "rot_stable_median_grouping_change": statistics.median(qc_stable_change),
        "rearranged_median_grouping_change": statistics.median(qc_rearranged_change),
    }
    qc["quality_control_pass"] = (
        qc["rot_stable_median_mere_rotation"] >= 7
        and qc["rot_stable_median_grouping_change"] <= 4
        and qc["rearranged_median_grouping_change"] >= 7
    )

    source_mean = {k: statistics.fmean(v) for k, v in transitions.items() if v}
    by_participant_condition = defaultdict(list)
    for (participant, sid), value in source_mean.items():
        by_participant_condition[(participant, key[sid])].append(value)

    participants = sorted({p for p, condition in by_participant_condition if condition in {"TARGET", "CONTROL"}})
    ds = []
    targets = []
    controls = []
    for participant in participants:
        if not by_participant_condition[(participant, "TARGET")] or not by_participant_condition[(participant, "CONTROL")]:
            continue
        target = statistics.fmean(by_participant_condition[(participant, "TARGET")])
        control = statistics.fmean(by_participant_condition[(participant, "CONTROL")])
        targets.append(target)
        controls.append(control)
        ds.append(target - control)

    if len(ds) < 2:
        raise ValueError("insufficient participants")

    D = statistics.fmean(ds)
    sd = statistics.stdev(ds)
    dz = D / sd if sd else float("inf")
    p = signflip_p(ds)
    ci95 = bootstrap_ci(ds, .95)
    ci90 = bootstrap_ci(ds, .90, seed=SEED + 1)

    # Quality-control gate has precedence over an apparently favorable result.
    if not qc["quality_control_pass"]:
        outcome = "INCONCLUSIVE — TASK/MEASUREMENT VALIDITY FAILURE"
    elif ci95[1] < 0:
        outcome = "CONTROL_ADVANTAGE / FALSIFIED_AT_TESTED_SCOPE"
    elif ci90[0] > -SESOI and ci90[1] < SESOI:
        outcome = "EQUIVALENT / DOWNGRADE"
    elif p < ALPHA and D >= SESOI and ci95[0] > 0:
        outcome = "SURVIVED_AT_TESTED_SCOPE"
    else:
        outcome = "INCONCLUSIVE"

    return {
        "n": len(ds),
        **qc,
        "target_mean": statistics.fmean(targets),
        "control_mean": statistics.fmean(controls),
        "D": D,
        "dz": dz,
        "p": p,
        "ci95": ci95,
        "ci90": ci90,
        "outcome": outcome,
    }


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("usage: analyze_confirmatory.py DATA.csv REVEALED_BLIND_KEY.csv")
    for k, v in compute(sys.argv[1], sys.argv[2]).items():
        print(f"{k}: {v}")
