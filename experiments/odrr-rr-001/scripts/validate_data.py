#!/usr/bin/env python3
import csv
import sys

REQUIRED = {
    "participant_token", "stimulus_id", "orientation_index",
    "coherence", "grouping_change", "mere_rotation", "technical_ok"
}

def as_float(v, field):
    x = float(v)
    if not (0 <= x <= 10):
        raise ValueError(f"{field} outside 0..10: {x}")
    return x

def validate(path):
    rows = list(csv.DictReader(open(path, newline="", encoding="utf-8")))
    if not rows:
        raise ValueError("no data rows")
    missing = REQUIRED - set(rows[0].keys())
    if missing:
        raise ValueError(f"missing columns: {sorted(missing)}")
    for i,row in enumerate(rows, start=2):
        as_float(row["coherence"], "coherence")
        if row["orientation_index"] != "1":
            as_float(row["grouping_change"], "grouping_change")
        as_float(row["mere_rotation"], "mere_rotation")
        if row["technical_ok"] not in {"0","1","true","false","TRUE","FALSE"}:
            raise ValueError(f"bad technical_ok on line {i}")
    print(f"VALID: {len(rows)} rows")

if __name__ == "__main__":
    validate(sys.argv[1])
