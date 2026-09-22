#!/usr/bin/env python3
import hashlib
import random
import sys

MASTER_SEED = "20260907"
ORIENTATIONS = [0, 90, 180, 270]

def participant_seed(token: str) -> int:
    raw = f"{MASTER_SEED}|{token}".encode("utf-8")
    return int(hashlib.sha256(raw).hexdigest()[:16], 16)

def randomized_plan(token: str, stimulus_ids):
    rng = random.Random(participant_seed(token))
    ids = list(stimulus_ids)
    rng.shuffle(ids)
    plan = []
    for sid in ids:
        orientations = ORIENTATIONS[:]
        rng.shuffle(orientations)
        plan.append((sid, orientations))
    return plan

if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise SystemExit("usage: generate_randomization.py PARTICIPANT_TOKEN S001 S002 ...")
    for sid, seq in randomized_plan(sys.argv[1], sys.argv[2:]):
        print(sid + "," + ",".join(map(str, seq)))
