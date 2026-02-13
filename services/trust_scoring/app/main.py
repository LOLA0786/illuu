from fastapi import FastAPI
from app.routes.score_routes import router

app = FastAPI(title="Trust Scoring Service")

app.include_router(router)

@app.get("/")
def health():
    return {"status": "Trust Scoring running"}
