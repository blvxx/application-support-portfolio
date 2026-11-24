import json
import tempfile
import unittest
from pathlib import Path

from src.incident_simulator import build_report, correlate_logs


ALERT = {
    "alert_id": "INC-1",
    "alert_name": "ApiErrorsHigh",
    "service": "payments",
    "environment": "test",
    "severity": "high",
    "starts_at": "2026-11-24T10:00:00Z",
    "summary": "5xx rate high",
}


class IncidentSimulatorTests(unittest.TestCase):
    def setUp(self):
        self.logs = [
            {
                "timestamp": "2026-11-24T09:59:00Z",
                "service": "payments",
                "level": "ERROR",
                "request_id": "req-1",
                "message": "Database connection pool exhausted",
            },
            {
                "timestamp": "2026-11-24T10:01:00Z",
                "service": "notifications",
                "level": "ERROR",
                "request_id": "req-2",
                "message": "Connection refused",
            },
        ]

    def test_correlates_only_same_service_and_time_window(self):
        evidence = correlate_logs(ALERT, self.logs, window_minutes=2)
        self.assertEqual(len(evidence), 1)
        self.assertEqual(evidence[0]["request_id"], "req-1")

    def test_classifies_database_pool_pattern_and_keeps_read_only_boundary(self):
        report = build_report(ALERT, self.logs, window_minutes=2)
        self.assertEqual(report["probable_cause"], "Probable database connection-pool exhaustion")
        self.assertIn("req-1", report["matched_request_ids"])
        self.assertIn("No remediation", report["automation_boundary"])

    def test_no_evidence_returns_safe_fallback(self):
        report = build_report(ALERT, [], window_minutes=2)
        self.assertEqual(report["correlated_log_count"], 0)
        self.assertEqual(report["probable_cause"], "Insufficient correlated log evidence")

    def test_invalid_timestamp_is_rejected(self):
        bad_alert = {**ALERT, "starts_at": "not-a-date"}
        with self.assertRaises(ValueError):
            build_report(bad_alert, self.logs)

    def test_jsonl_loader_rejects_malformed_line(self):
        from src.incident_simulator import load_jsonl
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bad.jsonl"
            path.write_text('{"ok": true}\nnot-json\n', encoding="utf-8")
            with self.assertRaises(ValueError):
                load_jsonl(path)


if __name__ == "__main__":
    unittest.main()
