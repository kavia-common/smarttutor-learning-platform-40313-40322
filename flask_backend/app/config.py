import os
from dotenv import load_dotenv

load_dotenv()

# PUBLIC_INTERFACE
def get_config() -> dict:
    """Load application configuration from environment variables.

    Returns:
        dict: Flask configuration mapping including SQLAlchemy URI and app secrets.
    """
    database_url = os.getenv("DATABASE_URL", "").strip()
    if not database_url:
        raise RuntimeError("DATABASE_URL is required. Please set it in the environment or .env file.")

    jwt_secret = os.getenv("JWT_SECRET", "").strip()
    if not jwt_secret:
        raise RuntimeError("JWT_SECRET is required. Please set it in the environment or .env file.")

    return {
        "SQLALCHEMY_DATABASE_URI": database_url,
        "SQLALCHEMY_TRACK_MODIFICATIONS": False,
        "JWT_SECRET": jwt_secret,
    }
