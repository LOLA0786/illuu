from fastapi import APIRouter
import requests
from app.core.scorer import calculate_score

router = APIRouter()

IDENTITY_VERIFY_URL = "http://127.0.0.1:8000/verify"

@router.post("/score")
def score_event(email: str, message: str, signature: str = "", device_fingerprint: str = ""):

    identity_verified = False
    device_match = False

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

    # Temporary device match logic
    if device_fingerprint:
        device_match = True

    trust_score = calculate_score(identity_verified, device_match, message, email)

    return {
        "trust_score": trust_score,
        "identity_verified": identity_verified,
        "device_match": device_match
    }
