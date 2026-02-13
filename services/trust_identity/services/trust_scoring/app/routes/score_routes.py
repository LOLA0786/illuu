from fastapi import APIRouter
import requests
from app.core.scorer import calculate_score

router = APIRouter()

IDENTITY_VERIFY_URL = "http://127.0.0.1:8000/verify"
IDENTITY_LOOKUP_URL = "http://127.0.0.1:8000/lookup"

@router.post("/score")
def score_event(email: str, message: str, signature: str, device_fingerprint: str):
    
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

    return {
        "trust_score": trust_score,
        "identity_verified": identity_verified,
        "device_match": device_match
    }
