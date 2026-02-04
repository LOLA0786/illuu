from fastapi import FastAPI

from api.routers.memory import get_router

app = FastAPI(title="Knowledge Vault")
app.include_router(get_router(include_health=True))
