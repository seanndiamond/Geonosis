#!/usr/bin/env python3
import csv
import math
import statistics
import sys

NUMERIC = ["aspect_ratio", "mean_luminance", "rms_contrast", "edge_strength", "entropy_bits"]


def load(path):
    rows = list(csv.DictReader(open(path, newline="", encoding="utf-8")))
    for r in rows:
        for k in NUMERIC:
            r[k] = float(r[k])
    return rows


def zscore(rows):
    means = {k: statistics.fmean(r[k] for r in rows) for k in NUMERIC}
    sds = {}
    for k in NUMERIC:
        vals = [r[k] for r in rows]
        sds[k] = statistics.stdev(vals) if len(vals) > 1 and statistics.stdev(vals) > 0 else 1.0
    for r in rows:
        for k in NUMERIC:
            r["z_" + k] = (r[k] - means[k]) / sds[k]


def distance(a, b):
    return math.sqrt(sum((a["z_" + k] - b["z_" + k]) ** 2 for k in NUMERIC))


def main(path):
    rows = load(path)
    required = {"source_id", "condition", "source_class"}
    if not rows or not required.issubset(rows[0]):
        raise ValueError("CSV requires source_id, condition, source_class and numeric feature columns")
    zscore(rows)
    targets = sorted((r for r in rows if r["condition"] == "TARGET"), key=lambda r: r["source_id"])
    available = {r["source_id"]: r for r in rows if r["condition"] == "CONTROL_CANDIDATE"}
    writer = csv.writer(sys.stdout)
    writer.writerow(["target_source_id", "control_source_id", "source_class", "standardized_distance"])
    for target in targets:
        candidates = [r for r in available.values() if r["source_class"] == target["source_class"]]
        if not candidates:
            raise ValueError(f"no remaining same-class control for {target['source_id']}")
        candidates.sort(key=lambda r: (distance(target, r), r["source_id"]))
        chosen = candidates[0]
        writer.writerow([target["source_id"], chosen["source_id"], target["source_class"], f"{distance(target, chosen):.8f}"])
        del available[chosen["source_id"]]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: match_controls.py IMAGE_FEATURES_WITH_METADATA.csv")
    main(sys.argv[1])
