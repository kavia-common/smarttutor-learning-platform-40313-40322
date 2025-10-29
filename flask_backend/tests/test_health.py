import os
import pytest

os.environ.setdefault("DATABASE_URL", "postgresql+psycopg://postgres:postgres@localhost:5432/smarttutor")
os.environ.setdefault("JWT_SECRET", "test_secret")

from app import create_app  # noqa: E402

@pytest.fixture()
def client():
    app = create_app()
    with app.test_client() as c:
        yield c

def test_health_ok(client):
    rv = client.get("/health")
    assert rv.status_code == 200
    data = rv.get_json()
    assert isinstance(data, dict)
    assert data.get("status") == "ok"
