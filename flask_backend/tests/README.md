Backend Tests

How to run locally:
- From flask_backend:
  - ./run_tests.sh
  or
  - python -m venv .venv && . .venv/bin/activate
  - pip install -r requirements.txt -r requirements-dev.txt
  - DATABASE_URL=sqlite:///:memory: JWT_SECRET=test_secret pytest -q

CI suggestions:
- Scope working directory to flask_backend
- Ensure DATABASE_URL and JWT_SECRET are set (SQLite in-memory is fine for unit tests)
- Avoid Flutter analyzers; React frontend is built with npm in its own job
