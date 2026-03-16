# DOCS

## Purpose
The intent module computes and exposes human intent signals used to inform authorization and governance decisions.

## Scope

### In Scope
- Intent scoring in `intent/engine/scoring.py`.
- Intent explainability primitives in `intent/engine/explain.py`.
- FastAPI endpoints in `intent/api/server.py`.
- Adapter code relocated to `integrations/adapters/intent_adapters/` with shims in `intent/adapters/__init__.py`.

### Out of Scope
- Enforcement of policy decisions (owned by `governance/`).
- Persistent storage of intent data (current implementation is in-memory only).
- External SDKs.

## Architecture
The API stores intents in process memory (`INTENTS` list). Injected intents are scored by attributes such as momentum, confidence, authenticity, streak, and time decay.

Text diagram:

```
POST /inject-intent
  -> in-memory INTENTS
POST /verify-intent
  -> compare last intent topic
Scoring
  -> engine/scoring.py
```

## Interfaces

### HTTP Endpoints (intent/api/server.py)
- `GET /health`
- `POST /inject-intent` with payload `{topic, confidence, momentum, authenticity, streak_days}`
- `POST /verify-intent` with payload `{topic}`

### Public Functions
- `intent/engine/scoring.compute_intent_score(intent: dict) -> float`.

## Security & Compliance
- No authentication or authorization is enforced by this module.
- Intents are stored in process memory; there is no persistence or access control.

## Testing Strategy
- `intent/tests/test_scoring.py` covers scoring behavior.
- No API integration tests are present in this module.

## Failure Modes
- Process restart clears all intent history.
- Missing `created_at` yields a score of `0.0`.
- Lack of persistence can break authorization expectations.

## Observability
- No structured logging, metrics, or tracing are present in this module.

## Operational Runbook
- Deployment: run FastAPI app in `intent/api/server.py`.
- Rollback: redeploy previous container.
- Upgrades: no migration steps due to in-memory storage.

## Ownership
- Owning team: Governance Intelligence.
- Review process: scoring changes require risk review.
- Escalation path: Governance On‑Call -> Platform SRE.
- SLA expectations: Tier‑2; intent is advisory but used in authorization flows.

## Roadmap
- Replace in-memory store with persistent storage.
- Add signed intent evidence for audits.
- Add API authentication.
