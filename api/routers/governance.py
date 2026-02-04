from fastapi import APIRouter

router = APIRouter()

@router.get("/governance/health")
def health():
    return {"status": "ok"}
