# DOCS

## Purpose
The vault module provides secure storage, audit evidence management, quorum-based approvals, and a control-plane API for tenant governance workflows.

## Scope

### In Scope
- Control-plane API in `vault/services/api/`.
- Quorum validation in `vault/quorum.py`.
- Evidence export in `vault/evidence_export.py`.
- Ledger adapters in `vault/ledgers/`.
- CLI tooling in `vault/cli/`.
- Database migrations in `vault/migrations/`.

### Out of Scope
- Governance proxy enforcement (owned by `governance/`).
- Unified external API (owned by `api/`).
- Workflow orchestration (owned by `workflows/`).

## Architecture
The control plane is implemented as a FastAPI application (`vault/services/api/app.py`) and mounted under `/api/v1`. It includes authentication middleware based on bearer tokens and tenant scoping. Quorum approval validation uses environment-configured rules and signed approvals. Evidence export compiles audit logs into bundles.

Text diagram:

```
Client
  -> /api/v1 (vault/services/api/app.py)
    -> auth middleware (PV_SERVICE_TOKENS)
    -> routes: status, auth, tenants, quorum, audit, approvals, evidence
      -> quorum.py validates approvals
      -> audit_logger reads audit logs
      -> evidence_export bundles audit evidence
```

## Interfaces

### HTTP API (vault/services/api)
- `GET /api/v1/status` returns `{status, version}`.
- `GET /api/v1/health` returns `{status}`.
- `GET /api/v1/auth/me` returns token/scopes.
- `POST /api/v1/tenants` create tenant.
- `GET /api/v1/tenants` list tenants.
- `GET /api/v1/tenants/{tenant_id}` get tenant.
- `PATCH /api/v1/tenants/{tenant_id}` update tenant.
- `DELETE /api/v1/tenants/{tenant_id}` delete tenant.
- `GET /api/v1/quorum/rules` get quorum rules.
- `PUT /api/v1/quorum/rules` update quorum rules.
- `POST /api/v1/quorum/validate` validate approvals.
- `GET /api/v1/audit` list audit events.
- `GET /api/v1/approvals` list approvals.
- `POST /api/v1/evidence/export` export evidence bundle.

### Environment Configuration
- `PV_SERVICE_TOKENS`: JSON list of tokens and scopes for auth.
- `PV_CONTEXT_KEYS`: JSON map of key IDs to secrets for approval signatures.
- `PV_QUORUM_MIN`, `PV_QUORUM_RULES`, `PV_QUORUM_RULES_V2`, `PV_QUORUM_RULES_FILE`: quorum rules.
- `PV_AUDIT_LOG_PATH`: audit log location.
- `PV_EXPORT_ROOT`: evidence export destination.

### Internal Modules
- `vault/quorum.py`: quorum validation, signature verification, rule resolution.
- `vault/security_context.py`: request signing and context validation (shim to governance implementation).
- `vault/audit_logger.py`, `vault/policy_engine.py`, `vault/approval_store.py`: compatibility shims into governance.
- `vault/ledgers/*`: ledger adapters (cosmos, qldb, ethereum, fabric).

### Connectors
- `vault/connectors/__init__.py` is a shim to `integrations/adapters/vault_connectors`.

## Security & Compliance
- Authentication is enforced via bearer tokens (`PV_SERVICE_TOKENS`).
- Tenant scoping is enforced in API routes (e.g., `TENANT_SCOPE_VIOLATION`).
- Quorum approvals use HMAC signatures derived from context keys.
- Audit data is read from audit log paths and exported as evidence bundles.
- Evidence bundles include manifest hashes and verification results.

## Testing Strategy
- Tests in `vault/tests/` cover API, quorum, evidence export, and control-plane security.
- `vault/pytest.ini` configures test execution for this module.

## Failure Modes
- Missing or invalid `PV_SERVICE_TOKENS` causes authentication failures.
- Missing audit log paths result in empty audit responses.
- Quorum rule parsing errors raise `QUORUM_RULES_INVALID`.
- Evidence export fails if export root is unavailable.

## Observability
- Audit logs are read from JSONL files indicated by `PV_AUDIT_LOG_PATH`.
- No structured metrics export is implemented in code.

## Operational Runbook
- Deployment: run `vault/services/api/app.py` (FastAPI).
- Rollback: redeploy previous container or artifact.
- Upgrades: keep database migrations in `vault/migrations/` in sync.
- Incident response: preserve audit logs and evidence bundles.

## Ownership
- Owning team: Vault Platform.
- Review process: security review for auth/quorum changes.
- Escalation path: Vault On‑Call -> Platform SRE -> Compliance.
- SLA expectations: Tier‑1 for audit export and quorum validation.

## Roadmap
- Integrate vault APIs into unified `api/` gateway.
- Replace file-based audit log access with ledger-backed evidence store.
- Add structured metrics and traces.
