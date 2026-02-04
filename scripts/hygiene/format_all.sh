#!/usr/bin/env bash
set -euo pipefail

python3 scripts/hygiene/normalize_indentation.py
black .
isort .
