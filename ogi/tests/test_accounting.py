from research.accounting import AccountingNode, summarize_accounting


def test_accounting_separates_damage_from_exposure_and_cost_context():
    nodes = [
        AccountingNode(
            node_id="demonstrated",
            category="research",
            premise_dependent=True,
            demonstrated_damage=True,
        ),
        AccountingNode(
            node_id="exposed",
            category="education",
            premise_dependent=True,
            backward_historical_authority=True,
            exposed_pending_feature_test=True,
        ),
        AccountingNode(
            node_id="programme_context",
            category="funding_context",
            premise_dependent=False,
            documented_cost_eur=2_700_000,
            attributable_cost_eur=None,
        ),
    ]
    summary = summarize_accounting(nodes)
    assert summary["demonstrated_damage_node_count"] == 1
    assert summary["exposed_pending_feature_test_count"] == 1
    assert summary["backward_historical_authority_count"] == 1
    assert summary["documented_context_budget_eur"] == 2_700_000
    assert summary["attributable_cost_eur"] is None
