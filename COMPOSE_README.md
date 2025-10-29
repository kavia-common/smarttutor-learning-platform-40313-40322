# Running with Docker Compose

Prereqs:
- Docker and Docker Compose installed

Steps:
1) Copy envs:
   cp .env.example .env
   cd smarttutor-learning-platform-40313-40322/flask_backend && cp .env.example .env && cd ../../
2) Start services:
   docker compose up -d --build
   - DB on 5432
   - Backend on http://localhost:8000
3) Initialize DB:
   docker compose exec flask_backend alembic upgrade head
4) Seed sample data (optional):
   docker compose exec flask_backend python seed.py
   # or
   docker compose exec flask_backend python scripts/seed_all_sample.py
5) Check:
   curl http://localhost:8000/health
   curl http://localhost:8000/openapi.json | python -m json.tool

Stop:
- docker compose down
- To keep DB data, a named volume "db_data" is used.
