from fastapi import APIRouter
import requests
from app.core.scorer import calculate_score
from app.db import SessionLocal
from app.models import TrustEvent

router = APIRouter()

IDENTITY_VERIFY_URL = "http://127.0.0.1:8000/verify"
IDENTITY_LOOKUP_URL = "http://127.0.0.1:8000/lookup"

@router.post("/score")
def score_event(
    tenant_id: str,
    email: str,
    message: str,
    signature: str,
    device_fingerprint: str
):
    verify_response = requests.post(
        IDENTITY_VERIFY_URL,
        params={
            "email": email,
            "message": message,
            "signature": signature
        }
    )

    identity_verified = verify_response.json().get("verified", False)

    lookup_response = requests.get(
        IDENTITY_LOOKUP_URL,
        params={"email": email}
    )

    registered_device = lookup_response.json().get("device_fingerprint")
    device_match = (registered_device == device_fingerprint)

    trust_score = calculate_score(identity_verified, device_match, message, email)

    db = SessionLocal()

    event = TrustEvent(
        tenant_id=tenant_id,
        email=email,
        trust_score=trust_score,
        identity_verified=str(identity_verified),
        device_match=str(device_match)
    )

    db.add(event)
    db.commit()

    return {
        "trust_score": trust_score,
        "identity_verified": identity_verified,
        "device_match": device_match
    }

@router.get("/events")
def get_events(tenant_id: str):
    db = SessionLocal()
    events = db.query(TrustEvent).filter(TrustEvent.tenant_id == tenant_id).all()

    return [
        {
            "email": e.email,
            "trust_score": e.trust_score,
            "identity_verified": e.identity_verified,
            "device_match": e.device_match,
            "timestamp": e.created_at
        }
        for e in events
    ]
