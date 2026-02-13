from fastapi import FastAPI
from app.routes.identity_routes import router

app = FastAPI(title="Trust Identity Service")

app.include_router(router)

@app.get("/")
def health():
    return {"status": "Trust Identity Service running"}
