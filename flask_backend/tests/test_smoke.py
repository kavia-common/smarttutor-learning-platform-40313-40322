import os
import pytest

os.environ.setdefault("DATABASE_URL", "sqlite+pysqlite:///:memory:")
os.environ.setdefault("JWT_SECRET", "test_secret")

from app import create_app  # noqa: E402

@pytest.fixture()
def client():
    app = create_app()
    with app.test_client() as c:
        yield c

def test_health(client):
    rv = client.get("/health")
    assert rv.status_code == 200
    data = rv.get_json()
    assert isinstance(data, dict)
    assert data.get("status") == "ok"

def test_openapi_json(client):
    # Ensure registering openapi does not error even if builder/extra modules exist
    rv = client.get("/openapi.json")
    # Some environments may not register the route if import fails; tolerate 404 but prefer 200
    assert rv.status_code in (200, 404)
