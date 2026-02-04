# Compliance Control Matrix

This matrix maps illuu controls to SOC 2 Trust Services Criteria (Security, Availability, Confidentiality), ISO/IEC 27001 Annex A, and India DPDP Act requirements. It is structured for third-party audit review and evidence linkage.

## Control Mapping Table
| Control ID | Control Objective | SOC 2 (TSC) | ISO 27001 Annex A | DPDP Act | Evidence Source | Owner |
| --- | --- | --- | --- | --- | --- | --- |
| C-001 | Access provisioning and deprovisioning | CC6.1, CC6.2 | A.5.15, A.5.16 | S.8 | IAM audit logs, access review records | Security |
| C-002 | MFA for privileged access | CC6.3 | A.5.17 | S.8 | IdP policy export | Security |
| C-003 | Least privilege enforcement | CC6.6 | A.5.15 | S.8 | Role policy definitions, access reviews | Security |
| C-004 | Change management approvals | CC8.1 | A.8.32 | S.8 | Change tickets, PR approvals | Engineering |
| C-005 | Secure software development | CC8.1 | A.8.28, A.8.29 | S.8 | SDLC policies, CI logs | Engineering |
| C-006 | Data retention and deletion | CC3.1, CC8.1 | A.5.34 | S.8, S.9 | Retention policies, deletion logs | Compliance |
| C-007 | Encryption in transit | CC6.7 | A.8.24 | S.8 | TLS configs, scan results | Security |
| C-008 | Encryption at rest | CC6.7 | A.8.24 | S.8 | KMS configs, storage settings | Security |
| C-009 | Incident response | CC7.3, CC7.4 | A.5.25, A.5.26 | S.10 | IR playbooks, postmortems | Security |
| C-010 | Availability monitoring | CC7.2, A1.2 | A.8.16 | S.8 | Monitoring dashboards, alerts | SRE |
| C-011 | Backup and disaster recovery | CC7.2, A1.2 | A.8.13 | S.8 | DR runbooks, restore tests | SRE |
| C-012 | Vendor risk management | CC9.2 | A.5.19 | S.8 | Vendor due diligence records | Compliance |

## Notes
- Control IDs are stable and used for evidence mapping in audit collection.
- Evidence sources will be generated automatically via telemetry and CI artifacts.
