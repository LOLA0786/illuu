# ADR-0004: All External Calls Are Proxied Through Governance

## Context
Direct external calls reduce traceability and can bypass policy enforcement. This is unacceptable for regulated workloads.

## Decision
All LLM, tool, and external service calls must go through governance-controlled proxies and policy evaluation.

## Consequences
- Kernel, workflows, and integrations must depend on GovernanceGateway.
- Observability captures full request/response metadata for audit.
- Policy updates can be applied without changing client code.

## Security Implications
- Eliminates bypass paths.
- Enables centralized PII redaction and policy enforcement.

## Alternatives Considered
- Allow direct calls with optional governance hooks: rejected due to enforcement gaps.
