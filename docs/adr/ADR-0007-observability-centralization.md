# ADR-0007: Observability Centralization

## Context
Metrics, logging, and tracing are implemented inconsistently across subsystems. This weakens auditability and operational debugging.

## Decision
observability/ owns schemas, sinks, and instrumentation standards. Other modules only emit through observability interfaces.

## Consequences
- Standardized log formats and metrics taxonomies.
- Centralized tracing configuration.
- Easier compliance reporting.

## Metrics Standards
- All events carry correlation IDs.
- Errors are classified using a shared taxonomy.

## Alternatives Considered
- Allowing module-specific telemetry stacks: rejected due to fragmentation.
