from __future__ import annotations

import argparse
import json
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any


def parse_timestamp(value: str) -> datetime:
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError(f"Timestamp must include timezone: {value}")
    return parsed.astimezone(timezone.utc)


def load_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"Expected JSON object in {path}")
    return value


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            try:
                item = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSON on line {line_number}: {exc}") from exc
            if not isinstance(item, dict):
                raise ValueError(f"Expected JSON object on line {line_number}")
            rows.append(item)
    return rows


def correlate_logs(
    alert: dict[str, Any],
    logs: list[dict[str, Any]],
    window_minutes: int = 10,
) -> list[dict[str, Any]]:
    alert_time = parse_timestamp(str(alert["starts_at"]))
    earliest = alert_time - timedelta(minutes=window_minutes)
    latest = alert_time + timedelta(minutes=window_minutes)
    service = str(alert["service"])
    matched = []
    for item in logs:
        if item.get("service") != service:
            continue
        timestamp = parse_timestamp(str(item["timestamp"]))
        if earliest <= timestamp <= latest:
            matched.append({**item, "_parsed_timestamp": timestamp})
    return sorted(matched, key=lambda row: row["_parsed_timestamp"])


def classify_pattern(evidence: list[dict[str, Any]]) -> tuple[str, list[str], list[str]]:
    messages = [str(row.get("message", "")).casefold() for row in evidence]
    pool_matches = [
        row for row in evidence
        if "connection pool" in str(row.get("message", "")).casefold()
        and any(term in str(row.get("message", "")).casefold()
                for term in ("timed out", "exhausted"))
    ]
    upstream_matches = [
        row for row in evidence
        if "connection refused" in str(row.get("message", "")).casefold()
        or "upstream unavailable" in str(row.get("message", "")).casefold()
    ]
    duplicate_matches = [
        row for row in evidence
        if "duplicate event" in str(row.get("message", "")).casefold()
        or "idempotency conflict" in str(row.get("message", "")).casefold()
    ]

    if pool_matches:
        return (
            "Probable database connection-pool exhaustion",
            [str(row.get("request_id", "unknown")) for row in pool_matches],
            [
                "Check database active sessions and connection limits using read-only queries.",
                "Compare application pool settings with database capacity.",
                "Review recent deployments and traffic changes in the alert window.",
                "Escalate to the service owner and DBA before any configuration change.",
            ],
        )
    if upstream_matches:
        return (
            "Probable upstream dependency connectivity failure",
            [str(row.get("request_id", "unknown")) for row in upstream_matches],
            [
                "Check dependency health and DNS/TCP/TLS connectivity.",
                "Compare upstream error rates and latency in the same time window.",
                "Review recent deployment or network changes with the owning team.",
            ],
        )
    if duplicate_matches:
        return (
            "Possible duplicate-event or idempotency conflict",
            [str(row.get("request_id", "unknown")) for row in duplicate_matches],
            [
                "Inspect delivery attempts and event identifiers.",
                "Compare idempotency-key handling and persisted event state.",
                "Reconcile source and target event counts before proposing replay.",
            ],
        )
    if not messages:
        return (
            "Insufficient correlated log evidence",
            [],
            [
                "Expand the time window only after confirming the alert timestamp.",
                "Check service, request ID and trace correlation fields.",
                "Escalate with the alert payload and available evidence.",
            ],
        )
    return (
        "No known failure pattern identified",
        [],
        [
            "Review related services and dependency metrics.",
            "Search logs using the alert time window and available correlation IDs.",
            "Escalate to the service owner with the evidence collected.",
        ],
    )


def build_report(
    alert: dict[str, Any],
    logs: list[dict[str, Any]],
    window_minutes: int = 10,
) -> dict[str, Any]:
    evidence = correlate_logs(alert, logs, window_minutes)
    probable_cause, matched_ids, next_checks = classify_pattern(evidence)
    counts = Counter(str(row.get("level", "UNKNOWN")).upper() for row in evidence)
    timeline = [
        {
            "timestamp": row["_parsed_timestamp"].isoformat().replace("+00:00", "Z"),
            "level": str(row.get("level", "UNKNOWN")).upper(),
            "request_id": row.get("request_id"),
            "message": row.get("message", ""),
        }
        for row in evidence
    ]
    return {
        "incident_id": alert.get("alert_id", "unknown"),
        "alert_name": alert.get("alert_name", "unknown"),
        "service": alert.get("service", "unknown"),
        "environment": alert.get("environment", "unknown"),
        "severity": str(alert.get("severity", "unknown")).lower(),
        "started_at": parse_timestamp(str(alert["starts_at"])).isoformat().replace("+00:00", "Z"),
        "summary": alert.get("summary", ""),
        "correlation_window_minutes": window_minutes,
        "correlated_log_count": len(evidence),
        "log_level_counts": dict(sorted(counts.items())),
        "probable_cause": probable_cause,
        "matched_request_ids": sorted(set(matched_ids)),
        "timeline": timeline,
        "next_read_only_checks": next_checks,
        "confidence_note": (
            "Pattern match only. Confirm the cause using service metrics, database state, "
            "deployment history and the owning team's investigation."
        ),
        "automation_boundary": "No remediation or configuration changes were executed.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Build an evidence-backed synthetic incident triage report.")
    parser.add_argument("--alert", type=Path, required=True)
    parser.add_argument("--logs", type=Path, required=True)
    parser.add_argument("--window-minutes", type=int, default=10)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.window_minutes < 0:
        parser.error("--window-minutes must be non-negative")

    report = build_report(load_json(args.alert), load_jsonl(args.logs), args.window_minutes)
    rendered = json.dumps(report, ensure_ascii=False, indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + "\n", encoding="utf-8")
    else:
        print(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
