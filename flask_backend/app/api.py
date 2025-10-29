from flask import Blueprint

api = Blueprint("api", __name__, url_prefix="/api")

# PUBLIC_INTERFACE
@api.get("/")
def api_root():
    """API root that returns basic metadata for the SmartTutor backend.

    Returns:
        dict: Basic info such as name and version.
    """
    return {
        "name": "SmartTutor Flask Backend",
        "version": "0.1.0",
        "status": "ok"
    }

# PUBLIC_INTERFACE
@api.get("/ping")
def ping():
    """Simple ping endpoint.

    Returns:
        dict: Pong response.
    """
    return {"pong": True}
