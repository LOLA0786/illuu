# Integrations Architecture

## Layout
- base/: connector interface and lifecycle
- auth/: SSO adapters
- adapters/: migrated legacy connectors
- mocks/: testing doubles

## Dependency Direction
- Core modules call integrations via registry.
- Integrations use vault for secrets and governance for audit.
