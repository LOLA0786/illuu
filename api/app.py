from fastapi import FastAPI

from api.middleware.auth import auth_middleware
from api.middleware.audit import audit_middleware
from api.middleware.request_id import request_id_middleware
from api.routers.health import router as health_router
from api.routers.memory import get_router as get_memory_router
from api.routers.intent import get_router as get_intent_router
from api.routers.vault import get_router as get_vault_router
from api.routers.governance import router as governance_router

app = FastAPI(title="illuu API")

app.middleware("http")(request_id_middleware)
app.middleware("http")(auth_middleware)
app.middleware("http")(audit_middleware)

# Root health
app.include_router(health_router)

# Unified, namespaced routes
app.include_router(get_memory_router(include_health=True), prefix="/memory", tags=["memory"])
app.include_router(get_intent_router(include_health=True), prefix="/intent", tags=["intent"])
app.include_router(get_vault_router(include_health=True), prefix="/vault", tags=["vault"])
app.include_router(governance_router, tags=["governance"])

# Legacy root routes (no /health to avoid conflicts)
app.include_router(get_memory_router(include_health=False), tags=["memory-legacy"])
app.include_router(get_intent_router(include_health=False), tags=["intent-legacy"])
app.include_router(get_vault_router(include_health=False), tags=["vault-legacy"])
