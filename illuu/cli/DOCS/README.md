# DOCS

## Purpose
The CLI module is intended to provide operator and admin tooling for illuu.

## Scope

### In Scope
- Operator CLI commands (not implemented in this module).
- Admin workflows for governance and tenants (not implemented in this module).

### Out of Scope
- API endpoints (owned by `api/`).
- Governance enforcement (owned by `governance/`).

## Architecture
No runtime implementation exists in this module. The CLI functionality currently lives in `vault/cli/` for the PrivateVault subsystem.

## Interfaces
- No public interfaces implemented in this module.

## Security & Compliance
- Not implemented here. Any CLI must use authenticated control-plane APIs.

## Testing Strategy
- No tests exist for this module.

## Failure Modes
- Not applicable: no runtime implementation.

## Observability
- Not implemented.

## Operational Runbook
- Not applicable: no runtime implementation.

## Ownership
- Owning team: Platform Operations.
- Review process: security review required for CLI authentication and scopes.
- Escalation path: Platform SRE.
- SLA expectations: N/A until implementation.

## Roadmap
- Implement a unified CLI backed by `api/`.
