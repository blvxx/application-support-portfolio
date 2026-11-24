# Artem Kalinin — Application & Production Support Portfolio

**Application Support L2 · Support Engineer · Production Support · Linux · SQL · Incident Management**

I work with technical troubleshooting, application diagnostics, logs, SQL, service health and structured incident investigation. My approach combines clear reproduction, evidence collection, impact assessment, escalation and post-fix verification.

**Target roles:** Application Support Engineer L2 · Production Support Engineer · Technical Support Engineer · Support Engineer

[GitHub profile](https://github.com/blvxx) · [Email](mailto:blvx8x@gmail.com) · [Telegram](https://t.me/blvlxx)

## Core support capabilities

- **Linux:** service diagnostics, systemd, journalctl, processes, permissions and basic networking.
- **Logs and troubleshooting:** log filtering, timeline reconstruction, error correlation and evidence capture.
- **SQL and data diagnostics:** PostgreSQL queries, filtering, joins, aggregation, reconciliation and consistency checks.
- **Web and infrastructure:** HTTP, REST, DNS, TLS, TCP/IP, Nginx and application connectivity.
- **Monitoring and observability:** Prometheus, Grafana, service metrics and health checks.
- **Incident process:** impact and severity assessment, reproduction, escalation, RCA, runbooks and recovery verification.
- **Automation:** Python scripts for repetitive checks, data analysis and diagnostic workflows.

## Selected projects

Project implementations are currently maintained in the original engineering repository. This repository is the dedicated Application Support entry point; links below open source material and supporting runbooks.

### 1. Linux Support Engineering Lab

[Open project](https://github.com/blvxx/portfolio/tree/main/support-engineering-lab)

A practical troubleshooting casebook with 10 documented playbooks.

Topics:
- Linux service and process investigation.
- systemd and journalctl diagnostics.
- Log triage and source-line evidence.
- Network, DNS, TLS and Nginx troubleshooting.
- Severity ranking, escalation notes and actionable runbooks.

### 2. Incident Investigation Lab

[Open project](https://github.com/blvxx/portfolio/tree/main/incident-lab)

A simulated payment-webhook incident investigation.

Topics:
- Incident timeline and symptom reconstruction.
- Log analysis and request correlation.
- SQL reconciliation of application records.
- Root-cause analysis and recovery steps.
- Post-recovery verification and prevention actions.

### 3. Support Operations Analytics

[Open project](https://github.com/blvxx/portfolio/tree/main/support-operations-analytics)

SQL-based analysis of support operations.

Topics:
- Ticket volume and category analysis.
- SLA performance and overdue cases.
- Backlog age and workload distribution.
- Operational reporting and improvement hypotheses.

### 4. SQL + Python Data Analytics

[Open project](https://github.com/blvxx/portfolio/tree/main/data-analytics)

A PostgreSQL/Python data workflow with validation and CSV/JSON reporting.

### 5. FinTech Service Diagnostics

[Open project](https://github.com/blvxx/portfolio/tree/main/fintech-qa-platform)

A local payment/ledger sandbox with service health checks, logs, metrics, PostgreSQL, Docker Compose and a controlled dependency-outage/recovery exercise.

[CI evidence](https://github.com/blvxx/portfolio/actions/runs/45100258032)

## Incident-handling workflow

1. Confirm the symptom, time window, affected users and business impact.
2. Check service health, recent changes, logs and dependencies.
3. Reproduce the issue where safe and collect relevant evidence.
4. Use SQL and API checks to validate application state.
5. Assign severity, identify the next responsible team and communicate status.
6. Verify the recovery and check for data consistency.
7. Document root cause, corrective action and preventive follow-up.

## Example operational checks

| Area | Example investigation |
|---|---|
| Application unavailable | Process/service status, recent deploy, logs, port binding and dependency health |
| Slow or failed API | HTTP status, latency, request ID, upstream response and timeout behavior |
| Data mismatch | SQL reconciliation, duplicate/missing records and timestamp boundaries |
| Queue or webhook issue | Delivery attempts, retry behavior, idempotency and downstream availability |
| Elevated errors | Metric trend, log correlation, affected endpoint and time-to-recovery |

These are troubleshooting patterns and lab exercises. They do not imply access to a particular employer's production environment.

## Business value

Reliable application support reduces time spent on repeated investigation, makes incidents easier to reproduce and improves communication between support, engineering and operations.

The related QA/Commercial Casebook includes a support-triage automation concept with human review and proposed measures such as triage time, escalation quality and repeat-contact rate: [open casebook](https://github.com/blvxx/portfolio/blob/main/qa-commercial-casebook.md).

No production SLA improvement or customer savings are claimed without operational measurements.

## Scope and transparency

This repository is a curated Application Support portfolio landing page. Source projects currently remain in the original repository and will be migrated after the destination layout and file history are verified. Incident data is simulated; all examples are independent practice materials, not real customer incidents or employer production records.

---

**Artem Kalinin** · [GitHub](https://github.com/blvxx)
