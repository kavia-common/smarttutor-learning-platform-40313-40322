from flask import Blueprint, current_app, jsonify

introspection_bp = Blueprint("introspection", __name__, url_prefix="/api/diag")

# PUBLIC_INTERFACE
@introspection_bp.get("/routes")
def list_routes():
    """List registered Flask routes (rule, methods, endpoint)."""
    output = []
    for rule in sorted(current_app.url_map.iter_rules(), key=lambda r: r.rule):
        if rule.endpoint == 'static':
            continue
        output.append({
            "rule": rule.rule,
            "methods": sorted(m for m in rule.methods if m not in ("HEAD", "OPTIONS")),
            "endpoint": rule.endpoint
        })
    return jsonify(output)
