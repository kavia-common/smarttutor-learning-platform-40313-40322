#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python -m venv .venv
. .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt -r requirements-dev.txt
export DATABASE_URL=${DATABASE_URL:-sqlite:///:memory:}
export JWT_SECRET=${JWT_SECRET:-test_secret}
pytest -q
