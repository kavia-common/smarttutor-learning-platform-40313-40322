from flask import Blueprint, Response, jsonify
from .openapi import openapi_spec

openapi_dl_bp = Blueprint("openapi_download", __name__)

# PUBLIC_INTERFACE
@openapi_dl_bp.get("/openapi/download")
def openapi_download() -> Response:
    """Serve the OpenAPI JSON as an attachment for download tools."""
    spec_resp = openapi_spec()
    # Ensure we have a proper JSON body from the existing handler
    return Response(
        response=spec_resp.get_data(),
        status=200,
        mimetype="application/json",
        headers={"Content-Disposition": "attachment; filename=smarttutor_openapi.json"}
    )
