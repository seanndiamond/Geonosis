from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Mapping


ESTABLISHED = "ESTABLISHED"
OPEN = "OPEN"
BLOCKED_BY_PREREQUISITE = "BLOCKED_BY_PREREQUISITE"
CONDITIONALLY_IRRELEVANT = "CONDITIONALLY_IRRELEVANT_TO_HISTORICAL_MECHANISM"


@dataclass(frozen=True)
class MechanismNode:
    claim_id: str
    status: str
    required_prerequisites: tuple[str, ...] = ()
    independent_route: bool = False


@dataclass(frozen=True)
class MechanismVerdict:
    claim_id: str
    status: str
    earliest_failed_prerequisite: str | None
    failed_prerequisites: tuple[str, ...]
    reason: str


def evaluate_prerequisite_graph(nodes: Iterable[MechanismNode]) -> Mapping[str, MechanismVerdict]:
    """Evaluate a causal/engineering interpretation without letting distal evidence
    repair missing upstream prerequisites.

    Nodes should be supplied in approximately causal order. A node marked
    ESTABLISHED may still be blocked as a historical mechanism when a material
    prerequisite is OPEN or otherwise unestablished. Independent routes must be
    represented explicitly rather than assumed.
    """
    node_map = {node.claim_id: node for node in nodes}
    verdicts: dict[str, MechanismVerdict] = {}

    for node in nodes:
        failed: list[str] = []
        for prerequisite_id in node.required_prerequisites:
            prerequisite = node_map.get(prerequisite_id)
            if prerequisite is None:
                failed.append(prerequisite_id)
                continue
            prior_verdict = verdicts.get(prerequisite_id)
            effective_status = prior_verdict.status if prior_verdict else prerequisite.status
            if effective_status != ESTABLISHED:
                failed.append(prerequisite_id)

        if failed and not node.independent_route:
            verdicts[node.claim_id] = MechanismVerdict(
                claim_id=node.claim_id,
                status=CONDITIONALLY_IRRELEVANT if node.status == ESTABLISHED else BLOCKED_BY_PREREQUISITE,
                earliest_failed_prerequisite=failed[0],
                failed_prerequisites=tuple(failed),
                reason=(
                    f"{node.claim_id} cannot function as an established historical mechanism "
                    f"because prerequisite {failed[0]} is unestablished."
                ),
            )
        elif node.status == ESTABLISHED:
            verdicts[node.claim_id] = MechanismVerdict(
                claim_id=node.claim_id,
                status=ESTABLISHED,
                earliest_failed_prerequisite=None,
                failed_prerequisites=(),
                reason="Node and its tested prerequisites are established at this scope.",
            )
        else:
            verdicts[node.claim_id] = MechanismVerdict(
                claim_id=node.claim_id,
                status=OPEN,
                earliest_failed_prerequisite=None,
                failed_prerequisites=(),
                reason="Node remains open on its own evidence.",
            )

    return verdicts


def earliest_uncertain_prerequisite(nodes: Iterable[MechanismNode]) -> str | None:
    """Return the earliest node that is not established, for research prioritisation."""
    for node in nodes:
        if node.status != ESTABLISHED:
            return node.claim_id
    return None
