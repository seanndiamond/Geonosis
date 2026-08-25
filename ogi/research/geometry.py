from __future__ import annotations

from dataclasses import dataclass
from math import hypot
from statistics import mean
from typing import Iterable, Mapping


@dataclass(frozen=True)
class LandmarkComparison:
    feature: str
    reference_value: float
    derivative_value: float
    absolute_delta: float
    tolerance: float
    status: str


def normalized_position(*, point: float, origin: float, endpoint: float) -> float:
    """Normalize a one-dimensional landmark to a local anatomical/object frame.

    Example: waist=0 and skirt hem=1 permits hand positions to be compared across
    differently scaled figures and images. No claim about the meaning of the
    landmark is made here; this is measurement only.
    """
    span = endpoint - origin
    if span == 0:
        raise ValueError("normalization frame has zero span")
    return (point - origin) / span


def compare_normalized_feature(*, feature: str, reference_value: float,
                               derivative_value: float,
                               tolerance: float = 0.08) -> LandmarkComparison:
    delta = abs(reference_value - derivative_value)
    return LandmarkComparison(
        feature=feature,
        reference_value=reference_value,
        derivative_value=derivative_value,
        absolute_delta=delta,
        tolerance=tolerance,
        status="MISMATCH" if delta > tolerance else "WITHIN_TOLERANCE",
    )


def hand_to_skirt_ratio(*, hand_y: float, waist_y: float, skirt_hem_y: float) -> float:
    """Return hand height in a waist-to-skirt-hem frame: waist=0, hem=1."""
    return normalized_position(point=hand_y, origin=waist_y, endpoint=skirt_hem_y)


def point_distance(a: tuple[float, float], b: tuple[float, float]) -> float:
    return hypot(a[0] - b[0], a[1] - b[1])


def repeated_feature_shift(reference: Iterable[float], derivative: Iterable[float],
                           *, tolerance: float = 0.08) -> dict:
    """Test whether a derivative exhibits a repeated shift across matched figures.

    Inputs are already-normalized corresponding measurements. This deliberately
    avoids inferring cause. A repeated mismatch can motivate hypotheses such as
    regularization, copying error or geometric distortion, each of which requires
    separate testing.
    """
    ref = tuple(reference)
    der = tuple(derivative)
    if not ref or len(ref) != len(der):
        raise ValueError("reference and derivative must contain equal non-zero measurements")
    deltas = tuple(d - r for r, d in zip(ref, der))
    abs_deltas = tuple(abs(x) for x in deltas)
    return {
        "count": len(ref),
        "mean_signed_shift": mean(deltas),
        "mean_absolute_shift": mean(abs_deltas),
        "mismatch_count": sum(x > tolerance for x in abs_deltas),
        "systematic_mismatch": all(x > tolerance for x in abs_deltas),
        "directionally_consistent": all(x >= 0 for x in deltas) or all(x <= 0 for x in deltas),
    }


def fidelity_verdict(measurements: Iterable[LandmarkComparison]) -> Mapping[str, str]:
    """Issue a feature-scope fidelity verdict, never a blanket image verdict."""
    rows = tuple(measurements)
    if not rows:
        return {"status": "NOT_TESTED", "reason": "No comparable landmarks supplied"}
    mismatches = [r for r in rows if r.status == "MISMATCH"]
    if mismatches:
        return {
            "status": "GEOMETRICALLY_UNRELIABLE_AT_TESTED_FEATURE_SCOPE",
            "reason": ", ".join(r.feature for r in mismatches),
        }
    return {
        "status": "WITHIN_TOLERANCE_AT_TESTED_FEATURE_SCOPE",
        "reason": "All tested landmarks fall within declared tolerance",
    }
