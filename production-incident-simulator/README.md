# Production Incident Simulator — Alert to RCA

> Independent support-engineering portfolio lab. All alerts and logs are synthetic. This is not a real production incident or a claim of operating a customer's production environment.

A small, reproducible incident-triage exercise that turns a monitoring alert and structured application logs into an evidence-backed first-response report.

## What it demonstrates

- Reading a structured alert payload.
- Parsing JSON Lines application logs.
- Correlating log evidence by service and time window.
- Identifying a probable failure pattern without asserting an unproven root cause.
- Producing an incident timeline and severity summary.
- Suggesting read-only diagnostic checks and escalation ownership.
- Keeping remediation actions outside the automated triage script.

## Scenario

A synthetic monitoring alert reports an elevated 5xx rate for a payment API. The log evidence contains database connection-pool acquisition timeouts during the same time window. The simulator identifies this as a probable connection-pool exhaustion pattern and returns supporting log records.

The report intentionally says **probable cause**, not confirmed root cause. Confirmation requires checking database activity, pool configuration, recent deployment changes and service metrics.

## Run locally

Requirements: Python 3.10+; standard library only.

~~~bash
python src/incident_simulator.py \
  --alert data/alert.json \
  --logs data/application.jsonl \
  --window-minutes 10 \
  --output output/incident-report.json
~~~

Or print the report to stdout:

~~~bash
python src/incident_simulator.py --alert data/alert.json --logs data/application.jsonl
~~~

Run tests:

~~~bash
python -m unittest discover -s tests -v
~~~

## Report contents

- Alert metadata and service.
- Correlated evidence count.
- Ordered timeline.
- Probable failure pattern and matching evidence.
- Read-only next checks.
- Explicit uncertainty and escalation guidance.

## Safety boundary

The tool does not restart services, change pool sizes, delete data, requeue messages or modify configuration. Recommendations are read-only checks for a human support engineer. Any remediation must follow the owning team's change and approval process.

## Project limitations

- The dataset has one synthetic alert and a small sample log file.
- Correlation is based on service name and timestamp, not distributed trace spans.
- Pattern matching is deterministic and does not prove causality.
- No live Prometheus, Grafana, ELK or ticketing integration is connected.
- The report is a first-response aid, not an automated root-cause determination.

## Evidence

- [Incident triage runbook](docs/triage-runbook.md)
- [Sample incident report](docs/sample-incident-report.md)
- [CI workflow](../.github/workflows/production-incident-simulator.yml)

