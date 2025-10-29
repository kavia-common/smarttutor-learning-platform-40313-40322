#!/usr/bin/env bash
set -euo pipefail
# Run flutter analyze from the correct project directory in this hybrid repo.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"

FLUTTER_DIR="${ROOT_DIR}/smarttutor-learning-platform-40313-40322/react_frontend"

if [[ ! -d "${FLUTTER_DIR}" ]]; then
  echo "Flutter directory not found: ${FLUTTER_DIR}" >&2
  exit 2
fi

cd "${FLUTTER_DIR}"
if ! command -v flutter >/dev/null 2>&1; then
  echo "flutter command not found in PATH." >&2
  exit 127
fi

flutter --version
flutter pub get
flutter analyze
