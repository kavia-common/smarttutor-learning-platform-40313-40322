# CI Usage

This is a hybrid repository with a React frontend and a Flask backend. Some CI analyzers may try to detect a Flutter root and fail.

To run commands in the React frontend context during CI:
- scripts/ci_run_in_react_frontend.sh npm ci
- scripts/ci_run_in_react_frontend.sh npm run build
- scripts/ci_run_in_react_frontend.sh npm run lint

To run backend checks:
- make backend-health
- python scripts/check_backend_health.py
- docker compose up --build -d && make compose-migrate-seed
