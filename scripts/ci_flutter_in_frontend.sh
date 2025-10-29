#!/usr/bin/env bash
set -euo pipefail
# Usage: scripts/ci_flutter_in_frontend.sh <flutter args...>
# Forces CWD to the React/Flutter hybrid frontend to avoid "Could not determine project root" errors.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
APP_DIR="${ROOT_DIR}/smarttutor-learning-platform-40313-40322/react_frontend"

if [[ ! -d "${APP_DIR}" ]]; then
  echo "React/Flutter frontend directory not found at: ${APP_DIR}" >&2
  exit 2
fi

cd "${APP_DIR}"

if ! command -v flutter >/dev/null 2>&1; then
  echo "flutter command not found in PATH. Skipping." >&2
  exit 127
fi

exec flutter "$@"
