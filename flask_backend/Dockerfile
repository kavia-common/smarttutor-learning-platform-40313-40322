# SmartTutor Flask Backend Dockerfile
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# System deps (psycopg binary uses libpq; install curl for health checks)
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl build-essential gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirement files first for better caching
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy source
COPY . /app

# Expose backend port
EXPOSE 8000

# Default environment (override with .env in compose)
ENV HOST=0.0.0.0
ENV PORT=8000

# Run migrations on start then launch app
# Using a small entrypoint script for clarity
CMD bash -lc "alembic upgrade head && python seed.py || true; python wsgi.py"
