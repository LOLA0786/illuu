from pydantic import BaseModel

class ExecuteRequest(BaseModel):
    action: str | None = None
    payload: dict | None = None
    context: dict | None = None

class ExecuteResponse(BaseModel):
    status: str
    vault_result: dict | None = None
    evidence: str | None = None
