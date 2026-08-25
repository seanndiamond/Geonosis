from research.assertions import (
    ASSERTION_ONLY,
    EVENT_EVIDENCE_LINKED,
    TRANSMITTED_ASSERTION,
    assess_assertion_source,
)


def test_inspected_historical_statement_is_not_event_evidence():
    result = assess_assertion_source(
        source_inspected=True,
        asserts_event=True,
        reports_another_person=False,
        event_evidence_ids=[],
    )
    assert result.source_status == "INSPECTED"
    assert result.event_status == ASSERTION_ONLY


def test_report_of_report_is_transmission_not_corroboration():
    result = assess_assertion_source(
        source_inspected=True,
        asserts_event=True,
        reports_another_person=True,
        event_evidence_ids=[],
    )
    assert result.event_status == TRANSMITTED_ASSERTION


def test_event_evidence_must_be_linked_separately():
    result = assess_assertion_source(
        source_inspected=True,
        asserts_event=True,
        reports_another_person=False,
        event_evidence_ids=["before_after_exhibit", "physical_signature"],
    )
    assert result.event_status == EVENT_EVIDENCE_LINKED


def test_uninspected_source_cannot_establish_even_its_assertion_contents():
    result = assess_assertion_source(
        source_inspected=False,
        asserts_event=True,
        event_evidence_ids=[],
    )
    assert result.source_status == "NOT_INSPECTED"
    assert result.event_status == "UNSUPPORTED"
