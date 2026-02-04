# ADR-0008: Control Plane Purity (API and CLI)

## Context
Mixing domain logic with control-plane entrypoints makes code harder to test and violates Clean Architecture.

## Decision
api/ and cli/ are pure control-plane layers. They may orchestrate requests but cannot own domain logic.

## Consequences
- Domain logic stays in kernel, workflows, governance, memory, state, vault, intent, and integrations.
- API and CLI are thin adapters with strict dependency direction.
- Improves testability and long-term maintainability.

## Testability Notes
- API and CLI tests should mock domain interfaces.

## Alternatives Considered
- Embedding domain logic in API routes: rejected due to coupling.
