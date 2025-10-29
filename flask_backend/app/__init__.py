"""
Flask application factory for SmartTutor backend.

Creates the Flask app, configures SQLAlchemy, registers blueprints, enables CORS
for React dev server (port 3000), sets up Socket.IO namespaces, and exposes a
minimal /openapi.json for frontend consumption.

Environment variables required (configure in .env):
- DATABASE_URL: SQLAlchemy DB URL (e.g., postgresql+psycopg://user:pass@host:5432/dbname)
- JWT_SECRET: secret for JWT tokens (future JWT)
- STRIPE_SK: Stripe secret key for /api/payments/intent
"""
from __future__ import annotations

import os
from flask import Flask, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO

from .db import db
from .api import create_api_blueprint
from .api.auth import auth_bp
from .api.catalog import catalog_bp
from .api.enrollments import enroll_bp
from .api.recommendations import reco_bp
from .api.payments import payments_bp
from .api.docs import docs_bp
from .sockets import ChatNamespace, WhiteboardNamespace

# SocketIO instance (initialized in create_app)
socketio: SocketIO | None = None


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

    # Core configuration
    app.config["SQLALCHEMY_DATABASE_URI"] = _get_database_url()
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config.setdefault("JSON_SORT_KEYS", False)

    # Initialize database
    db.init_app(app)

    # Enable CORS for React on :3000
    CORS(
        app,
        resources={r"/api/*": {"origins": ["http://localhost:3000", "http://127.0.0.1:3000"]}},
        supports_credentials=True,
    )

    # Register API blueprints (mounted under /api)
    api_bp = create_api_blueprint()
    api_bp.register_blueprint(auth_bp)
    api_bp.register_blueprint(catalog_bp)
    api_bp.register_blueprint(enroll_bp)
    api_bp.register_blueprint(reco_bp)
    api_bp.register_blueprint(payments_bp)
    api_bp.register_blueprint(docs_bp)
    app.register_blueprint(api_bp)

    # Health and status
    @app.get("/health")
    def health():
        """Healthcheck endpoint."""
        return {"status": "ok"}

    @app.get("/api/status")
    def api_status():
        """Backend status endpoint."""
        return {"api": "smarttutor", "status": "ready"}

    # Minimal OpenAPI document
    @app.get("/openapi.json")
    def openapi_json():
        """
        Return minimal OpenAPI spec for core routes.
        """
        spec = {
            "openapi": "3.0.3",
            "info": {"title": "SmartTutor API", "version": "0.1.0", "description": "SmartTutor REST API"},
            "servers": [{"url": "http://localhost:8000"}],
            "paths": {
                "/api/auth/register": {"post": {"summary": "Register", "tags": ["auth"], "responses": {"201": {"description": "Created"}}}},
                "/api/auth/login": {"post": {"summary": "Login", "tags": ["auth"], "responses": {"200": {"description": "OK"}}}},
                "/api/auth/me": {"get": {"summary": "Current user", "tags": ["auth"], "responses": {"200": {"description": "OK"}, "401": {"description": "Unauthorized"}}}},
                "/api/catalog/courses": {"get": {"summary": "List courses", "tags": ["catalog"], "responses": {"200": {"description": "OK"}}}},
                "/api/catalog/courses/{course_id}/lessons": {
                    "get": {
                        "summary": "List lessons",
                        "tags": ["catalog"],
                        "parameters": [{"in": "path", "name": "course_id", "required": True, "schema": {"type": "integer"}}],
                        "responses": {"200": {"description": "OK"}},
                    }
                },
                "/api/catalog/search": {
                    "get": {
                        "summary": "Search courses",
                        "tags": ["catalog"],
                        "parameters": [{"in": "query", "name": "q", "schema": {"type": "string"}}],
                        "responses": {"200": {"description": "OK"}},
                    }
                },
                "/api/enrollments": {
                    "get": {"summary": "List my enrollments", "tags": ["enrollments"], "responses": {"200": {"description": "OK"}, "401": {"description": "Unauthorized"}}},
                    "post": {"summary": "Create enrollment", "tags": ["enrollments"], "responses": {"201": {"description": "Created"}, "401": {"description": "Unauthorized"}}},
                },
                "/api/recommendations": {"get": {"summary": "Get recommendations", "tags": ["recommendations"], "responses": {"200": {"description": "OK"}}}},
                "/api/payments/intent": {"post": {"summary": "Create payment intent", "tags": ["payments"], "responses": {"200": {"description": "OK"}}}},
            },
            "tags": [
                {"name": "auth"},
                {"name": "catalog"},
                {"name": "enrollments"},
                {"name": "recommendations"},
                {"name": "payments"},
            ],
        }
        return jsonify(spec)

    # Initialize Socket.IO and namespaces
    global socketio
    socketio = SocketIO(app, cors_allowed_origins=["http://localhost:3000", "http://127.0.0.1:3000"])
    socketio.on_namespace(ChatNamespace("/chat"))
    socketio.on_namespace(WhiteboardNamespace("/whiteboard"))

    return app
