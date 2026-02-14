from app.db import SessionLocal
from app.models import Tenant

db = SessionLocal()

tenant = Tenant(
    id="acme",
    api_key="acme-secret-key"
)

db.add(tenant)
db.commit()

print("Tenant created successfully")
