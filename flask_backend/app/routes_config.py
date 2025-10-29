from flask import Blueprint, jsonify, current_app

config_bp = Blueprint("config", __name__, url_prefix="/api")

# PUBLIC_INTERFACE
@config_bp.get("/config")
def get_config():
    """
    summary: Config diagnostics (safe subset)
    description: Returns a safe subset of configuration values for diagnostics. Secrets are masked.
    responses:
      200:
        description: Config diagnostics payload
    """
    cfg = current_app.config
    data = {
        "sqlalchemy_track_mods": cfg.get("SQLALCHEMY_TRACK_MODIFICATIONS"),
        "sqlalchemy_db_uri_set": bool(cfg.get("SQLALCHEMY_DATABASE_URI")),
        "jwt_secret_set": bool(cfg.get("JWT_SECRET")),
    }
    return jsonify(data)
