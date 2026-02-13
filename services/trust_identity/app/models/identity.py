from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import uuid

Base = declarative_base()

class Identity(Base):
    __tablename__ = "identities"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    email = Column(String, unique=True, nullable=False)
    public_key = Column(String, nullable=False)
    device_fingerprint = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
