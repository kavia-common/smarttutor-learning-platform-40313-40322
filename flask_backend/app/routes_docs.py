import os
from pathlib import Path
from flask import Blueprint, send_from_directory, abort

docs_bp = Blueprint("docs", __name__, url_prefix="/docs")

# PUBLIC_INTERFACE
@docs_bp.get("/openapi.html")
def serve_openapi_html():
    """Serve the Redoc-based OpenAPI viewer HTML from the docs folder."""
    docs_dir = Path(__file__).resolve().parent.parent / "docs"
    html_path = docs_dir / "openapi.html"
    if not html_path.exists():
        abort(404, "openapi.html not found. Run scripts/generate_openapi_site.py or commit docs first.")
    return send_from_directory(docs_dir.as_posix(), "openapi.html")
