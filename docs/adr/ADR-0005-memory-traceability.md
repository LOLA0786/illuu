# ADR-0005: Memory Is Read-First and Traceable

## Context
Agents need deterministic, auditable context. Ad-hoc retrieval breaks traceability and creates provenance gaps.

## Decision
All context binding must be served by memory/ with versioned sources and temporal queries. Memory is read-first and provides provenance metadata for every context bundle.

## Consequences
- Kernel and workflows must request context via MemoryStore.
- Any cache or derived context must retain source references.
- Memory becomes the single source of truth for context retrieval.

## Audit Requirements
- Every context response includes source IDs and versions.
- Temporal queries must be reproducible.

## Alternatives Considered
- Allowing local context caches without provenance: rejected due to audit risk.
