"""
Flask application factory for SmartTutor backend.

Creates the Flask app, configures SQLAlchemy and Alembic integration,
and registers blueprints (future). Reads DATABASE_URL and JWT_SECRET from environment variables.

Environment variables required (configure in .env):
- DATABASE_URL: SQLAlchemy DB URL (e.g., postgresql+psycopg://user:pass@host:5432/dbname)
- JWT_SECRET: secret for JWT tokens (used by auth, future)
"""
from __future__ import annotations

import os
from flask import Flask
from .db import db


def _get_database_url() -> str:
    """Return database URL from env or raise informative error."""
    url = os.getenv("DATABASE_URL")
    if not url:
        raise RuntimeError(
            "DATABASE_URL is not set. Create .env from .env.example and set DATABASE_URL."
        )
    return url


# PUBLIC_INTERFACE
def create_app() -> Flask:
    """Application factory for the SmartTutor Flask app."""
    app = Flask(__name__)

    # Minimal configuration
    app.config["SQLALCHEMY_DATABASE_URI"] = _get_database_url()
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize database
    db.init_app(app)

    # Simple health route
    @app.get("/health")
    def health():
        """Healthcheck endpoint."""
        return {"status": "ok"}

    # Placeholder status route for quick smoke
    @app.get("/api/status")
    def api_status():
        """Backend status endpoint."""
        return {"api": "smarttutor", "status": "ready"}

    return app
