# Integrations

## Purpose
Provide a unified, governed connector framework for external systems with consistent lifecycle, security, and auditability.

## Scope
- In scope: connector interface, registry, lifecycle, auth adapters, mocks.
- Out of scope: vendor business logic embedded in core modules.

## Interfaces
- integrations/base/connector.py
- integrations/base/registry.py
- integrations/base/lifecycle.py

## Testing
- Registry discovery tests
- Mock connector lifecycle tests
