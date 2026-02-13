from fastapi import APIRouter, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.identity import Base, Identity
from app.core.crypto import generate_key_pair

DATABASE_URL = "sqlite:///./trust_identity.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base.metadata.create_all(bind=engine)

router = APIRouter()

@router.post("/register")
def register_identity(email: str, device_fingerprint: str):
    db = SessionLocal()

    existing = db.query(Identity).filter(Identity.email == email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Identity already exists")

    private_key, public_key = generate_key_pair()

    identity = Identity(
        email=email,
        public_key=public_key,
        device_fingerprint=device_fingerprint
    )

    db.add(identity)
    db.commit()
    db.refresh(identity)

    return {
        "identity_id": identity.id,
        "public_key": public_key,
        "private_key": private_key
    }
