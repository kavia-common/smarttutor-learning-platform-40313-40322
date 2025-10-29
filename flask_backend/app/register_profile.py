from flask import Flask
from .routes_profile import profile_bp

def register_profile(app: Flask) -> None:
    """Register profile-related routes."""
    app.register_blueprint(profile_bp)
