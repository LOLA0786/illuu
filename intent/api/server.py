from fastapi import FastAPI

from api.routers.intent import get_router

api = FastAPI()
api.include_router(get_router(include_health=True))
