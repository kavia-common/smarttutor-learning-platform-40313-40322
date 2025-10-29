#!/usr/bin/env bash
set -euo pipefail
BASE="${1:-http://localhost:${PORT:-8000}}"
PATH_="${2:-/health}"
echo "GET $BASE$PATH_"
curl -i -fsS "$BASE$PATH_" | awk '/^X-Service-/{print}'
