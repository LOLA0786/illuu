# Evidence Pipeline Validation

1. Ensure `compliance/evidence/config/controls.yaml` references existing evidence files.
2. Run: `python3 compliance/evidence/scripts/collect_evidence.py`.
3. Confirm output bundle exists under `compliance/evidence/output/`.
4. Verify SHA-256 hashes match source files.
5. Store bundle in WORM storage (out of scope for this script).
