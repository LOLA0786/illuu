# Disaster Recovery Plan

## Objectives
- RTO: 4h (Tier 1), 24h (Tier 2)
- RPO: 15m (Tier 1), 4h (Tier 2)

## Steps
1. Declare DR event.
2. Fail over to secondary region.
3. Restore state from backups.
4. Validate governance and audit ledger integrity.
5. Re-enable tenant traffic.

## Testing
- Quarterly failover tests
- Monthly restore tests
