#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."

echo "== Environment diagnostics =="
python scripts/env_diag.py || true

echo "== Check required env vars =="
python scripts/check_env_vars.py || true

echo "== Print config =="
python scripts/print_config.py || true

echo "== Alembic head =="
python scripts/check_alembic_head.py || true

echo "== Verify models =="
python scripts/verify_models.py || true

echo "== Table counts (may fail if migrations not applied) =="
python scripts/table_counts.py || true

echo "== Curl smoke (no jq) =="
bash scripts/curl_smoke_min.sh || true

echo "== OpenAPI validation (ensure server running) =="
python scripts/validate_openapi.py || true

echo "Diagnostics completed."
