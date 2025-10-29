PY ?= python

run-dev:
	$(PY) run_dev.py

migrate:
	alembic upgrade head

revision:
	alembic revision --autogenerate -m "$(m)"

seed:
	$(PY) seed.py

core-check:
	$(PY) scripts/check_core_endpoints.py

openapi-site:
	$(PY) scripts/generate_openapi_site.py

openapi-site-serve:
	$(PY) scripts/serve_docs.py

env-info:
	$(PY) scripts/print_env_and_service.py

ping-all:
	$(PY) scripts/ping_all_endpoints.py
