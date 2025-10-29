# Testing the Flask Backend

Prereqs:
- Python 3.11+ recommended
- Create venv and install deps:
  - pip install -r requirements.txt
  - pip install -r requirements-dev.txt

Run tests:
- python scripts/run_tests.py
  - or: pytest -q

Smoke checks (with server running on :8000):
- python scripts/smoke_basic.py
- python scripts/check_core_endpoints.py
- make core-check
