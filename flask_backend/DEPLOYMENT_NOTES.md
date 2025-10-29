Deployment Notes – Flask Backend

Docker (local):
- Build: docker build -t smarttutor-backend:latest .
- Run (requires PostgreSQL): 
  docker run --rm -p 8000:8000 \
    -e DATABASE_URL=postgresql+psycopg://postgres:postgres@host.docker.internal:5432/smarttutor \
    -e JWT_SECRET=change_me \
    smarttutor-backend:latest

Docker Compose (with provided Postgres service):
- Start DB: docker compose up -d
- Build and run backend against compose DB:
  docker build -t smarttutor-backend:latest .
  docker run --rm -p 8000:8000 \
    --network=host \
    -e DATABASE_URL=postgresql+psycopg://postgres:postgres@localhost:5432/smarttutor \
    -e JWT_SECRET=change_me \
    smarttutor-backend:latest

Gunicorn env vars:
- GUNICORN_BIND (default: 0.0.0.0:8000)
- GUNICORN_WORKERS (default: 2*CPU+1)
- GUNICORN_THREADS (default: 4)
- GUNICORN_TIMEOUT (default: 60)
- LOG_LEVEL (backend logging level)
