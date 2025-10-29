API Examples

Two quick ways to exercise the backend manually:

1) VS Code REST Client
- Open api_examples.http
- Install the "REST Client" extension
- Click "Send Request" above any request

2) Postman
- Import postman/SmartTutor_Backend.postman_collection.json
- Set base_url to http://localhost:8000
- Send requests to the endpoints

Endpoints to try first:
- GET /health
- GET /api/status
- GET /openapi.json
- GET /api/diag/routes
- GET /api/ws-help
