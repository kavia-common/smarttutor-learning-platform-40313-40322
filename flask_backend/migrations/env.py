from __future__ import annotations

import os
import sys
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context

# Ensure app is on path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

# Load .env
from dotenv import load_dotenv
load_dotenv()

# Alembic Config object
config = context.config

# Interpret the config file for Python logging.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Import app and models to get metadata
from app import create_app  # noqa: E402
from app.db import db  # noqa: E402
from app.models import (  # noqa: E402
    user, course, lesson, enrollment, chat_message,
    whiteboard_session, whiteboard_event, payment, recommendations_cache
)

target_metadata = db.Model.metadata

def get_url():
    return os.getenv("DATABASE_URL")

def run_migrations_offline():
    url = get_url()
    if not url:
        raise RuntimeError("DATABASE_URL not set for alembic offline migration.")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    url = get_url()
    if not url:
        raise RuntimeError("DATABASE_URL not set for alembic online migration.")
    configuration = config.get_section(config.config_ini_section)
    configuration["sqlalchemy.url"] = url

    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
