from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, Iterable, List

STAGE_ORDER = [
    "CITED", "LOCATED", "RETRIEVED", "INSPECTED", "MAPPED",
    "DERIVED", "REPRODUCED", "CHALLENGED", "SURVIVED",
]
STAGE_INDEX = {stage: i for i, stage in enumerate(STAGE_ORDER)}


class CourtViolation(ValueError):
    pass


@dataclass
class ClaimState:
    claim_id: str
    stage: str | None = None
    status: str = "OPEN"
    sources: List[str] = field(default_factory=list)
    reversal_conditions: List[str] = field(default_factory=list)
    lineage: List[Dict[str, Any]] = field(default_factory=list)
    blocked_by: List[str] = field(default_factory=list)


def _validate_stage_transition(previous: str | None, proposed: str) -> None:
    if proposed not in STAGE_INDEX:
        raise CourtViolation(f"Unknown epistemic stage: {proposed}")
    if previous is None:
        if proposed != "CITED":
            raise CourtViolation("A claim must enter the Court at CITED unless an explicit import event records prior earned state.")
        return
    if STAGE_INDEX[proposed] > STAGE_INDEX[previous] + 1:
        raise CourtViolation(f"Silent stage jump prohibited: {previous} -> {proposed}")


def project(events: Iterable[Dict[str, Any]]) -> Dict[str, ClaimState]:
    """Deterministically reconstruct Court state from immutable events."""
    claims: Dict[str, ClaimState] = {}

    for event in events:
        kind = event["type"]
        claim_id = event["claim_id"]
        state = claims.setdefault(claim_id, ClaimState(claim_id=claim_id))

        if kind == "CLAIM_CITED":
            _validate_stage_transition(state.stage, "CITED")
            state.stage = "CITED"
            if event.get("source_id"):
                state.sources.append(event["source_id"])

        elif kind == "STAGE_EARNED":
            proposed = event["stage"]
            if not event.get("evidence_event_ids"):
                raise CourtViolation("A stage cannot be earned without evidence event references.")
            _validate_stage_transition(state.stage, proposed)
            state.stage = proposed

        elif kind == "BLOCKED":
            reason = event["reason"]
            if reason not in state.blocked_by:
                state.blocked_by.append(reason)

        elif kind == "REVERSAL_CONDITION_SET":
            condition = event["condition"]
            if condition not in state.reversal_conditions:
                state.reversal_conditions.append(condition)

        elif kind == "SUPERSEDED":
            state.lineage.append({
                "superseded_event": event.get("superseded_event"),
                "reason": event["reason"],
                "replacement_claim_id": event.get("replacement_claim_id"),
            })
            state.status = "SUPERSEDED"

        elif kind == "FAILED":
            state.status = "FAILED"

        elif kind == "REOPENED":
            if event.get("trigger_type") not in {
                "NEW_EVIDENCE", "CONTRADICTION", "METHODOLOGICAL_FLAW",
                "FAILED_PREDICTION", "UPSTREAM_STATE_CHANGE",
            }:
                raise CourtViolation("Invalid reopen trigger")
            state.status = "OPEN"

        elif kind in {"SEARCH_EVENT", "RETRIEVAL_EVENT", "AUTHENTICATION_EVENT", "INSPECTION_EVENT"}:
            # Research events are preserved but do not automatically upgrade claim state.
            pass

        else:
            raise CourtViolation(f"Unknown event type: {kind}")

    return claims
