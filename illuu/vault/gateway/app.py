from fastapi import FastAPI

from api.routers.vault import get_router

app = FastAPI(title="PrivateIntent OS")
app.include_router(get_router(include_health=True))
