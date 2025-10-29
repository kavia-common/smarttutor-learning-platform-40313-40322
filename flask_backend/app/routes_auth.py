from flask import Blueprint, request, jsonify, current_app
from werkzeug.exceptions import BadRequest

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")

# PUBLIC_INTERFACE
@auth_bp.post("/register")
def register():
    """
    summary: Register a new user
    description: Create a user account and return a placeholder JWT token.
    responses:
      200:
        description: Registration success
    """
    data = request.get_json(silent=True) or {}
    email = data.get("email")
    password = data.get("password")
    name = data.get("name") or email
    if not email or not password:
        raise BadRequest("email and password are required")
    # TODO: persist using models.User with hashed pw
    token = f"dev-token-for-{email}"
    return jsonify({"token": token, "user": {"email": email, "name": name}})

# PUBLIC_INTERFACE
@auth_bp.post("/login")
def login():
    """
    summary: Login user
    description: Validate credentials and return a placeholder JWT token.
    responses:
      200:
        description: Login success
    """
    data = request.get_json(silent=True) or {}
    email = data.get("email")
    password = data.get("password")
    if not email or not password:
        raise BadRequest("email and password are required")
    token = f"dev-token-for-{email}"
    return jsonify({"token": token, "user": {"email": email}})

# PUBLIC_INTERFACE
@auth_bp.get("/profile")
def profile():
    """
    summary: Get current user profile
    description: Returns a placeholder profile based on Authorization header (dev mode).
    responses:
      200:
        description: Profile payload
    """
    authz = request.headers.get("Authorization", "")
    email = "user@example.com"
    if authz.startswith("Bearer dev-token-for-"):
        email = authz.replace("Bearer dev-token-for-", "").strip()
    return jsonify({"email": email, "name": email.split("@")[0].title()})
