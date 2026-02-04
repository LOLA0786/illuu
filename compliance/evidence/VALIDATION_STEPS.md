# Validation Steps

## Evidence Pipeline
1. Update `compliance/registry/controls.yaml` with control mappings.
2. Ensure evidence source files exist for referenced paths.
3. Run `python3 compliance/evidence/scripts/collect_evidence.py`.
4. Verify bundle schema against `compliance/evidence/schemas/evidence_bundle.json`.

## Control Registry
1. Validate YAML schema for controls.
2. Ensure all referenced standards are valid identifiers.
3. Confirm evidence mappings align with actual collection sources.
