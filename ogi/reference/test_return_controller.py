import unittest

from return_controller import Decision, SafeExit, evaluate_return_state


def base_record():
    return {
        "record_id": "example",
        "task_id": "T",
        "declared_objective": "Complete the task legitimately.",
        "operative_proxy": "External score.",
        "orientation_state": "ON_PATH",
        "objective_state": "CLEAR",
        "proxy_state": "ALIGNED",
        "permission_state": "AUTHORIZED",
        "authority_state": "CLEAR",
        "safe_exit_state": "AVAILABLE",
        "return_status": "NOT_REQUIRED",
        "allowed_safe_exits": [
            "UNRESOLVED",
            "IMPOSSIBLE_UNDER_CONSTRAINTS",
            "PERMISSION_REQUIRED",
            "AUTHORITY_CONFLICT",
            "HUMAN_REVIEW_REQUIRED"
        ],
        "divergence_events": [],
        "correction_events": []
    }


class ReturnControllerTests(unittest.TestCase):
    def test_authorizes_clear_field(self):
        decision = evaluate_return_state(base_record())
        self.assertEqual(decision.decision, Decision.AUTHORIZE)
        self.assertIsNone(decision.safe_exit)

    def test_proxy_capture_routes_to_review(self):
        record = base_record()
        record["proxy_state"] = "CONFLICTING"
        record["divergence_events"] = [
            {"event_id": "D1", "rf_code": "RF-02_PROXY_CAPTURE"}
        ]
        decision = evaluate_return_state(record)
        self.assertEqual(decision.decision, Decision.SAFE_EXIT)
        self.assertEqual(decision.safe_exit, SafeExit.HUMAN_REVIEW_REQUIRED)

    def test_impossible_task_exits_safely(self):
        record = base_record()
        record["divergence_events"] = [
            {"event_id": "D2", "rf_code": "RF-07_IMPOSSIBLE_TASK_ESCALATION"}
        ]
        decision = evaluate_return_state(record)
        self.assertEqual(decision.decision, Decision.SAFE_EXIT)
        self.assertEqual(decision.safe_exit, SafeExit.IMPOSSIBLE_UNDER_CONSTRAINTS)

    def test_state_regression_recovers_without_reopen(self):
        record = base_record()
        record["divergence_events"] = [
            {"event_id": "D3", "rf_code": "RF-03_STATE_REGRESSION"}
        ]
        record["correction_events"] = [
            {
                "event_id": "C1",
                "correction": "Return to current state.",
                "reopen_trigger_present": False
            }
        ]
        decision = evaluate_return_state(record)
        self.assertEqual(decision.decision, Decision.REEVALUATE)

    def test_new_evidence_reopens_instead_of_blind_return(self):
        record = base_record()
        record["divergence_events"] = [
            {"event_id": "D4", "rf_code": "RF-03_STATE_REGRESSION"}
        ]
        record["correction_events"] = [
            {
                "event_id": "C2",
                "correction": "New contradictory exhibit entered.",
                "reopen_trigger_present": True
            }
        ]
        decision = evaluate_return_state(record)
        self.assertEqual(decision.decision, Decision.REOPEN_AND_REEVALUATE)

    def test_false_return_requires_state_verification(self):
        record = base_record()
        record["return_status"] = "FALSE_RETURN_SUSPECTED"
        decision = evaluate_return_state(record)
        self.assertEqual(decision.decision, Decision.REEVALUATE)

    def test_conflicting_authority_stops_action(self):
        record = base_record()
        record["authority_state"] = "CONFLICTING"
        decision = evaluate_return_state(record)
        self.assertEqual(decision.decision, Decision.SAFE_EXIT)
        self.assertEqual(decision.safe_exit, SafeExit.AUTHORITY_CONFLICT)


if __name__ == "__main__":
    unittest.main()
