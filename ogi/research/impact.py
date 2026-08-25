from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


INVALID_AT_CLAIM_SCOPE = "INVALID_AT_CLAIM_SCOPE"
OPEN = "OPEN"
SUPPORTED = "SUPPORTED"


@dataclass(frozen=True)
class DownstreamImpact:
    claim_id: str
    status: str
    defective_feature: str
    dependency_path: tuple[str, ...]
    independent_support: bool
    reversal_condition: str


def assess_derivative_impact(*, defective_source_id: str, defective_feature: str,
                             downstream_claims: Iterable[dict]) -> tuple[DownstreamImpact, ...]:
    """Propagate a demonstrated derivative defect only along material dependencies.

    This function does not infer intent and does not assume that every downstream
    claim using the source is invalid. A claim is blocked only when the defective
    feature is material to that claim and no evidentially independent route survives.
    """
    impacts: list[DownstreamImpact] = []

    for claim in downstream_claims:
        claim_id = claim["claim_id"]
        material_features = set(claim.get("material_features", ()))
        path = tuple(claim.get("dependency_path", ()))
        independent_support = bool(claim.get("independent_support", False))

        depends_on_source = defective_source_id in path
        depends_on_feature = defective_feature in material_features

        if depends_on_source and depends_on_feature and not independent_support:
            status = INVALID_AT_CLAIM_SCOPE
            reversal = (
                "Re-derive the material feature from an authenticated upstream exhibit "
                "or establish an evidentially independent chain at the required stage."
            )
        elif depends_on_source and depends_on_feature and independent_support:
            status = OPEN
            reversal = "Audit and derive the claimed independent evidentiary route."
        else:
            status = SUPPORTED
            reversal = "No reversal condition from this derivative defect at the tested scope."

        impacts.append(DownstreamImpact(
            claim_id=claim_id,
            status=status,
            defective_feature=defective_feature,
            dependency_path=path,
            independent_support=independent_support,
            reversal_condition=reversal,
        ))

    return tuple(impacts)


def summarize_impact(impacts: Iterable[DownstreamImpact]) -> dict:
    rows = tuple(impacts)
    return {
        "affected_claim_count": sum(r.status in {INVALID_AT_CLAIM_SCOPE, OPEN} for r in rows),
        "invalid_at_claim_scope_count": sum(r.status == INVALID_AT_CLAIM_SCOPE for r in rows),
        "independent_route_audit_count": sum(r.status == OPEN for r in rows),
        "unaffected_at_tested_scope_count": sum(r.status == SUPPORTED for r in rows),
        "intent_finding": "NOT_EVALUATED_BY_IMPACT_PROPAGATION",
    }
