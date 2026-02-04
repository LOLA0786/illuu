from pydantic import BaseModel

class IngestRequest(BaseModel):
    content: str
    owner: str = "system"
    metadata: dict = {}

class IngestResponse(BaseModel):
    doc_id: str
    status: str

class QueryResponse(BaseModel):
    query: str
    results: list
