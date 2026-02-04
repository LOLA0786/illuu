# Deployment

## Environments
- Local development
- Staging
- Production

## Core Dependencies
- Redis (hot state)
- Postgres (cold state)
- OPA (policy evaluation)
- Object storage (evidence)

## Deployment Model
- Services deployed independently
- Governance proxy must be on critical path
- Observability agents in every service

## Configuration
- All configuration via env + typed config
- No secrets in code or repo

## Operational Requirements
- High availability for governance and state
- Ledger storage durability and backups
- Strict network policy enforcement
