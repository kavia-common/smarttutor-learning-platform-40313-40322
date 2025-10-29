"""
Auth blueprint providing register, login, and me endpoints.

Note:
- Simplified token approach for demo: token is 'user-{user_id}' in Authorization header.
- In production, replace with JWT (using JWT_SECRET) and proper password hashing.
"""
from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Optional, Tuple

from flask import Blueprint, request, jsonify, current_app
from sqlalchemy import select

from ..db import db
from ..models import User


auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@dataclass
class AuthUser:
    id: int
    email: str
    name: str
    role: str


def _make_token(user_id: int) -> str:
    # Placeholder token; replace with JWT in real usage
    return f"user-{user_id}"


def _parse_token(auth_header: Optional[str]) -> Optional[int]:
    """
    Parse token 'user-{id}' from Authorization header 'Bearer user-{id}'.
    """
    if not auth_header:
        return None
    parts = auth_header.split()
    if len(parts) == 2 and parts[0].lower() == "bearer" and parts[1].startswith("user-"):
        try:
            return int(parts[1].split("-", 1)[1])
        except ValueError:
            return None
    return None


def _current_user() -> Optional[User]:
    user_id = _parse_token(request.headers.get("Authorization"))
    if not user_id:
        return None
    return db.session.get(User, user_id)


# PUBLIC_INTERFACE
@auth_bp.post("/register")
def register():
    """
    Register a new user.

    Request JSON:
      - email: string
      - name: string
      - role: string (optional, defaults to 'student')

    Returns:
      201 Created with user info and token.
    """
    data = request.get_json(silent=True) or {}
    email = (data.get("email") or "").strip().lower()
    name = (data.get("name") or "").strip()
    role = (data.get("role") or "student").strip()

    if not email or not name:
        return jsonify({"error": "email and name are required"}), 400

    # Check existing
    existing = db.session.execute(select(User).where(User.email == email)).scalar_one_or_none()
    if existing:
        return jsonify({"error": "email already registered"}), 409

    user = User(email=email, name=name, role=role or "student")
    db.session.add(user)
    db.session.commit()

    token = _make_token(user.id)
    return (
        jsonify(
            {
                "user": {"id": user.id, "email": user.email, "name": user.name, "role": user.role},
                "token": token,
            }
        ),
        201,
    )


# PUBLIC_INTERFACE
@auth_bp.post("/login")
def login():
    """
    Login endpoint (email only for demo).
    In production: verify password and issue JWT.

    Request JSON:
      - email: string

    Returns:
      200 OK with user info and token.
    """
    data = request.get_json(silent=True) or {}
    email = (data.get("email") or "").strip().lower()
    if not email:
        return jsonify({"error": "email is required"}), 400

    user = db.session.execute(select(User).where(User.email == email)).scalar_one_or_none()
    if not user:
        return jsonify({"error": "invalid credentials"}), 401

    token = _make_token(user.id)
    return jsonify({"user": {"id": user.id, "email": user.email, "name": user.name, "role": user.role}, "token": token})


# PUBLIC_INTERFACE
@auth_bp.get("/me")
def me():
    """
    Return current user information based on Authorization header.

    Headers:
      - Authorization: Bearer user-{id}

    Returns:
      200 OK with user info or 401 if missing/invalid.
    """
    user = _current_user()
    if not user:
        return jsonify({"error": "unauthorized"}), 401
    return jsonify({"id": user.id, "email": user.email, "name": user.name, "role": user.role})
