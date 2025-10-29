#!/usr/bin/env python
import json
from app.config import get_config

def main():
    cfg = get_config().copy()
    # Redact secrets
    if "JWT_SECRET" in cfg:
        cfg["JWT_SECRET"] = "***redacted***"
    print(json.dumps(cfg, indent=2))

if __name__ == "__main__":
    main()
