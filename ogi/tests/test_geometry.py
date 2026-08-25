from research.geometry import (
    compare_normalized_feature,
    fidelity_verdict,
    hand_to_skirt_ratio,
    repeated_feature_shift,
)


def test_hand_to_skirt_ratio_uses_local_frame():
    assert hand_to_skirt_ratio(hand_y=150, waist_y=100, skirt_hem_y=200) == 0.5
    assert hand_to_skirt_ratio(hand_y=200, waist_y=100, skirt_hem_y=200) == 1.0


def test_large_hand_position_shift_is_geometric_mismatch():
    comparison = compare_normalized_feature(
        feature="hand endpoint relative to skirt hem",
        reference_value=0.5,
        derivative_value=1.0,
        tolerance=0.08,
    )
    assert comparison.status == "MISMATCH"
    assert comparison.absolute_delta == 0.5


def test_repeated_downward_shift_is_detected_without_inferring_cause():
    result = repeated_feature_shift(
        reference=[0.48, 0.52, 0.50, 0.55],
        derivative=[0.96, 1.02, 0.98, 1.00],
        tolerance=0.08,
    )
    assert result["systematic_mismatch"] is True
    assert result["directionally_consistent"] is True
    assert result["mismatch_count"] == 4


def test_fidelity_verdict_is_feature_scoped_not_blanket():
    measurement = compare_normalized_feature(
        feature="hand endpoint relative to skirt hem",
        reference_value=0.5,
        derivative_value=1.0,
    )
    verdict = fidelity_verdict([measurement])
    assert verdict["status"] == "GEOMETRICALLY_UNRELIABLE_AT_TESTED_FEATURE_SCOPE"
