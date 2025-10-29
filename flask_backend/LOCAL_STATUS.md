# Local Backend Status

- App factory: OK
- Database models: OK
- Alembic configured: OK
- Health endpoint: /health
- OpenAPI: /openapi.json
- Diagnostics suite: see DIAGNOSTICS.md
- Quick commands:
  - make install && make run
  - python scripts/db_setup.py --seed
  - python scripts/run_all_diagnostics.py
  - python scripts/smoke_runner.py
