from research.mechanism import (
    BLOCKED_BY_PREREQUISITE,
    CONDITIONALLY_IRRELEVANT,
    ESTABLISHED,
    OPEN,
    MechanismNode,
    earliest_uncertain_prerequisite,
    evaluate_prerequisite_graph,
)


def test_water_cannot_rescue_unproved_rope_traction():
    nodes = [
        MechanismNode("rope_traction", OPEN),
        MechanismNode("sled_motion", OPEN, ("rope_traction",)),
        MechanismNode("water_reduces_friction_lab", ESTABLISHED),
        MechanismNode(
            "historical_water_lubrication",
            ESTABLISHED,
            ("sled_motion", "water_reduces_friction_lab"),
        ),
    ]
    verdicts = evaluate_prerequisite_graph(nodes)
    assert verdicts["sled_motion"].status == BLOCKED_BY_PREREQUISITE
    assert verdicts["historical_water_lubrication"].status == CONDITIONALLY_IRRELEVANT
    assert verdicts["historical_water_lubrication"].earliest_failed_prerequisite == "sled_motion"


def test_earliest_uncertain_prerequisite_is_researched_first():
    nodes = [
        MechanismNode("rope_exists", ESTABLISHED),
        MechanismNode("rope_to_sled_attachment", OPEN, ("rope_exists",)),
        MechanismNode("worker_force_transmission", OPEN, ("rope_to_sled_attachment",)),
        MechanismNode("water_application", OPEN),
    ]
    assert earliest_uncertain_prerequisite(nodes) == "rope_to_sled_attachment"


def test_independent_physics_stays_established_while_history_is_blocked():
    nodes = [
        MechanismNode("historical_traction", OPEN),
        MechanismNode("wet_sand_friction_measurement", ESTABLISHED),
        MechanismNode(
            "historical_lubrication",
            OPEN,
            ("historical_traction", "wet_sand_friction_measurement"),
        ),
    ]
    verdicts = evaluate_prerequisite_graph(nodes)
    assert verdicts["wet_sand_friction_measurement"].status == ESTABLISHED
    assert verdicts["historical_lubrication"].status == BLOCKED_BY_PREREQUISITE
