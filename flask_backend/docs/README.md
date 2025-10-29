# Backend Docs

- openapi.html: Redoc-based viewer for the SmartTutor API (loads openapi.json in the same folder)
- openapi.json: Generated OpenAPI specification file (run scripts/generate_openapi_site.py to create)

Quick usage:
- Generate: python scripts/generate_openapi_site.py
- Serve locally: python scripts/serve_docs.py
- Open: http://localhost:8080/openapi.html
