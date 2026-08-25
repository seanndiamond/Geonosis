from __future__ import annotations

import argparse
import json
from pathlib import Path

from benchmarks.brown_1889.evaluator import evaluate
from kernel.state import project
from research.planner import plan_provenance_work


def load_jsonl(path: Path):
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def main() -> int:
    parser = argparse.ArgumentParser(description="Run Court projection and Brown provenance trial checks")
    parser.add_argument("events", type=Path, help="JSONL event log")
    args = parser.parse_args()

    events = load_jsonl(args.events)
    states = project(events)
    trial = evaluate(events)

    claims_for_planner = []
    for claim_id, state in states.items():
        claims_for_planner.append({
            "claim_id": claim_id,
            "target": claim_id,
            "stage": state.stage,
            "reversal_conditions": state.reversal_conditions,
            "institutional_limitations": [],
            "downstream_dependence": 0,
            "primary_exhibit_access": "UNKNOWN",
        })

    tasks = plan_provenance_work(claims_for_planner)
    print(json.dumps({
        "trial_passed": trial.passed,
        "failures": list(trial.failures),
        "claims": {k: vars(v) for k, v in states.items()},
        "next_research_tasks": [vars(t) for t in tasks],
    }, indent=2))
    return 0 if trial.passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
