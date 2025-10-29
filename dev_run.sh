#!/usr/bin/env bash
# Run Flask backend (docker-compose) and React frontend (Vite) together for local development.
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
BACKEND_DIR="$ROOT_DIR/flask_backend"
FRONTEND_DIR="$ROOT_DIR/react_frontend"

echo "Starting backend (docker-compose) ..."
( cd "$BACKEND_DIR" && docker compose up --build -d )

echo "Ensuring frontend .env exists ..."
if [ ! -f "$FRONTEND_DIR/.env" ]; then
  cp "$FRONTEND_DIR/.env.example" "$FRONTEND_DIR/.env"
fi

echo "Starting frontend dev server ..."
( cd "$FRONTEND_DIR" && npm install && npm run dev )
