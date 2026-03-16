from fastapi import APIRouter
from pydantic import BaseModel
import uuid

def get_router(include_health: bool = True) -> APIRouter:
    router = APIRouter()

    class IngestRequest(BaseModel):
        content: str
        owner: str = "system"
        metadata: dict = {}

    if include_health:
        @router.get("/health")
        def health():
            return {"status": "ok"}

    @router.post("/ingest")
    def ingest(req: IngestRequest):
        from embeddings.embedding_provider import embed_text
        from store.vector_store import upsert_embedding

        doc_id = str(uuid.uuid4())
        embedding = embed_text(req.content)

        upsert_embedding(
            doc_id=doc_id,
            embedding=embedding,
            metadata={
                "owner": req.owner,
                **req.metadata,
            },
        )

        return {
            "doc_id": doc_id,
            "status": "ingested",
        }

    @router.get("/query")
    def query(q: str, actor_id: str = "boss-ai"):
        from access.retrieval import query_knowledge

        results = query_knowledge(q, actor_id)
        return {
            "query": q,
            "results": results,
        }

    return router
