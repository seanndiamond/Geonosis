from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class TrialResult:
    passed: bool
    failures: tuple[str, ...]


def evaluate(events: Iterable[dict]) -> TrialResult:
    events = list(events)
    failures: list[str] = []

    earned = {}
    for event in events:
        if event.get("type") == "STAGE_EARNED":
            earned.setdefault(event["claim_id"], []).append(event["stage"])

    # No claim may have INSPECTED without a prior retrieval and an inspection event.
    for claim_id, stages in earned.items():
        if "INSPECTED" in stages:
            if "RETRIEVED" not in stages:
                failures.append(f"{claim_id}: INSPECTED without RETRIEVED")
            if not any(e.get("type") == "INSPECTION_EVENT" and e.get("claim_id") == claim_id for e in events):
                failures.append(f"{claim_id}: INSPECTED without inspection event")

    # Institutional limitations may not silently mitigate a case.
    for event in events:
        if event.get("type") == "INSTITUTIONAL_LIMITATION_ACCEPTED" and not event.get("evidence_event_ids"):
            failures.append("Institutional limitation accepted without evidence")

    # Search failures must be retained, not omitted from the record.
    searches = [e for e in events if e.get("type") == "SEARCH_EVENT"]
    if searches and not all("outcome" in e for e in searches):
        failures.append("One or more searches lack recorded outcomes")

    # A successful trial must leave at least one explicit provenance edge or blocked link.
    has_mapping = any(e.get("type") in {"PROVENANCE_EDGE", "BLOCKED"} for e in events)
    if not has_mapping:
        failures.append("No provenance edge or blocked link recorded")

    # Claims of intent are forbidden without an explicit intent evidence chain.
    for event in events:
        if event.get("type") == "INTENT_FINDING" and not event.get("evidence_event_ids"):
            failures.append("Intent finding entered without evidence chain")

    return TrialResult(passed=not failures, failures=tuple(failures))
