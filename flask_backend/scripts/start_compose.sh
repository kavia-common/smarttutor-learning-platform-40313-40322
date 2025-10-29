#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
echo "Starting Postgres + Backend via docker-compose at repo root..."
docker compose -f ../../docker-compose.yml up --build
