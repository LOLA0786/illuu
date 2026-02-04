# Phase 1 Inventory (Keep / Merge / Archive / Extract)

This inventory maps current folders to Phase 1 actions. It is the authoritative reference for consolidation decisions.

## Keep (Canonical)
- kernel/
- workflows/
- integrations/
- state/
- observability/
- api/
- cli/
- docs/
- governance/
- memory/
- intent/
- oaas/
- vault/

## Merge (Move into Canonical Modules)
- vault/governance -> governance/
- vault/governance-relay -> governance/
- memory/uaal -> governance/
- vault/security -> governance/
- vault/policy_engine.py -> governance/internal/policy/
- vault/policy_registry.py -> governance/internal/policy/
- vault/guardrails.py -> governance/internal/policy/
- vault/approval_store.py -> governance/internal/approval/
- vault/approval_binding.py -> governance/internal/approval/
- vault/ml_risk_model.py -> governance/internal/risk/
- vault/audit_logger.py -> governance/internal/audit/
- vault/decision_ledger.py -> governance/internal/audit/
- vault/security_context.py -> governance/internal/security/
- vault/governance/envoy -> governance/
- vault/governance/opa -> governance/
- memory/orchestrator -> workflows/
- memory/api -> api/
- intent/api -> api/
- vault/gateway -> api/
- governance/api -> api/
- vault/services -> api/ or integrations/ (case-by-case)
- vault/cli -> cli/
- vault/privatevault-cli -> cli/
- vault/migrations -> state/migrations
- vault/config -> module-specific config/

## Extract (Canonical Subfolders)
- vault/ledgers -> vault/ledger/
- vault/enterprise-audit -> vault/audit/
- vault/monitoring -> observability/
- vault/benchmarks -> observability/benchmarks/
- vault/sdk -> integrations/sdk/
- vault/sovereign-sdk -> integrations/sdk/
- vault/connectors -> integrations/
- vault/ui/privatevault-control -> api/ui/ (or separate ui/; decision pending)

## Archive (Legacy / Duplicates / Artifacts)
- vault/privatevault-enterprise-pilot -> vault/legacy/enterprise-pilot/
- vault/demo -> vault/legacy/demos/
- vault/demos -> vault/legacy/demos/
- vault/examples -> vault/legacy/demos/
- vault/uaal-demo -> vault/legacy/demos/
- vault/test-results-* -> vault/legacy/test-artifacts/
- vault/verify2-results-* -> vault/legacy/test-artifacts/

## Notes
- This file is a plan with partial execution; governance and API moves are in progress with shims.
- Decisions that add new canonical modules require an ADR.
