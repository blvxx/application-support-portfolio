# Alert-to-RCA triage runbook

> Synthetic exercise only. Follow the employer's approved incident procedure in a real environment.

## 1. Acknowledge and scope

- Record alert ID, service, environment, severity, start time and alert rule.
- Confirm whether customer impact is known or only suspected.
- Check whether the alert is firing, recovering or flapping.
- Identify the service owner and incident communication channel.

## 2. Gather read-only evidence

- Inspect service health/readiness and recent error-rate/latency metrics.
- Filter logs by service and alert time window.
- Prefer request IDs, trace IDs and event IDs over broad text-only search.
- Compare dependency status and recent deployment/change history.
- Use read-only SQL to inspect connection count, queue state or data consistency where authorised.

## 3. Form a working hypothesis

A pattern match is not a confirmed root cause. Record:
- observed fact and evidence reference;
- hypothesis;
- alternative explanations;
- missing information;
- confidence and next verification step.

## 4. Escalate safely

Escalate when there is customer impact, risk to financial/data integrity, insufficient permissions or a need for a configuration/production change. State who owns the next action and when the next update is due.

## 5. Verify recovery

- Confirm alert state returns to normal.
- Verify error rate and latency against the agreed baseline.
- Check that retries or queues are draining without creating duplicates.
- Reconcile affected records if data integrity may have been impacted.
- Capture the recovery timestamp and remaining risk.

## 6. Close with an RCA

A useful retrospective separates trigger, contributing conditions, detection gap, response timeline, confirmed root cause, corrective action, prevention and owners. Do not label a hypothesis as a confirmed root cause without supporting evidence.
