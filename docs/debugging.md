# Debugging

## Principles
- Every decision is traceable
- All workflows are replayable
- Ledger is source of truth

## Debug Checklist
- Verify governance decision path
- Inspect ledger events for the run
- Check state checkpoints and resumes
- Validate memory provenance

## Common Failure Patterns
- Governance rejection due to policy drift
- Missing context provenance
- State recovery loop

## Tools
- Audit explorer (control plane)
- Workflow replay tooling
- Trace correlation IDs
