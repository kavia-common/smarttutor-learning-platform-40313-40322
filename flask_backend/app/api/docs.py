"""
Docs helper blueprint to expose a friendly link to download the OpenAPI JSON.
"""
from __future__ import annotations

from flask import Blueprint, jsonify, current_app

docs_bp = Blueprint("docs", __name__, url_prefix="/docs")


# PUBLIC_INTERFACE
@docs_bp.get("/openapi")
def get_openapi_location():
    """
    Returns the location of the OpenAPI document.
    """
    return jsonify({"openapi_url": "/openapi.json"})
