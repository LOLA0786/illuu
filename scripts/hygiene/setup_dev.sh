#!/usr/bin/env bash
set -euo pipefail

pip install -r requirements-dev.txt
pre-commit install
