# ADR-0003: Ledger and Evidence Storage Owned by Vault

## Context
Ledger and audit evidence components appear in multiple locations. A single canonical ledger implementation is required for cryptographic integrity and long-term maintenance.

## Decision
Vault owns the ledger and evidence storage. All other modules interact with the ledger through defined interfaces.

## Consequences
- Governance and kernel write audit events via the Vault ledger interface only.
- Ledger verification logic remains isolated in vault/.
- Ledger and evidence storage are versioned and immutable.

## Interfaces Impacted
- AuditLedger.append
- AuditLedger.verify

## Alternatives Considered
- Placing ledger in governance: rejected because governance should not own storage primitives.
