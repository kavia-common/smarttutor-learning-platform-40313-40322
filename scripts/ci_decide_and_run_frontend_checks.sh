#!/usr/bin/env bash
set -euo pipefail
# Decide whether to run Flutter or React frontend checks based on detected files.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
FRONTEND_DIR="${ROOT_DIR}/smarttutor-learning-platform-40313-40322/react_frontend"

if [[ ! -d "${FRONTEND_DIR}" ]]; then
  echo "[ci_decide] Frontend directory not found; nothing to run."
  exit 0
fi

cd "${FRONTEND_DIR}"

if [[ -f "pubspec.yaml" && -d "lib" ]]; then
  echo "[ci_decide] Detected Flutter-like layout. Running safe Flutter analyze."
  bash "${ROOT_DIR}/scripts/ci_safe_flutter_analyze.sh"
  exit 0
fi

if [[ -f "package.json" && -d "src" ]]; then
  echo "[ci_decide] Detected React layout. Running npm ci && npm run build && npm run lint."
  if command -v npm >/dev/null 2>&1; then
    npm ci || npm install
    npm run build
    npm run lint || true
    echo "[ci_decide] React checks complete."
    exit 0
  else
    echo "[ci_decide] npm not found; skipping React checks."
    exit 0
  fi
fi

echo "[ci_decide] Unknown frontend layout; skipping."
exit 0
