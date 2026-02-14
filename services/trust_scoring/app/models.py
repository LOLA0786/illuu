from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import uuid

Base = declarative_base()

class TrustEvent(Base):
    __tablename__ = "trust_events"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    tenant_id = Column(String, nullable=False)
    email = Column(String, nullable=False)
    trust_score = Column(Integer, nullable=False)
    identity_verified = Column(String)
    device_match = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)


class Tenant(Base):
    __tablename__ = "tenants"

    id = Column(String, primary_key=True)
    api_key = Column(String, nullable=False)
