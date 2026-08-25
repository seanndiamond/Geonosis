from research.impact import (
    INVALID_AT_CLAIM_SCOPE,
    OPEN,
    SUPPORTED,
    assess_derivative_impact,
    summarize_impact,
)


def test_defective_facsimile_invalidates_material_downstream_claim_without_independent_support():
    impacts = assess_derivative_impact(
        defective_source_id="facsimile_A",
        defective_feature="horizontal_rope_geometry",
        downstream_claims=[{
            "claim_id": "sled_water_model",
            "material_features": ["horizontal_rope_geometry"],
            "dependency_path": ["wall", "facsimile_A", "paper_1"],
            "independent_support": False,
        }],
    )
    assert impacts[0].status == INVALID_AT_CLAIM_SCOPE


def test_independent_route_prevents_automatic_invalidation_but_requires_audit():
    impacts = assess_derivative_impact(
        defective_source_id="facsimile_A",
        defective_feature="horizontal_rope_geometry",
        downstream_claims=[{
            "claim_id": "sled_water_model",
            "material_features": ["horizontal_rope_geometry"],
            "dependency_path": ["wall", "facsimile_A", "paper_1"],
            "independent_support": True,
        }],
    )
    assert impacts[0].status == OPEN


def test_unrelated_claim_is_not_invalidated():
    impacts = assess_derivative_impact(
        defective_source_id="facsimile_A",
        defective_feature="horizontal_rope_geometry",
        downstream_claims=[{
            "claim_id": "pigment_claim",
            "material_features": ["pigment_colour"],
            "dependency_path": ["wall", "facsimile_A", "paper_2"],
            "independent_support": False,
        }],
    )
    assert impacts[0].status == SUPPORTED


def test_impact_summary_never_inferrs_intent():
    impacts = assess_derivative_impact(
        defective_source_id="facsimile_A",
        defective_feature="horizontal_rope_geometry",
        downstream_claims=[
            {
                "claim_id": "c1",
                "material_features": ["horizontal_rope_geometry"],
                "dependency_path": ["facsimile_A"],
                "independent_support": False,
            },
            {
                "claim_id": "c2",
                "material_features": ["horizontal_rope_geometry"],
                "dependency_path": ["facsimile_A"],
                "independent_support": True,
            },
        ],
    )
    summary = summarize_impact(impacts)
    assert summary["affected_claim_count"] == 2
    assert summary["invalid_at_claim_scope_count"] == 1
    assert summary["independent_route_audit_count"] == 1
    assert summary["intent_finding"] == "NOT_EVALUATED_BY_IMPACT_PROPAGATION"
