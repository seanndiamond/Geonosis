"""Minimal executable reference for the OGI/Oggy Return Controller v0.2.

This is deliberately small. It does not implement an LLM agent, memory system, or
full policy engine. It demonstrates one testable proposition: consequential action
should be gated by objective/proxy, permission, authority, current-state and return
conditions rather than by model output alone.
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from enum import Enum
from typing import Any, Dict, Iterable, List, Optional


class Decision(str, Enum):
    AUTHORIZE = "AUTHORIZE"
    SAFE_EXIT = "SAFE_EXIT"
    REEVALUATE = "REEVALUATE"
    REOPEN_AND_REEVALUATE = "REOPEN_AND_REEVALUATE"


class SafeExit(str, Enum):
    UNRESOLVED = "UNRESOLVED"
    INSUFFICIENT_EVIDENCE = "INSUFFICIENT_EVIDENCE"
    IMPOSSIBLE_UNDER_CONSTRAINTS = "IMPOSSIBLE_UNDER_CONSTRAINTS"
    PERMISSION_REQUIRED = "PERMISSION_REQUIRED"
    AUTHORITY_CONFLICT = "AUTHORITY_CONFLICT"
    HUMAN_REVIEW_REQUIRED = "HUMAN_REVIEW_REQUIRED"


@dataclass(frozen=True)
class ReturnDecision:
    decision: Decision
    safe_exit: Optional[SafeExit]
    reason: str
    next_legitimate_action: str
    rf_codes: List[str]

    def to_dict(self) -> Dict[str, Any]:
        result = asdict(self)
        result["decision"] = self.decision.value
        result["safe_exit"] = self.safe_exit.value if self.safe_exit else None
        return result


def _rf_codes(record: Dict[str, Any]) -> List[str]:
    return [
        event.get("rf_code", "")
        for event in record.get("divergence_events", [])
        if event.get("rf_code")
    ]


def _safe_exit_allowed(record: Dict[str, Any], exit_name: SafeExit) -> bool:
    allowed: Iterable[str] = record.get("allowed_safe_exits", [])
    return exit_name.value in set(allowed)


def _latest_reopen_trigger(record: Dict[str, Any]) -> bool:
    corrections = record.get("correction_events", [])
    if not corrections:
        return False
    return bool(corrections[-1].get("reopen_trigger_present", False))


def evaluate_return_state(record: Dict[str, Any]) -> ReturnDecision:
    """Evaluate a machine-readable OGI return-state record.

    This function is intentionally conservative. It authorizes only when the
    hard relational checks are clear. Unknown or conflicting consequential state
    routes to a safe exit or reevaluation rather than fabricated completion.
    """

    rf_codes = _rf_codes(record)
    permission = record.get("permission_state", "UNKNOWN")
    authority = record.get("authority_state", "UNKNOWN")
    proxy = record.get("proxy_state", "UNKNOWN")
    objective = record.get("objective_state", "MISSING")
    orientation = record.get("orientation_state", "AMBIGUOUS")
    return_status = record.get("return_status", "NOT_REQUIRED")

    if permission == "PROHIBITED":
        return ReturnDecision(
            Decision.SAFE_EXIT,
            SafeExit.PERMISSION_REQUIRED,
            "The proposed action is prohibited by the current permission state.",
            "Request explicit authorization or choose an authorized alternative.",
            rf_codes,
        )

    if permission in {"REQUIRES_REVIEW", "UNKNOWN"}:
        return ReturnDecision(
            Decision.SAFE_EXIT,
            SafeExit.HUMAN_REVIEW_REQUIRED,
            "Permission is not sufficiently clear for consequential action.",
            "Obtain operator review before acting.",
            rf_codes,
        )

    if authority == "CONFLICTING":
        return ReturnDecision(
            Decision.SAFE_EXIT,
            SafeExit.AUTHORITY_CONFLICT,
            "The governing authority relation is internally conflicting.",
            "Resolve the authority graph before action.",
            rf_codes,
        )

    if authority == "UNKNOWN":
        return ReturnDecision(
            Decision.SAFE_EXIT,
            SafeExit.HUMAN_REVIEW_REQUIRED,
            "The system cannot identify the governing authority.",
            "Establish the governing authority before action.",
            rf_codes,
        )

    if objective in {"CONFLICTED", "MISSING"}:
        return ReturnDecision(
            Decision.SAFE_EXIT,
            SafeExit.HUMAN_REVIEW_REQUIRED,
            "The declared objective is missing or conflicted.",
            "Clarify the objective before optimizing any proxy.",
            rf_codes,
        )

    if proxy in {"CONFLICTING", "DOMINANT"} or "RF-02_PROXY_CAPTURE" in rf_codes:
        return ReturnDecision(
            Decision.SAFE_EXIT,
            SafeExit.HUMAN_REVIEW_REQUIRED,
            "The operative proxy has separated from or displaced the declared objective.",
            "Return to the declared objective and review the proxy/reward design.",
            rf_codes,
        )

    if "RF-06_REWARD_TAMPERING" in rf_codes:
        return ReturnDecision(
            Decision.SAFE_EXIT,
            SafeExit.HUMAN_REVIEW_REQUIRED,
            "Reward or evaluator tampering has been detected.",
            "Preserve actual task status and route the event to review.",
            rf_codes,
        )

    if "RF-03_STATE_REGRESSION" in rf_codes:
        if _latest_reopen_trigger(record):
            return ReturnDecision(
                Decision.REOPEN_AND_REEVALUATE,
                None,
                "State regression coincides with a recorded reopen trigger.",
                "Reopen only the affected state, preserve lineage, and reevaluate.",
                rf_codes,
            )
        return ReturnDecision(
            Decision.REEVALUATE,
            None,
            "A stale or superseded state has displaced the current warranted state.",
            "Recover the latest warranted state and regenerate from corrected context.",
            rf_codes,
        )

    if "RF-07_IMPOSSIBLE_TASK_ESCALATION" in rf_codes:
        if _safe_exit_allowed(record, SafeExit.IMPOSSIBLE_UNDER_CONSTRAINTS):
            return ReturnDecision(
                Decision.SAFE_EXIT,
                SafeExit.IMPOSSIBLE_UNDER_CONSTRAINTS,
                "Legitimate completion is unavailable under current constraints.",
                "Report the constraint and stop rather than escalate into unauthorized routes.",
                rf_codes,
            )
        return ReturnDecision(
            Decision.SAFE_EXIT,
            SafeExit.HUMAN_REVIEW_REQUIRED,
            "Impossible-task escalation is present but no explicit safe exit is configured.",
            "Add or authorize a legitimate safe-failure state.",
            rf_codes,
        )

    if "RF-09_CORRECTION_REJECTION" in rf_codes:
        return ReturnDecision(
            Decision.SAFE_EXIT,
            SafeExit.HUMAN_REVIEW_REQUIRED,
            "A valid correction has not changed operative state.",
            "Freeze consequential action and repair state-control before continuing.",
            rf_codes,
        )

    if "RF-10_FALSE_RETURN" in rf_codes or return_status == "FALSE_RETURN_SUSPECTED":
        return ReturnDecision(
            Decision.REEVALUATE,
            None,
            "Compliance language is not sufficient evidence that operative state returned.",
            "Verify state identifiers, proxy state and queued actions before authorization.",
            rf_codes,
        )

    if orientation in {"DRIFTING", "OUT_OF_PATH"}:
        if return_status in {"RETURN_AVAILABLE", "RETURN_IN_PROGRESS", "RETURNED"}:
            return ReturnDecision(
                Decision.REEVALUATE,
                None,
                "The system is off-path but has a represented return route.",
                "Complete return, rerun checks, then reconsider action.",
                rf_codes,
            )
        return ReturnDecision(
            Decision.SAFE_EXIT,
            SafeExit.UNRESOLVED,
            "The system is off-path and no trustworthy return route is represented.",
            "Stop and reconstruct the governing field.",
            rf_codes,
        )

    return ReturnDecision(
        Decision.AUTHORIZE,
        None,
        "Hard objective, proxy, permission, authority and return checks are clear.",
        "Proceed while preserving the event and state log.",
        rf_codes,
    )


if __name__ == "__main__":
    import argparse
    import json
    from pathlib import Path

    parser = argparse.ArgumentParser(description="Evaluate an OGI return-state JSON record.")
    parser.add_argument("record", type=Path, help="Path to return-state JSON")
    args = parser.parse_args()

    payload = json.loads(args.record.read_text(encoding="utf-8"))
    print(json.dumps(evaluate_return_state(payload).to_dict(), indent=2))
