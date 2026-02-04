# ADR-0002: Governance Is the Single Enforcement Plane

## Context
Governance and policy enforcement logic exist in multiple subsystems. This creates bypass paths, inconsistent policy evaluation, and audit gaps.

## Decision
All enforcement, policy evaluation, risk scoring, and LLM/tool mediation will live exclusively in governance/.

## Consequences
- Any governance logic found elsewhere must be migrated or wrapped behind governance interfaces.
- Kernel and workflow execution must call governance first; no bypass paths.
- Policy evaluation and enforcement are centrally testable and auditable.

## Enforcement Rules
- No direct external API or LLM calls are permitted outside governance.
- Any new enforcement capability must be added in governance/ with tests.

## Alternatives Considered
- Split enforcement between kernel and governance: rejected due to audit fragmentation.
