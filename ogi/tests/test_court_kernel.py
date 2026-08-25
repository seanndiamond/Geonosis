import pytest

from kernel.state import CourtViolation, project
from research.dependency import INVALID_AT_CLAIM_SCOPE, assess_damage_attribution, assess_material_dependency
from research.planner import plan_provenance_work
from research.provenance import classify_research_result, institutional_limitation_claim


def test_citation_does_not_become_inspection():
    assert classify_research_result(
        has_mention=True,
        has_catalogue_identity=False,
        bytes_retrieved=False,
        authenticated=False,
        inspected=False,
    ) == "CITED"


def test_catalogue_location_does_not_become_retrieval():
    assert classify_research_result(
        has_mention=True,
        has_catalogue_identity=True,
        bytes_retrieved=False,
        authenticated=False,
        inspected=False,
    ) == "LOCATED"


def test_silent_stage_jump_is_rejected():
    events = [
        {"type": "CLAIM_CITED", "claim_id": "x", "source_id": "s1"},
        {"type": "STAGE_EARNED", "claim_id": "x", "stage": "INSPECTED", "evidence_event_ids": ["e1"]},
    ]
    with pytest.raises(CourtViolation):
        project(events)


def test_supersession_preserves_lineage():
    state = project([
        {"type": "CLAIM_CITED", "claim_id": "x", "source_id": "s1"},
        {"type": "SUPERSEDED", "claim_id": "x", "reason": "new evidence", "superseded_event": "old", "replacement_claim_id": "y"},
    ])["x"]
    assert state.status == "SUPERSEDED"
    assert state.lineage[0]["reason"] == "new evidence"


def test_unverified_institutional_excuse_generates_research_task():
    limitation = institutional_limitation_claim("The source may be lost in the archive")
    tasks = plan_provenance_work([{
        "claim_id": "x",
        "stage": "CITED",
        "target": "primary exhibit",
        "downstream_dependence": 10,
        "primary_exhibit_access": "UNKNOWN",
        "institutional_limitations": [limitation],
        "reversal_conditions": [],
    }])
    types = {task.task_type for task in tasks}
    assert "VERIFY_LIMITATION_CLAIM" in types
    assert "ESCALATE_CITATION_EXHIBIT_GAP" in types


def test_reversal_condition_becomes_active_work():
    tasks = plan_provenance_work([{
        "claim_id": "x",
        "stage": "LOCATED",
        "target": "decisive exhibit",
        "downstream_dependence": 8,
        "primary_exhibit_access": "LOW",
        "institutional_limitations": [],
        "reversal_conditions": ["Retrieve and authenticate the decisive upstream exhibit"],
    }])
    assert tasks[0].task_type == "WORK_REVERSAL_CONDITION"


def test_failed_material_dependency_invalidates_only_at_claim_scope():
    verdict = assess_material_dependency(
        claim_id="paper_claim",
        dependencies=[{
            "exhibit_id": "decisive_photo",
            "material": True,
            "stage": "LOCATED",
            "required_stage": "INSPECTED",
        }],
        independent_support=False,
    )
    assert verdict.status == INVALID_AT_CLAIM_SCOPE
    assert verdict.failed_dependencies == ("decisive_photo",)


def test_independent_evidence_prevents_automatic_whole_claim_invalidation():
    verdict = assess_material_dependency(
        claim_id="paper_claim",
        dependencies=[{
            "exhibit_id": "missing_photo",
            "material": True,
            "stage": "CITED",
            "required_stage": "INSPECTED",
        }],
        independent_support=True,
    )
    assert verdict.status == "OPEN"


def test_general_vandalism_does_not_prove_specific_feature_loss():
    result = assess_damage_attribution(
        observed_damage=True,
        causal_label="vandalism",
        causal_evidence_ids=["historical_report"],
        specific_feature="horizontal rope",
        feature_loss_evidence_ids=[],
    )
    assert result["damage_observation"] == "ESTABLISHED"
    assert result["causal_attribution"] == "EVIDENCE_PRESENT_REQUIRES_DERIVATION"
    assert result["specific_feature_loss"] == "UNSUPPORTED_SPECIFIC_ATTRIBUTION"


def test_damage_model_must_account_for_surviving_morphology():
    result = assess_damage_attribution(
        observed_damage=True,
        causal_label="vandalism",
        causal_evidence_ids=["historical_report"],
        morphology_explained=False,
    )
    assert result["damage_model_status"] == "INCOMPLETE_MODEL"
