from flask import Blueprint, jsonify, current_app

routes_bp = Blueprint("routes_list", __name__, url_prefix="/api")

# PUBLIC_INTERFACE
@routes_bp.get("/routes")
def list_routes():
    """
    summary: List registered routes
    description: Returns a list of routes with methods and rule strings for diagnostics.
    responses:
      200:
        description: List of routes
    """
    output = []
    for rule in current_app.url_map.iter_rules():
        methods = sorted([m for m in rule.methods if m not in {"HEAD", "OPTIONS"}])
        output.append({
            "endpoint": rule.endpoint,
            "rule": str(rule),
            "methods": methods,
        })
    output.sort(key=lambda r: r["rule"])
    return jsonify({"routes": output})
