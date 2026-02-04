# ADR-0001: Canonical Module Boundaries

## Context
The repository contains multiple subsystems imported from separate projects with overlapping responsibilities. Without fixed module boundaries, duplication and tight coupling will persist and make long-term maintenance difficult.

## Decision
Adopt immutable top-level module boundaries:
- kernel/
- workflows/
- governance/
- memory/
- state/
- vault/
- intent/
- oaas/
- integrations/
- observability/
- api/
- cli/
- docs/

## Consequences
- All code must be mapped into one of these modules.
- No new top-level modules are created without a new ADR.
- Cross-module dependencies must be explicit and governed by interfaces.

## Alternatives Considered
- Keeping subsystem-specific layouts: rejected due to duplication and unclear ownership.
- Flattening into fewer modules: rejected due to loss of separation of concerns.
