# Governance

## Purpose
Defines the enforcement plane for all LLM/tool calls, policy evaluation, risk scoring, and audit hooks.

## Responsibilities
- Enforce policies via OPA and risk engine
- Proxy all external calls (LLM, tools, services)
- Emit audit ledger events
- Provide compliance and kill-switch controls

## Interfaces
- GovernanceGateway.authorize
- PolicyEngine.evaluate
- AuditLedger.append (via Vault)

## Data Flow
1. Kernel submits action context to governance.
2. Governance evaluates policy and risk.
3. If approved, governance proxies the call.
4. Ledger event is recorded.

## Extension Points
- New policy bundles
- New proxy adapters
- Risk scoring plugins

## Failure Modes
- Policy engine unavailable
- Proxy latency spikes
- Ledger append failure

## Testing Strategy
- Unit tests for policy evaluation
- Integration tests with proxy + OPA
- Audit replay tests
