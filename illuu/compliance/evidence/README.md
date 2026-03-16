# Compliance Evidence Pipeline

## Purpose
Automate evidence collection for SOC2, ISO 27001, and DPDP controls using immutable, auditable artifacts.

## Components
- `config/controls.yaml`: control registry and evidence mapping.
- `scripts/collect_evidence.py`: generates evidence bundles from sources.
- `schemas/evidence_bundle.json`: bundle schema contract.
- `output/`: generated bundles (excluded from repo in production).

## Usage
- Configure controls in `config/controls.yaml`.
- Run `python3 compliance/evidence/scripts/collect_evidence.py`.
- Review bundle output and manifest.
