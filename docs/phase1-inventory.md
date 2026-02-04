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
- This file is a plan, not an action log. No code has been moved yet.
- Decisions that add new canonical modules require an ADR.
