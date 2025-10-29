from __future__ import annotations

from contextlib import contextmanager
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, scoped_session, sessionmaker

from .config import Config


class Base(DeclarativeBase):
    """Base class for all SQLAlchemy ORM models."""


# Create engine; future=True is default in SQLAlchemy 2.x
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)

# Thread-local scoped session for Flask apps
SessionLocal = scoped_session(
    sessionmaker(bind=engine, autoflush=False, autocommit=False, expire_on_commit=False)
)


# PUBLIC_INTERFACE
@contextmanager
def get_session() -> Generator:
    """Context manager that yields a database session and ensures cleanup."""
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:  # noqa: BLE001
        session.rollback()
        raise
    finally:
        session.close()
