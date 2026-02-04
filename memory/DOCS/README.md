# DOCS

## Purpose
The memory module implements the Knowledge Vault data plane for ingesting content, generating embeddings, and serving retrieval queries for agents.

## Scope

### In Scope
- Ingest pipeline (`memory/ingest/*`) for repos, APIs, and files.
- Embedding generation via `memory/embeddings/embedding_provider.py`.
- Vector storage with ChromaDB in `memory/store/vector_store.py`.
- Retrieval interface in `memory/access/retrieval.py`.
- FastAPI service in `memory/api/server.py`.

### Out of Scope
- Governance enforcement (owned by `governance/`).
- Audit ledger persistence (owned by `vault/`).
- Workflow orchestration (owned by `workflows/`).

## Architecture
Ingest requests are embedded and persisted to a ChromaDB collection named `knowledge_vault`. Queries are embedded and matched against the vector store. The API exposes `/ingest` and `/query` endpoints and returns raw results from the vector store.

Text diagram:

```
API /ingest
  -> embeddings/embedding_provider.py
  -> store/vector_store.py (ChromaDB)
API /query
  -> access/retrieval.py
  -> store/vector_store.py
```

## Interfaces

### HTTP Endpoints (memory/api/server.py)
- `GET /health`
- `POST /ingest` with payload `{content, owner, metadata}`
- `GET /query` with query string `q` and `actor_id`

### Internal Functions
- `embeddings.embed_text(content)` in `memory/embeddings/embedding_provider.py`.
- `store.vector_store.upsert_embedding(doc_id, embedding, metadata)`.
- `store.vector_store.query_embedding(query_embedding, top_k=5)`.
- `access.retrieval.query_knowledge(query, actor_id)`.

### Contracts
- `memory/contracts/vault_api.yaml` exists but is not referenced in code.

## Security & Compliance
- No access control is enforced in retrieval; `memory/access/permissions.py` returns `False` but is not used.
- `memory/access/audit_log.py` is a stub and does not emit audit evidence.
- This module currently lacks governance integration for access decisions.

## Testing Strategy
- No unit tests are present in this module.
- Integration testing should validate ingestion, retrieval, and persistence in ChromaDB.

## Failure Modes
- ChromaDB unavailable or storage path inaccessible prevents persistence.
- Embedding provider errors prevent ingestion.
- Retrieval returns empty results without access control checks.

## Observability
- No structured logging or metrics are present in this module.

## Operational Runbook
- Deployment: run `memory/api/server.py` or containerized service with ChromaDB storage at `./data/chroma`.
- Rollback: redeploy previous container.
- Upgrades: preserve persisted ChromaDB directory.

## Ownership
- Owning team: Memory Platform.
- Review process: schema and retrieval changes require governance review.
- Escalation path: Memory On‑Call -> Platform SRE -> Security.
- SLA expectations: Tier‑1 for production retrieval availability.

## Roadmap
- Replace access and audit stubs with governance-backed enforcement.
- Add provenance metadata and temporal query support.
- Add unit and integration tests.
