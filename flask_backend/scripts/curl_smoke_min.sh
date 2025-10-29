#!/usr/bin/env bash
set -euo pipefail
BASE="${1:-http://localhost:${PORT:-8000}}"
echo "GET $BASE/health"
curl -fsS "$BASE/health" || { echo "Health failed"; exit 1; }
echo
echo "GET $BASE/api/status"
curl -fsS "$BASE/api/status" || { echo "Status failed"; exit 1; }
echo
echo "GET $BASE/openapi.json (first 200 chars)"
curl -fsS "$BASE/openapi.json" | head -c 200 || true
echo
echo "Smoke OK"
