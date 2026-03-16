# DOCS

## Purpose
The integrations module provides a unified connector framework and registry for external systems, with a manifest-based discovery mechanism and compatibility shims for legacy adapters.

## Scope

### In Scope
- Connector interface in `integrations/base/connector.py`.
- Registry and discovery in `integrations/base/registry.py`.
- Lifecycle placeholder in `integrations/base/lifecycle.py`.
- Mock connector in `integrations/mocks/mock_connector.py`.
- Legacy adapters consolidated under `integrations/adapters/`.

### Out of Scope
- Direct calls to external vendors from core modules.
- Secret storage (expected to be provided by `vault/`).
- Governance enforcement (owned by `governance/`).

## Architecture
Connectors are registered via a local manifest (`integrations/registry/manifest.json`). The registry loads connector classes by module path and registers them in memory. Legacy adapters are hosted under `integrations/adapters/*` and exposed through shim packages.

Text diagram:

```
manifest.json
  -> base/registry.discover()
    -> import module + class
    -> register(name -> connector class)
```

## Interfaces

### Connector Contract
Defined in `integrations/base/connector.py`:
- `auth(context)`
- `connect(config)`
- `fetch(query)`
- `push(payload)`
- `sync(state)`
- `revoke(token)`

### Registry
- `register(name, connector_cls)`
- `get(name)`
- `load_manifest(path=None)`
- `discover(path=None)`

### Adapters
- Legacy intent adapters moved to `integrations/adapters/intent_adapters/*`.
- Legacy memory adapters moved to `integrations/adapters/memory_adapters/*`.
- Legacy vault connectors moved to `integrations/adapters/vault_connectors/*`.

## Security & Compliance
- No secret handling is implemented in this module; it must be supplied by vault-backed mechanisms in downstream integration.
- No audit emission is implemented; governance is expected to wrap execution.

## Testing Strategy
- `integrations/tests/test_registry.py` validates manifest discovery.
- `integrations/tests/test_lifecycle.py` validates lifecycle placeholder usage.

## Failure Modes
- Manifest missing or invalid prevents connector discovery.
- Import path or class name mismatch prevents registration.
- No audit enforcement without governance wrapper.

## Observability
- No structured logging or metrics in this module.

## Operational Runbook
- Deployment: library module only; no service entrypoint.
- Rollback: revert connector manifest and adapter changes.
- Upgrades: ensure manifest and connector class names remain stable.

## Ownership
- Owning team: Ecosystem Engineering.
- Review process: connector additions require security and governance review.
- Escalation path: Ecosystem On‑Call -> Platform SRE.
- SLA expectations: N/A (library module).

## Roadmap
- Add vault-backed secret retrieval.
- Add governance audit hooks for connector lifecycle.
- Add connector certification tests.
