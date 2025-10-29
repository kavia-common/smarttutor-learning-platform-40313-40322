# SmartTutor Flask Backend

[![Status](https://img.shields.io/badge/status-initial%20API%20ready-blue)](#)
[OpenAPI JSON](http://localhost:8000/openapi.json) • [Download OpenAPI](http://localhost:8000/openapi/download) • [Health](http://localhost:8000/health) • [Status](http://localhost:8000/api/status)

This is the Flask backend for SmartTutor. It provides database models, migrations, and REST APIs (with WebSocket endpoints planned).

Quick links:
- EXAMPLES.md – quick ways to test endpoints (REST Client, Postman)
- scripts/README.md – helper scripts index

Structure:
- app/
  - __init__.py
  - config.py
  - db.py
  - models/
    - __init__.py
    - user.py
    - course.py
    - lesson.py
    - enrollment.py
    - chat_message.py
    - whiteboard_session.py
    - whiteboard_event.py
    - payment.py
    - recommendations_cache.py
- migrations/ (Alembic)
- seed.py
- requirements.txt
- .env.example
- wsgi.py

Environment matrix:
- Dev (SQLite quick smoke):
  - DATABASE_URL=sqlite:///smarttutor.db
  - JWT_SECRET=dev_only_secret_change_me
- Dev (Postgres local):
  - DATABASE_URL=postgresql+psycopg://postgres:password@localhost:5432/smarttutor
  - JWT_SECRET=<your secret>
- Docker Compose:
  - DATABASE_URL=postgresql+psycopg://postgres:postgres@db:5432/smarttutor
  - JWT_SECRET=<your secret>

Getting started:
1) Copy .env.example -> .env and set environment variables.
   - DATABASE_URL: PostgreSQL connection string, e.g. postgresql+psycopg://user:pass@localhost:5432/smarttutor
   - JWT_SECRET: a random secret for JWT signing
   - STRIPE_SK: Stripe secret key for creating payment intents
   - CORS_ORIGINS: Comma-separated origins (e.g., http://localhost:3000)
2) Create venv and install deps:
   python -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
3) Initialize DB:
   alembic upgrade head
4) Seed initial data (optional):
   python seed.py
   - Seeds users, a sample course, and lessons for quick E2E verification
5) Run in development:
   python run_dev.py

Docker Compose:
- Compose file at ../docker-compose.yml builds backend and a Postgres service.
- On container start, migrations run automatically; seed.py is attempted (non-fatal).
- To re-run seeding:
  docker compose exec backend python seed.py

E2E verification from backend perspective:
- Health: GET http://localhost:8000/health
- Status: GET http://localhost:8000/api/status
- Payments: POST http://localhost:8000/api/payments/intent (requires STRIPE_SK)
- OpenAPI: GET http://localhost:8000/openapi.json

Docs and utilities:
- ENVIRONMENT.md for environment variables and Docker Compose notes
- COMPOSE_README.md for running Postgres + backend with Docker Compose
- DIAGNOSTICS.md for diagnostics routes and checks
- docs/openapi.html to view OpenAPI (generate with scripts/generate_openapi_site.py)
- scripts/README.md lists available helper scripts
- Quick ping: python scripts/ping_all_endpoints.py (expects backend on :8000)

Create an admin user (optional, for future auth):
   python scripts/create_admin.py --email admin@example.com --name "Admin" --password change_me_hash

Environment variables (do not hardcode in code):
- DATABASE_URL
- JWT_SECRET

Notes:
- Prefer PostgreSQL using SQLAlchemy URL driver "psycopg" (SQLAlchemy 2.x).
- Migrations are managed via Alembic; models live in app/models.
- The app factory pattern is used in app/__init__.py.
