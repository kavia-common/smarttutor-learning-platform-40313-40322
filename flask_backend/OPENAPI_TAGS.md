# OpenAPI Tags

Defined tags:
- core       — Health, version, index, basic service endpoints
- payments   — Payments, receipts (dev tooling)
- whiteboard — Sessions, events
- alembic    — Database migrations diagnostics
- headers    — Headers echo diagnostics

Validation helpers:
- scripts/openapi_summary.py — prints total paths and tags
- scripts/generate_openapi_site.py — fetches /openapi.json and writes docs/openapi.json
- scripts/serve_docs.py — serves docs/ for convenient local browsing
