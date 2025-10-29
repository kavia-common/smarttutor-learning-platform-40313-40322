# Backend smoke tests

- Start backend: `make install && make run`
- In another terminal:
  - `python scripts/print_config.py`
  - `python scripts/check_migrations.py`
  - `python scripts/verify_models.py`
  - `python scripts/table_counts.py`
  - `python scripts/smoke_all_in_one.py`

Expected:
- All endpoints return JSON payloads with reasonable values.
- Table counts are 0 before seeding; run `make seed` to populate sample data.
