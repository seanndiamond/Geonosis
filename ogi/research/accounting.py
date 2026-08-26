from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class AccountingNode:
    node_id: str
    category: str
    premise_dependent: bool
    backward_historical_authority: bool = False
    demonstrated_damage: bool = False
    exposed_pending_feature_test: bool = False
    independently_surviving_result: bool = False
    mechanism_corrected: bool = False
    documented_cost_eur: float | None = None
    attributable_cost_eur: float | None = None


def summarize_accounting(nodes: Iterable[AccountingNode]) -> dict:
    rows = tuple(nodes)
    categories = Counter(row.category for row in rows)
    documented_cost = sum(row.documented_cost_eur or 0.0 for row in rows)
    attributable = [row.attributable_cost_eur for row in rows if row.attributable_cost_eur is not None]
    return {
        "verified_node_count": len(rows),
        "premise_dependent_node_count": sum(row.premise_dependent for row in rows),
        "demonstrated_damage_node_count": sum(row.demonstrated_damage for row in rows),
        "exposed_pending_feature_test_count": sum(row.exposed_pending_feature_test for row in rows),
        "backward_historical_authority_count": sum(row.backward_historical_authority for row in rows),
        "independently_surviving_result_count": sum(row.independently_surviving_result for row in rows),
        "mechanism_correction_count": sum(row.mechanism_corrected for row in rows),
        "categories": dict(categories),
        "documented_context_budget_eur": documented_cost,
        "attributable_cost_eur": sum(attributable) if attributable else None,
        "cost_warning": (
            "A programme-level budget is context only unless a source attributes a share to the tested work. "
            "Unknown attribution must remain unknown."
        ),
    }
