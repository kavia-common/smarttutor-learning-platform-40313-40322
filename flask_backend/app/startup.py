import logging
import os

log = logging.getLogger("startup")

# PUBLIC_INTERFACE
def print_startup_banner() -> None:
    """Print a concise startup banner for diagnostics."""
    db = os.getenv("DATABASE_URL", "")
    jwt = os.getenv("JWT_SECRET", "")
    log.info("SmartTutor Flask Backend starting...")
    log.info("DATABASE_URL set: %s", bool(db))
    log.info("JWT_SECRET set: %s", bool(jwt))
    log.info("PORT: %s", os.getenv("PORT", "8000"))
