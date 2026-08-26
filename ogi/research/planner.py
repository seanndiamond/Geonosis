from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List


@dataclass(frozen=True)
class ResearchTask:
    task_type: str
    target: str
    reason: str
    priority: int


def plan_provenance_work(claims: Iterable[dict]) -> List[ResearchTask]:
    """Generate general research tasks from unresolved provenance state.

    No case-specific names or expected solutions belong here.
    """
    tasks: List[ResearchTask] = []

    for claim in claims:
        stage = claim.get("stage")
        dependence = int(claim.get("downstream_dependence", 0))
        access = claim.get("primary_exhibit_access", "UNKNOWN")
        target = claim.get("target") or claim.get("claim_id", "unknown")

        if stage in {"CITED", "LOCATED"}:
            tasks.append(ResearchTask(
                task_type="TRACE_SOURCE_GENEALOGY",
                target=target,
                reason="Claim is upstream-consequential but has not reached retrieval/inspection.",
                priority=70 + min(dependence, 20),
            ))

        if dependence >= 5 and access in {"LOW", "UNKNOWN", "UNAVAILABLE"}:
            tasks.append(ResearchTask(
                task_type="ESCALATE_CITATION_EXHIBIT_GAP",
                target=target,
                reason="High downstream dependence with weak primary-exhibit accessibility.",
                priority=95,
            ))

        for condition in claim.get("reversal_conditions", []):
            tasks.append(ResearchTask(
                task_type="WORK_REVERSAL_CONDITION",
                target=condition,
                reason="Unresolved Court reversal condition is an active research duty.",
                priority=100,
            ))

        for limitation in claim.get("institutional_limitations", []):
            if limitation.get("status") != "VERIFIED":
                tasks.append(ResearchTask(
                    task_type="VERIFY_LIMITATION_CLAIM",
                    target=limitation.get("text", "unspecified limitation"),
                    reason="Institutional limitation cannot mitigate provenance failure until derived.",
                    priority=90,
                ))

    return sorted(tasks, key=lambda task: task.priority, reverse=True)
