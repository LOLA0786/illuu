from pydantic import BaseModel

class AuthorizeRequest(BaseModel):
    action: str
    actor: str | None = None
    payload: dict | None = None
    context: dict | None = None

class AuthorizeResponse(BaseModel):
    allowed: bool
    reason: str
    policy_version: str | None = None
    evidence_id: str | None = None
