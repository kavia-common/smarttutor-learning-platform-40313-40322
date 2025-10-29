#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
ENV_FILE=".env"
EXAMPLE=".env.example"
if [ ! -f "$ENV_FILE" ]; then
  if [ -f "$EXAMPLE" ]; then
    cp "$EXAMPLE" "$ENV_FILE"
    echo "Created $ENV_FILE from $EXAMPLE"
  else
    echo "Missing .env and .env.example"
    exit 1
  fi
fi
if grep -q '^DATABASE_URL=sqlite' "$ENV_FILE"; then
  sed -i.bak 's|^DATABASE_URL=sqlite.*|DATABASE_URL=postgresql+psycopg://postgres:password@localhost:5432/smarttutor|' "$ENV_FILE"
  echo "Switched DATABASE_URL to Postgres in $ENV_FILE"
else
  sed -i.bak 's|^DATABASE_URL=.*|DATABASE_URL=sqlite:///smarttutor.db|' "$ENV_FILE"
  echo "Switched DATABASE_URL to SQLite in $ENV_FILE"
fi
