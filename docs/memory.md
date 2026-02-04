# Memory

## Purpose
Provide a traceable, versioned memory layer for context binding and evidence of retrieval.

## Responsibilities
- Ingest structured/unstructured data
- Version and store documents
- Provide temporal queries
- Return provenance with every context bundle

## Interfaces
- MemoryStore.bind
- MemoryStore.query
- MemoryStore.ingest

## Data Flow
1. Ingest pipeline normalizes and versions data.
2. Indexing produces vector and keyword indices.
3. Kernel/workflows request context bundles with provenance.

## Extension Points
- New adapters
- Additional vector stores
- Schema evolution

## Failure Modes
- Index drift
- Stale vector cache
- Missing provenance

## Testing Strategy
- Deterministic retrieval tests
- Temporal query replay
- Provenance verification
