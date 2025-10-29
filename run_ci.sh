#!/usr/bin/env bash
# CI pipeline script to build React frontend and test Flask backend.
# This intentionally avoids any Flutter tooling since the frontend is React (Vite).
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"

echo "== Backend tests =="
pushd "$ROOT/flask_backend" >/dev/null
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt -r requirements.dev.txt
pytest
deactivate
popd >/dev/null

echo "== Frontend build (React Vite) =="
pushd "$ROOT/react_frontend" >/dev/null
if [ ! -f .env ]; then
  cp .env.example .env
fi
npm ci || npm install
npm run build
popd >/dev/null

echo "CI run completed successfully."
