from fastapi import APIRouter
import requests

INTENT_ENGINE = "http://localhost:8000"
PRIVATE_VAULT = "http://localhost:8001"


def get_router(include_health: bool = True) -> APIRouter:
    router = APIRouter()

    if include_health:
        @router.get("/health")
        def health():
            return {"status": "ok"}

    @router.post("/execute")
    def execute(payload: dict):
        decision = requests.post(f"{INTENT_ENGINE}/authorize-intent", json=payload).json()

        if not decision.get("allowed"):
            return {
                "status": "BLOCKED",
                "reason": decision.get("reason"),
                "policy": decision.get("policy_version"),
                "evidence": decision.get("evidence_id"),
            }

        result = requests.post(f"{PRIVATE_VAULT}/vault/secure-action", json=payload).json()

        return {
            "status": "EXECUTED",
            "vault_result": result,
            "evidence": decision.get("evidence_id"),
        }

    return router
