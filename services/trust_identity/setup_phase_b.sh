#!/bin/bash

mkdir -p services/trust_scoring/app
mkdir -p services/trust_scoring/app/routes
mkdir -p services/trust_scoring/app/core

touch services/trust_scoring/app/main.py
touch services/trust_scoring/app/routes/score_routes.py
touch services/trust_scoring/app/core/scorer.py
touch services/trust_scoring/requirements.txt

echo "fastapi
uvicorn
requests
pydantic" > services/trust_scoring/requirements.txt

echo "Phase B structure created."
