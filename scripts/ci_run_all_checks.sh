#!/usr/bin/env bash
set -euo pipefail
# Consolidated CI runner for this hybrid repo.

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "[ci] Validating environment files..."
python "${ROOT_DIR}/scripts/validate_envs.py" || echo "[ci] Env validation failed or missing; continuing (non-blocking)."

echo "[ci] Backend health (if running on :8000)..."
python "${ROOT_DIR}/scripts/check_backend_health.py" || echo "[ci] Backend health failed or backend not running; continuing."

echo "[ci] Frontend checks..."
bash "${ROOT_DIR}/scripts/ci_decide_and_run_frontend_checks.sh"

echo "[ci] Done."
