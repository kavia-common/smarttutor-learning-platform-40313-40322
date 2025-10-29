API Docs Publishing

Generate OpenAPI file (without running server):
  python scripts/write_openapi_file.py
  # Outputs: openapi.json in flask_backend/

Use with:
- Swagger Editor (https://editor.swagger.io/)
- Redocly (CLI), Redoc (static HTML)
- Stoplight, Postman (import OpenAPI)

Optional: Commit openapi.json for CI/CD pipelines that publish API docs.
