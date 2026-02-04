# DOCS

## Purpose
The oaas module exposes an Optimization-as-a-Service engine that computes recommended next values using a Nesterov optimizer.

## Scope

### In Scope
- Flask API in `oaas/app.py` with `/optimize` endpoint.
- Optimization logic in `oaas/nesterov_engine.py` and related engines.

### Out of Scope
- Governance enforcement (owned by `governance/`).
- Tenant isolation and billing (owned by `vault/` and `api/`).

## Architecture
The Flask app maintains an in-memory `client_states` registry keyed by `client_id` and metric, and reuses a `UniversalNesterovOptimizer` instance per key.

Text diagram:

```
POST /optimize
  -> client_states lookup
  -> UniversalNesterovOptimizer.optimize()
  -> JSON response
```

## Interfaces

### HTTP Endpoint (oaas/app.py)
- `POST /optimize`
  - Request JSON: `client_id`, `metric`, `current_val`, `gradient`, `industry`.
  - Response JSON: `status`, `industry`, `recommended_next_value`, `logic`.

## Security & Compliance
- No authentication or authorization is implemented.
- No governance enforcement or audit logging is present.

## Testing Strategy
- No tests are present in this module.

## Failure Modes
- Process restart clears `client_states`.
- Invalid input arrays may raise runtime errors from NumPy.

## Observability
- No structured logs, metrics, or tracing are present.

## Operational Runbook
- Deployment: run `oaas/app.py` (Flask server) on port 5000.
- Rollback: redeploy previous container.

## Ownership
- Owning team: Optimization Platform.
- Review process: model and algorithm changes require performance review.
- Escalation path: Platform SRE.
- SLA expectations: Tier‑2.

## Roadmap
- Add authentication and governance enforcement.
- Add persistence for client state.
