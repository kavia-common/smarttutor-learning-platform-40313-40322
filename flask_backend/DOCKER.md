Run with Docker and Docker Compose

Prerequisites:
- Docker and docker-compose installed

Steps:
1) cd smarttutor-learning-platform-40313-40322/flask_backend
2) cp .env.example .env
   - Optionally adjust DATABASE_URL to: postgresql+psycopg://smarttutor:smarttutor@db:5432/smarttutor
3) docker compose up --build
   - Backend: http://localhost:8000
   - Health: http://localhost:8000/health
   - API root: http://localhost:8000/api/
   - OpenAPI: http://localhost:8000/openapi.json

Notes:
- The compose file launches a local Postgres (db service) and the backend.
- On startup, migrations are applied automatically before serving traffic.
