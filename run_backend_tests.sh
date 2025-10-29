#!/usr/bin/env bash
# Convenience script to run Flask backend tests from the workspace root
set -euo pipefail
cd "$(dirname "$0")/flask_backend"
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt -r requirements.dev.txt
pytest
