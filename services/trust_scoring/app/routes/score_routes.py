from fastapi import APIRouter, HTTPException
import requests
from app.core.scorer import calculate_score
from app.db import SessionLocal
from app.models import TrustEvent, Tenant

router = APIRouter()

IDENTITY_VERIFY_URL = "http://127.0.0.1:8000/verify"
IDENTITY_LOOKUP_URL = "http://127.0.0.1:8000/lookup"

@router.post("/score")
def score_event(
    tenant_id: str,
    api_key: str,
    email: str,
    message: str,
    signature: str = "",
    device_fingerprint: str = ""
):
    db = SessionLocal()

    # 🔐 Validate tenant + API key
    tenant = db.query(Tenant).filter(Tenant.id == tenant_id).first()
    if not tenant or tenant.api_key != api_key:
        raise HTTPException(status_code=401, detail="Invalid API key")

    identity_verified = False
    device_match = False

    # Signature verification
    if signature:
        try:
            verify_response = requests.post(
                IDENTITY_VERIFY_URL,
                params={
                    "email": email,
                    "message": message,
                    "signature": signature
                }
            )
            identity_verified = verify_response.json().get("verified", False)
        except:
            identity_verified = False

    # Device lookup
    try:
        lookup_response = requests.get(
            IDENTITY_LOOKUP_URL,
            params={"email": email}
        )
        lookup_data = lookup_response.json()
        registered_device = lookup_data.get("device_fingerprint")

        if registered_device and device_fingerprint:
            device_match = (registered_device == device_fingerprint)
    except:
        device_match = False

    trust_score = calculate_score(identity_verified, device_match, message, email)

    # Persist event
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
def get_events(tenant_id: str, api_key: str):
    db = SessionLocal()

    tenant = db.query(Tenant).filter(Tenant.id == tenant_id).first()
    if not tenant or tenant.api_key != api_key:
        raise HTTPException(status_code=401, detail="Invalid API key")

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
