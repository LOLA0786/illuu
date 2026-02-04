# Evidence Generation Plan

## Principles
- Evidence is generated automatically via system telemetry and CI/CD artifacts.
- No manual evidence collection.
- All evidence is immutable and traceable to a control ID.

## Evidence Sources
- CI/CD: build logs, test results, approvals
- IAM: access review exports, role assignment logs
- Vault ledger: audit trail for governed actions
- Observability: uptime, latency, error rates
- Change management: PR approvals, release tags
- Backup/DR: restore run logs

## Evidence Pipeline
1. Emit control-tagged events to the audit ledger.
2. Export ledger snapshots into immutable evidence bundles.
3. Store bundles in WORM-backed storage.
4. Provide read-only audit portal to external auditors.

## Retention
- Evidence retained for 7 years (configurable per tenant).
- Rotation and purge enforced by policy.
