# SEV1 Data Breach Playbook

## Trigger
- Confirmed unauthorized data access or exfiltration.

## Immediate Actions (0–1 hour)
- Declare SEV1, notify Security Lead and SRE Lead.
- Isolate affected tenant and revoke tokens.
- Disable external egress if needed.

## Containment (1–4 hours)
- Snapshot audit logs and ledger entries.
- Rotate affected credentials/keys.
- Preserve forensic evidence.

## Notification (Within regulatory window)
- Prepare regulator notification (DPDP / GDPR as applicable).
- Notify affected customers with required details.

## Recovery
- Restore systems with clean images.
- Validate audit log integrity.
- Re-enable tenant access after approval.

## Postmortem
- RCA within 5 business days.
- Update controls and evidence registry.
