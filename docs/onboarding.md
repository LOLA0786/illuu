# Onboarding

## Goals
Enable a senior engineer to understand the system in one hour.

## Read Order
1. docs/system_overview.md
2. docs/adr/ADR-0001-canonical-module-boundaries.md
3. docs/governance.md
4. docs/memory.md
5. docs/workflows.md

## Local Setup (High Level)
- Start state services (Redis, Postgres)
- Start governance proxy
- Start memory service
- Run kernel smoke workflow

## Coding Standards
- Clean Architecture
- SOLID
- Typed Python (mypy)
- Interfaces before implementation

## Where to Start
- kernel/
- workflows/
- governance/
