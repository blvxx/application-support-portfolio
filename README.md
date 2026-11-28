# Application & Production Support — Engineering Evidence

> **Portfolio navigation:** the concise employer-facing introduction now lives in the [single career portfolio](https://blvxx.github.io/portfolio/). This repository is the supporting technical evidence library: source code, labs, runbooks, synthetic incidents and CI checks. It is not a separate employer portfolio.


**Application Support L2 · Support Engineering · Linux · SQL · Incident Investigation**

I troubleshoot application and infrastructure issues using logs, SQL, API checks, service diagnostics and structured incident investigation. My approach combines impact assessment, evidence collection, safe recovery, clear escalation and post-fix verification.

**Target roles:** Application Support Engineer L2 · Production Support Engineer · Technical Support Engineer · Support Engineer

[GitHub profile](https://github.com/blvxx) · [Email](mailto:blvx8x@gmail.com) · [Telegram](https://t.me/blvlxx)

## Core support capabilities

- **Linux:** systemd, journalctl, process/service diagnostics, permissions and networking.
- **Logs and troubleshooting:** filtering, timeline reconstruction, correlation IDs and evidence capture.
- **SQL and data diagnostics:** PostgreSQL queries, joins, aggregation, reconciliation and consistency checks.
- **Web and infrastructure:** HTTP, REST, DNS, TLS, TCP/IP, Nginx and application connectivity.
- **Monitoring:** Prometheus, Grafana, metrics, health checks and dependency visibility.
- **Incident process:** impact/severity assessment, reproduction, escalation, RCA, runbooks and recovery verification.
- **Automation:** Python scripts for log triage, reconciliation and repetitive diagnostics.

## Selected projects

The source projects, tests, runbooks and supporting documentation are included in this repository. The project folders preserve their original paths so their local run commands and relative documentation links continue to work.

### 1. Linux Support Engineering Lab

[Open project](./support-engineering-lab/)

A troubleshooting casebook with 10 documented scenarios covering service failures, disk/inode pressure, Nginx 502/504, DNS, TLS, OOM, PostgreSQL pool exhaustion, permissions and port conflicts.

Evidence includes:
- systemd and journalctl diagnostic playbooks.
- Python log triage CLI with severity-ranked findings and source-line evidence.
- Synthetic sample logs and unit tests.
- Incident report and handover templates.

### 2. Incident Investigation Lab

[Open project](./incident-lab/)

A simulated payment-webhook incident from first report through investigation, root-cause analysis and recovery.

Evidence includes:
- Incident timeline, logs and HTTP request/response examples.
- SQL reconciliation and duplicate detection.
- Python diagnostic utilities and test coverage.
- Recovery and reconciliation runbooks.

### 3. Fintech Support & QA Lab

[Open project](./fintech-support-qa-lab/)

A local FastAPI payment/webhook sandbox built to demonstrate application support and integration troubleshooting.

Evidence includes:
- Health/readiness checks and PostgreSQL integration.
- HMAC webhook verification and idempotent event processing.
- SQL investigation playbook and Postman collection.
- Synthetic logs and a Python log-analysis CLI.
- Docker Compose and GitHub Actions checks.

### 4. Support Operations Analytics

[Open project](./support-operations-analytics/)

SQL analysis of a synthetic SaaS support dataset.

Topics:
- Ticket volume and category trends.
- First-response and resolution SLA.
- Backlog age and workload distribution.
- Data-quality checks and metric caveats.

### 5. SQL + Python Data Analytics

[Open project](./data-analytics/)

A PostgreSQL/Python data workflow with validation, KPI calculations, tests and CSV/JSON reporting. The dataset is synthetic.

### 6. Delivery and UAT Simulation

[Open documentation](./docs/delivery-simulation/)

A fictional support-operations automation delivery package with product brief, prioritised backlog, change request, review record, UAT handover and incident retrospective. All stakeholders and approvals are simulated, not real client work.

### 7. FinTech Service Diagnostics

[Open project](https://github.com/blvxx/qa-engineering-labs/tree/main/fintech-qa-platform)

A complementary payment/ledger sandbox with service health checks, PostgreSQL, Docker Compose, metrics and controlled dependency-outage/recovery testing.

[CI workflow](https://github.com/blvxx/qa-engineering-labs/actions/workflows/fintech-qa-platform.yml)

### 8. Production Incident Simulator — Alert to RCA

[Open project](./production-incident-simulator/)

A deterministic lab that correlates a synthetic monitoring alert with JSON Lines application logs, identifies a probable failure pattern, creates an evidence-backed timeline and proposes read-only investigation checks.

Evidence includes:
- Alert and log correlation by service and timestamp.
- Severity summary, matched request IDs and probable-cause hypothesis.
- Incident triage runbook and sample RCA report.
- Python unit tests and GitHub Actions validation.

[Successful CI workflow](https://github.com/blvxx/application-support-labs/actions/workflows/production-incident-simulator.yml)

### 9. Games Support Casebook

[Open casebook](./games-support-casebook/)

A simulated player-support casebook covering purchase issues, account security, login problems, connectivity, moderation and escalation.

Evidence includes:
- Player-facing first responses and safe evidence collection.
- Account-security boundaries and escalation rules.
- Internal ticket notes and concise handover examples.
- Prioritisation and communication guidance.

All players, products, tickets and incidents are fictional practice scenarios, not real customer support records.

## Incident-handling workflow

1. Confirm the symptom, time window, affected users and business impact.
2. Check service health, recent changes, logs and dependencies.
3. Reproduce the issue where safe and collect relevant evidence.
4. Use SQL and API checks to validate application state.
5. Assign severity, identify the next responsible team and communicate status.
6. Verify recovery and data consistency.
7. Document root cause, corrective action and preventive follow-up.

## Example operational checks

| Area | Example investigation |
|---|---|
| Application unavailable | Process/service status, recent deployment, logs, port binding and dependency health |
| Slow or failed API | HTTP status, latency, request ID, upstream response and timeout behavior |
| Data mismatch | SQL reconciliation, duplicate/missing records and timestamp boundaries |
| Queue or webhook issue | Delivery attempts, retry behavior, idempotency and downstream availability |
| Elevated errors | Metric trend, log correlation, affected endpoint and time-to-recovery |

These are troubleshooting patterns and lab exercises. They do not imply access to a particular employer's production environment.

## Business value

Reliable application support reduces time spent on repeated investigation, makes incidents easier to reproduce and improves communication between support, engineering and operations.

The [AI Support Triage Agent](https://github.com/blvxx/python-backend-projects/tree/main/ai-support-triage-agent) implements a retrieval-grounded support-triage prototype with evidence validation and mandatory human review. The [QA & Commercial Problem-Solving Casebook](https://github.com/blvxx/qa-engineering-labs/blob/main/qa-commercial-casebook.md) describes the concept, boundaries and proposed pilot metrics.

No production SLA improvement or customer savings are claimed without operational measurements.

## Scope and transparency

This portfolio contains independent practice projects, synthetic incident data and fictional delivery scenarios. They are not presented as real customer incidents, paid client deployments or employer production records. CI evidence proves only the checks included in each workflow.

---

**Artem Kalinin** · [GitHub](https://github.com/blvxx)
