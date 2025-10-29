#!/usr/bin/env bash
# Quick curl-based smoke test for the Flask backend
set -euo pipefail
BASE="${BASE:-http://127.0.0.1:8000}"

echo "Health:"
curl -fsS "$BASE/health" | jq .

echo "Status:"
curl -fsS "$BASE/api/status" | jq .

echo "Version:"
curl -fsS "$BASE/api/version" | jq .

echo "OpenAPI paths:"
curl -fsS "$BASE/openapi.json" | jq '.paths | keys'
