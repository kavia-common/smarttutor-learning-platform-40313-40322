PY ?= python

# Backend quick health check (expects backend running locally on :8000)
backend-health:
	$(PY) scripts/check_backend_health.py

# Print Flutter project root path for CI that needs it
flutter-root:
	$(PY) scripts/print_flutter_root.py

# Print React project root path for CI/tooling
react-root:
	$(PY) scripts/print_react_root.py

# Start backend (dev) from repo root
backend-dev:
	$(PY) scripts/run_backend_dev.py

# Start backend (gunicorn) from repo root
backend-gunicorn:
	$(PY) scripts/run_backend_gunicorn.py

# Compose: migrate and seed inside backend container
compose-migrate-seed:
	bash scripts/compose_migrate_and_seed.sh

# Run Flutter analyze safely (skips if not applicable)
flutter-analyze-safe:
	bash scripts/ci_safe_flutter_analyze.sh

# CI meta target to run basic checks
ci-basic:
	make react-root
	make backend-health || true
	make flutter-analyze-safe

# Run consolidated CI checks (env validation, backend health, frontend decision)
ci-all:
	bash scripts/ci_run_all_checks.sh
