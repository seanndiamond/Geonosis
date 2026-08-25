from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


INVALID_AT_CLAIM_SCOPE = "INVALID_AT_CLAIM_SCOPE"
SUPPORTED = "SUPPORTED"
OPEN = "OPEN"


@dataclass(frozen=True)
class DependencyVerdict:
    status: str
    reason: str
    failed_dependencies: tuple[str, ...] = ()


def assess_material_dependency(*, claim_id: str, dependencies: Iterable[dict], independent_support: bool = False) -> DependencyVerdict:
    """Propagate provenance failure only where the dependency is material.

    A dependency is considered failed for derivation when it is marked material and
    its exhibit cannot be produced/authenticated/inspected at the scope required by
    the claim. This is an admissibility verdict, not a truth-value verdict.
    """
    failed: list[str] = []
    for dep in dependencies:
        if not dep.get("material", False):
            continue
        stage = dep.get("stage", "NO_STAGE")
        required = dep.get("required_stage", "INSPECTED")
        order = ["NO_STAGE", "CITED", "LOCATED", "RETRIEVED", "AUTHENTICATED", "INSPECTED", "MAPPED", "DERIVED", "REPRODUCED", "CHALLENGED", "SURVIVED"]
        try:
            if order.index(stage) < order.index(required):
                failed.append(dep.get("claim_id") or dep.get("exhibit_id") or "unknown_dependency")
        except ValueError:
            failed.append(dep.get("claim_id") or dep.get("exhibit_id") or "unknown_dependency")

    if failed and not independent_support:
        return DependencyVerdict(
            status=INVALID_AT_CLAIM_SCOPE,
            reason=(f"{claim_id} materially depends on unresolved upstream evidence; "
                    "the claim is not admissible as established knowledge at this scope."),
            failed_dependencies=tuple(failed),
        )
    if failed and independent_support:
        return DependencyVerdict(
            status=OPEN,
            reason=(f"{claim_id} has a failed dependency, but an independent evidentiary route exists and must be audited separately."),
            failed_dependencies=tuple(failed),
        )
    return DependencyVerdict(status=SUPPORTED, reason=f"No unresolved material dependency blocks {claim_id} at the tested scope.")


def assess_damage_attribution(*, observed_damage: bool, causal_label: str | None,
                              causal_evidence_ids: Iterable[str] = (),
                              specific_feature: str | None = None,
                              feature_loss_evidence_ids: Iterable[str] = (),
                              morphology_explained: bool | None = None) -> dict:
    """Keep damage observation separate from causal and feature-loss claims."""
    result = {
        "damage_observation": "ESTABLISHED" if observed_damage else "NOT_ESTABLISHED",
        "causal_attribution": "NOT_CLAIMED" if not causal_label else "UNSUPPORTED",
        "specific_feature_loss": "NOT_CLAIMED" if not specific_feature else "UNSUPPORTED",
        "morphology_fit": "NOT_TESTED" if morphology_explained is None else ("EXPLAINED" if morphology_explained else "UNEXPLAINED"),
    }

    if causal_label and tuple(causal_evidence_ids):
        result["causal_attribution"] = "EVIDENCE_PRESENT_REQUIRES_DERIVATION"
    if specific_feature and tuple(feature_loss_evidence_ids):
        result["specific_feature_loss"] = "EVIDENCE_PRESENT_REQUIRES_DERIVATION"

    # General evidence of vandalism never automatically proves loss of a named feature.
    if specific_feature and not tuple(feature_loss_evidence_ids):
        result["specific_feature_loss"] = "UNSUPPORTED_SPECIFIC_ATTRIBUTION"

    if morphology_explained is False:
        result["damage_model_status"] = "INCOMPLETE_MODEL"
    elif morphology_explained is True:
        result["damage_model_status"] = "MORPHOLOGY_ACCOUNTED_FOR_NOT_CAUSATION_PROOF"
    else:
        result["damage_model_status"] = "NOT_TESTED"

    return result
