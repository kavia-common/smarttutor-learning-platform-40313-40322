import os
from dataclasses import dataclass


# PUBLIC_INTERFACE
def get_env(name: str, default: str | None = None) -> str:
    """Retrieve an environment variable or default value.

    Args:
        name: The name of the environment variable.
        default: Default value to use if not set.

    Returns:
        The environment variable value or the provided default.

    Raises:
        RuntimeError: If the variable is not set and no default provided.
    """
    value = os.getenv(name, default)
    if value is None:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


@dataclass
class Config:
    """Base configuration loaded from environment variables."""
    SQLALCHEMY_DATABASE_URI: str = get_env("DATABASE_URL", "sqlite:///smarttutor.db")
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    JWT_SECRET: str = get_env("JWT_SECRET", "dev_only_secret_change_me")
    ENV: str = os.getenv("FLASK_ENV", "development")
    DEBUG: bool = os.getenv("FLASK_DEBUG", "1") == "1"
