# Sample incident report

> Fictional scenario generated from the committed synthetic alert and application log fixtures.

## Summary

On 24 November 2026 at 10:00 UTC, a synthetic monitoring alert reported an elevated 5xx rate for the payment API. Correlated sample logs show database connection-pool acquisition timeouts and an exhausted-pool message.

## Evidence

| Evidence | Observation |
|---|---|
| ALERT-DEMO-2026-1124-001 | Payment API 5xx rate high |
| req-demo-1002 | Database pool acquisition timed out |
| req-demo-1003 | Database pool exhausted; HTTP 503 |
| req-demo-1006 | Another pool acquisition timeout |
| req-demo-1004 | Webhook processing delayed while dependency health degraded |

## Working hypothesis

**Probable pattern:** database connection-pool exhaustion.

This is not a confirmed root cause. A support engineer should verify database session count, connection limits, configured pool size, recent deployment changes and traffic shape.

## Recovery verification checklist

- [ ] Alert returned to normal.
- [ ] Payment API 5xx rate returned to baseline.
- [ ] Database pool acquisition latency returned to baseline.
- [ ] Delayed webhook queue drained without duplicate processing.
- [ ] Affected payment records were reconciled.
- [ ] Service owner documented confirmed root cause and follow-up actions.

No remediation was executed by the simulator.
