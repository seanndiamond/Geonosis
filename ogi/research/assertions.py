from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


ASSERTION_ONLY = "ASSERTION_ONLY"
TRANSMITTED_ASSERTION = "TRANSMITTED_ASSERTION"
EVENT_EVIDENCE_LINKED = "EVENT_EVIDENCE_LINKED"


@dataclass(frozen=True)
class AssertionAssessment:
    source_status: str
    event_status: str
    reason: str


def assess_assertion_source(*, source_inspected: bool, asserts_event: bool,
                            reports_another_person: bool = False,
                            event_evidence_ids: Iterable[str] = ()) -> AssertionAssessment:
    """Prevent an inspected assertion-source from becoming proof of its asserted event.

    Inspection establishes what the source says. It does not transfer INSPECTED or
    any truth status to the event described by the source. Event-specific evidence
    must be linked separately.
    """
    event_evidence = tuple(event_evidence_ids)

    if not source_inspected:
        return AssertionAssessment(
            source_status="NOT_INSPECTED",
            event_status="UNSUPPORTED",
            reason="The source itself has not been inspected.",
        )

    if not asserts_event:
        return AssertionAssessment(
            source_status="INSPECTED",
            event_status="NOT_CLAIMED",
            reason="The inspected source does not assert the tested event.",
        )

    if event_evidence:
        return AssertionAssessment(
            source_status="INSPECTED",
            event_status=EVENT_EVIDENCE_LINKED,
            reason="The assertion is recorded and separate event-specific evidence is linked for prosecution.",
        )

    if reports_another_person:
        return AssertionAssessment(
            source_status="INSPECTED",
            event_status=TRANSMITTED_ASSERTION,
            reason="The source establishes transmission of another person's assertion, not the occurrence of the event.",
        )

    return AssertionAssessment(
        source_status="INSPECTED",
        event_status=ASSERTION_ONLY,
        reason="The source establishes that the author asserted the event; the event itself remains unestablished.",
    )
