from pydantic import BaseModel

class InjectIntentRequest(BaseModel):
    topic: str
    confidence: float | None = None
    momentum: str | None = None
    authenticity: dict | None = None
    streak_days: int | None = None

class InjectIntentResponse(BaseModel):
    id: str

class VerifyIntentRequest(BaseModel):
    topic: str

class VerifyIntentResponse(BaseModel):
    allowed: bool
    reason: str
    intent_score: float | None = None
