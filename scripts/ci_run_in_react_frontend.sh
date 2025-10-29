#!/usr/bin/env bash
set -euo pipefail
# Usage: scripts/ci_run_in_react_frontend.sh <command...>
# Forces CWD to the React frontend path to avoid Flutter root detection errors in hybrid repo CI.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
APP_DIR="${ROOT_DIR}/smarttutor-learning-platform-40313-40322/react_frontend"

if [[ ! -d "${APP_DIR}" ]]; then
  echo "React frontend directory not found at: ${APP_DIR}" >&2
  exit 2
fi

cd "${APP_DIR}"
exec "$@"
