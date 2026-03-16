# DOCS

## Purpose
The governance module (Choubis) enforces outbound AI traffic control, policy evaluation, and audit logging. It provides the sovereign proxy that sits between agents and external LLM/tool providers, ensuring requests are inspected, redacted, and gated before execution.

## Scope

### In Scope
- Reverse-proxy enforcement via `governance/main.go` and `governance/internal/shield/*`.
- Policy loading and evaluation via `governance/internal/policy/engine.go` and YAML policy bundles under `governance/policies/`.
- Audit event logging to JSONL in `governance/logs/` via `governance/internal/shield/audit.go`.
- Safety scoring and kill-switch checks via `governance/pkg/vault/enforcer.go`.
- Admin HTTP handler endpoints in `governance/internal/admin/server.go`.
- Interface contracts for policy, risk, approval, audit, and gateway under `governance/contracts/`.

### Out of Scope
- Business logic execution for workflows or agents.
- Storage of long-term evidence and ledger data (owned by `vault/`).
- External billing or tenant provisioning (owned by `vault/` and `api/`).
- Direct SDKs for external customers.

## Architecture
The proxy process in `governance/main.go` starts a reverse proxy on port `:9000` and routes all inbound HTTP requests through the shield engine. The shield modifies request bodies, applies simple risk scoring, and can trigger a kill-switch by rewriting the request path. Policy evaluation is handled by YAML policy bundles loaded by tenant. Audit logs are appended as JSONL to `governance/logs/<tenant>.jsonl`.

Text diagram:

```
Inbound AI Request
  -> governance/main.go (HTTP server :9000)
    -> internal/shield (reverse proxy + request redaction)
      -> pkg/vault/enforcer (safety scoring)
      -> internal/policy (YAML policy evaluation)
      -> internal/shield/audit (JSONL logging)
```

## Interfaces

### Public HTTP Interfaces
- Reverse proxy listener on `:9000` (all paths) in `governance/main.go`.
- Admin handler endpoints in `governance/internal/admin/server.go`:
  - `POST /reload` reloads `policies/rules.yaml`.
  - `GET /audit` serves audit logs.
  - `GET /stats` serves stats.
  - `GET /tenants` serves tenant list.
  - `GET /usage` serves usage.

### Internal Contracts
- `governance/contracts/policy.py`: `PolicyEngine.evaluate()`
- `governance/contracts/risk.py`: `RiskEngine.score()`
- `governance/contracts/approval.py`: `ApprovalGateway.requires_approval()` / `request_approval()` / `resolve()`
- `governance/contracts/audit.py`: `AuditLogger.record()`
- `governance/contracts/gateway.py`: `GovernanceGateway.authorize()` / `proxy_call()`

### Policies
- YAML bundles in `governance/policies/*.yaml` loaded by `governance/internal/policy/engine.go`.

## Security & Compliance
- Access control is enforced at the proxy boundary; requests are intercepted before reaching external providers.
- Safety scoring uses `pkg/vault/enforcer.go` with a configurable minimum safety score and a kill-switch on risk keywords.
- Audit logs are written to append-only JSONL files under `governance/logs/`.
- Policy evaluation is deterministic based on YAML bundles.
- This module is a key enforcement layer for SOC2 Security and ISO 27001 access control controls; evidence is emitted via audit logs.
- Admin HTTP endpoints in `governance/internal/admin/server.go` do not show authentication in code; operational deployments must restrict access at the network or reverse-proxy layer.

## Testing Strategy
- Go unit tests are not present in this module.
- Python contracts are interface-only and not exercised directly.
- Integration tests should cover:
  - Proxy routing to a known upstream.
  - Policy load and evaluation for tenant policies.
  - Audit log append behavior.
  - Kill-switch behavior on risk keywords.

## Failure Modes
- Policy bundle missing or invalid: policy defaults to allow in `Evaluate` when cache is empty.
- Audit log file cannot be written: `LogEvent` returns without raising and audit evidence is lost.
- Proxy upstream unreachable: requests fail at reverse proxy layer.
- Kill-switch false positives/negatives due to simple keyword scoring.

## Observability
- Audit events are logged in JSONL to `governance/logs/<tenant>.jsonl`.
- Proxy logs use standard Go logging to stdout in `governance/main.go`.
- No structured tracing instrumentation is present in this module.

## Operational Runbook
- Deployment: run `governance/main.go` (or container) to start proxy on `:9000`.
- Rollback: redeploy previous container or binary.
- Upgrades: require reloading YAML policies via `/reload` if policy bundles change.
- Incident response: preserve `governance/logs/` and reverse proxy logs for audit review.

## Ownership
- Owning team: Governance Engineering.
- Review process: policy changes require security review and approval.
- Escalation path: Security On‑Call -> Platform SRE -> Compliance.
- SLA expectations: proxy availability is Tier‑1; audit log durability is mandatory.

## Roadmap
- Replace keyword safety scoring with policy-driven risk engine.
- Add authenticated admin endpoints.
- Add structured tracing and metrics export.
