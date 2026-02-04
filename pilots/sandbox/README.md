# Pilot Sandbox Environment

## Purpose
Provide isolated, test-only environments for enterprise pilots with shadow-mode execution.

## Components
- `config/sandbox.yaml`: tenant and resource configuration.
- `scripts/provision_sandbox.py`: local provisioning stub.

## Policies
- No shared tenant data.
- Separate KMS keys per tenant.
- Audit logging enabled by default.
