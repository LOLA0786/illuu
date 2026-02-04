# Key Rotation Runbook

## Trigger
- Scheduled rotation
- Compromise suspicion

## Steps
1. Generate new keys in KMS.
2. Update tenant key references.
3. Re-encrypt stored secrets.
4. Validate audit logs for key change events.
5. Revoke old keys.

## Evidence
- KMS logs
- Audit trail entries
