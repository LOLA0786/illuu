#!/bin/bash

mkdir -p services/trust_identity/app
mkdir -p services/trust_identity/app/models
mkdir -p services/trust_identity/app/routes
mkdir -p services/trust_identity/app/core

touch services/trust_identity/app/main.py
touch services/trust_identity/app/models/identity.py
touch services/trust_identity/app/routes/identity_routes.py
touch services/trust_identity/app/core/crypto.py
touch services/trust_identity/requirements.txt

echo "fastapi
uvicorn
sqlalchemy
pydantic
cryptography" > services/trust_identity/requirements.txt

echo "Phase A structure created."
