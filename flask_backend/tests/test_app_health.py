import os
from dotenv import load_dotenv

# Load env variables for testing; if not present, set minimal defaults
load_dotenv()
os.environ.setdefault("DATABASE_URL", "sqlite:///:memory:")
os.environ.setdefault("JWT_SECRET", "test_secret")

def test_health_endpoint():
    from app import create_app
    app = create_app()
    client = app.test_client()
    res = client.get("/health")
    assert res.status_code == 200
    data = res.get_json()
    assert data.get("status") == "ok"
