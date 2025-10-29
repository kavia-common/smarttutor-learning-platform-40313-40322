"""
API package initialization for SmartTutor Flask backend.

This module exposes factory functions to create and register API blueprints
and Socket.IO namespaces for chat and whiteboard.
"""
from __future__ import annotations

from flask import Blueprint


def create_api_blueprint() -> Blueprint:
    """
    Create the root API blueprint '/api' to which sub-blueprints will be registered.
    """
    api_bp = Blueprint("api", __name__, url_prefix="/api")
    return api_bp
