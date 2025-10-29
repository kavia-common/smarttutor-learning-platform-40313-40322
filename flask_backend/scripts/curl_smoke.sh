#!/usr/bin/env bash
set -euo pipefail
BASE="${1:-http://localhost:${PORT:-8000}}"
echo "Hitting $BASE ..."
echo "GET /health";        curl -fsS "$BASE/health" | jq .
echo "GET /api/status";    curl -fsS "$BASE/api/status" | jq .
echo "GET /openapi.json";  curl -fsS "$BASE/openapi.json" | jq '.info.title,.paths|keys|length' 
echo "GET /api/diag/routes"; curl -fsS "$BASE/api/diag/routes" | jq 'length'
echo "GET /api/diag/alembic"; curl -fsS "$BASE/api/diag/alembic" | jq .
echo "GET /api/ws-help";   curl -fsS "$BASE/api/ws-help" | jq .
