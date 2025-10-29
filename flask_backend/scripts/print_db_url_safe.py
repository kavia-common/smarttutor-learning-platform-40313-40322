#!/usr/bin/env python
"""
Print a redacted DATABASE_URL summary (scheme, host, port, db name).
"""
import os
from urllib.parse import urlparse

def redact(url: str) -> dict:
    p = urlparse(url)
    # Handle cases like postgresql+psycopg
    scheme = p.scheme
    # netloc may include credentials; strip user:pass@
    host = p.hostname or ""
    port = p.port
    db = p.path.lstrip("/") if p.path else ""
    return {
        "scheme": scheme,
        "host": host,
        "port": port,
        "database": db,
        "has_credentials": bool(p.username),
        "ssl": ("sslmode=" in (p.query or "")) or ("ssl" in (p.query or "")),
    }

def main() -> int:
    url = os.getenv("DATABASE_URL", "")
    if not url:
        print("DATABASE_URL not set")
        return 1
    info = redact(url)
    print(info)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
