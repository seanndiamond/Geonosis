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
    k=(len(xs)-1)*q
    f=math.floor(k); c=math.ceil(k)
    if f==c: return xs[int(k)]
    return xs[f]*(c-k)+xs[c]*(k-f)

def bootstrap_ci(ds, level=.95, n=N_BOOT, seed=SEED):
    rng=random.Random(seed)
    vals=[]
    for _ in range(n):
        samp=[rng.choice(ds) for _ in ds]
        vals.append(statistics.fmean(samp))
    a=(1-level)/2
    return percentile(vals,a), percentile(vals,1-a)

def signflip_p(ds, n=N_PERM, seed=SEED):
    obs=abs(statistics.fmean(ds))
    if len(ds) <= 20:
        total=2**len(ds)
        ge=0
        for mask in range(total):
            val=statistics.fmean(d if (mask>>i)&1 else -d for i,d in enumerate(ds))
            ge += abs(val) >= obs - 1e-12
        return ge/total
    rng=random.Random(seed)
    ge=0
    for _ in range(n):
        val=statistics.fmean(d if rng.random()<.5 else -d for d in ds)
        ge += abs(val) >= obs - 1e-12
    return (ge+1)/(n+1)

def load_key(path):
    key={}
    for r in csv.DictReader(open(path,newline="",encoding="utf-8")):
        key[r["stimulus_id"]] = r["condition"]
    return key

def compute(data_path, key_path):
    key=load_key(key_path)
    trans=defaultdict(list)
    for r in csv.DictReader(open(data_path,newline="",encoding="utf-8")):
        if str(r["technical_ok"]).lower() not in {"1","true"}:
            continue
        if int(r["orientation_index"]) == 1:
            continue
        c=float(r["coherence"]); g=float(r["grouping_change"]); m=float(r["mere_rotation"])
        odrr=(c+g+(10-m))/3
        trans[(r["participant_token"],r["stimulus_id"])].append(odrr)
    source_mean={k:statistics.fmean(v) for k,v in trans.items() if v}
    pc=defaultdict(list)
    for (p,s),v in source_mean.items():
        pc[(p,key[s])].append(v)
    participants=sorted({p for p,_ in pc})
    ds=[]; targets=[]; controls=[]
    for p in participants:
        if not pc[(p,"TARGET")] or not pc[(p,"CONTROL")]:
            continue
        t=statistics.fmean(pc[(p,"TARGET")])
        c=statistics.fmean(pc[(p,"CONTROL")])
        targets.append(t); controls.append(c); ds.append(t-c)
    if len(ds)<2:
        raise ValueError("insufficient participants")
    D=statistics.fmean(ds)
    sd=statistics.stdev(ds)
    dz=D/sd if sd else float("inf")
    p=signflip_p(ds)
    ci95=bootstrap_ci(ds,.95)
    ci90=bootstrap_ci(ds,.90,seed=SEED+1)
    if ci95[1] < 0:
        outcome="CONTROL_ADVANTAGE / FALSIFIED_AT_TESTED_SCOPE"
    elif ci90[0] > -SESOI and ci90[1] < SESOI:
        outcome="EQUIVALENT / DOWNGRADE"
    elif p < ALPHA and D >= SESOI and ci95[0] > 0:
        outcome="SURVIVED_AT_TESTED_SCOPE"
    else:
        outcome="INCONCLUSIVE"
    return {
        "n":len(ds),
        "target_mean":statistics.fmean(targets),
        "control_mean":statistics.fmean(controls),
        "D":D,
        "dz":dz,
        "p":p,
        "ci95":ci95,
        "ci90":ci90,
        "outcome":outcome
    }

if __name__ == "__main__":
    if len(sys.argv)!=3:
        raise SystemExit("usage: analyze_confirmatory.py DATA.csv REVEALED_BLIND_KEY.csv")
    for k,v in compute(sys.argv[1],sys.argv[2]).items():
        print(f"{k}: {v}")
