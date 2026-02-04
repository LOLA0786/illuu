from fastapi import FastAPI
from pydantic import BaseModel
from embeddings.embedding_provider import embed_text
from store.vector_store import upsert_embedding
from access.retrieval import query_knowledge
import uuid

app = FastAPI(title="Knowledge Vault")

class IngestRequest(BaseModel):
    content: str
    owner: str = "system"
    metadata: dict = {}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/ingest")
def ingest(req: IngestRequest):
    doc_id = str(uuid.uuid4())
    embedding = embed_text(req.content)

    upsert_embedding(
        doc_id=doc_id,
        embedding=embedding,
        metadata={
            "owner": req.owner,
            **req.metadata
        }
    )

    return {
        "doc_id": doc_id,
        "status": "ingested"
    }

@app.get("/query")
def query(q: str, actor_id: str = "boss-ai"):
    results = query_knowledge(q, actor_id)
    return {
        "query": q,
        "results": results
    }
