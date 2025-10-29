import os
from dotenv import load_dotenv

load_dotenv()
os.environ.setdefault("DATABASE_URL", "sqlite:///:memory:")
os.environ.setdefault("JWT_SECRET", "test_secret")

def test_health_and_status_endpoints():
    from app import create_app
    app = create_app()
    client = app.test_client()

    # Health
    r = client.get("/health")
    assert r.status_code == 200
    data = r.get_json()
    assert isinstance(data, dict)
    assert data.get("status") == "ok"

    # Status
    r2 = client.get("/api/status")
    assert r2.status_code == 200
    data2 = r2.get_json()
    assert isinstance(data2, dict)
    assert data2.get("ok") is True
    assert "name" in data2 and "version" in data2
