#!/usr/bin/env python
"""
Validate presence of required environment keys in backend and frontend .env files.
This helps CI fail-fast when configuration is missing.
"""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
BACKEND = ROOT / "smarttutor-learning-platform-40313-40322" / "flask_backend"
FRONTEND = ROOT / "smarttutor-learning-platform-40313-40322" / "react_frontend"

REQUIRED_BACKEND = ["DATABASE_URL", "JWT_SECRET"]
REQUIRED_FRONTEND = ["VITE_API_BASE_URL", "VITE_WS_BASE_URL"]

def read_env(path: Path) -> dict:
  vals = {}
  try:
    for line in path.read_text(encoding="utf-8").splitlines():
      line = line.strip()
      if not line or line.startswith("#"): continue
      if "=" in line:
        k, v = line.split("=", 1)
        vals[k.strip()] = v.strip()
  except FileNotFoundError:
    pass
  return vals

def main() -> int:
  ok = True

  backend_env = BACKEND / ".env"
  b_vals = read_env(backend_env)
  for key in REQUIRED_BACKEND:
    if not b_vals.get(key):
      print(f"Backend .env missing {key} at {backend_env}", file=sys.stderr)
      ok = False

  frontend_env = FRONTEND / ".env"
  f_vals = read_env(frontend_env)
  for key in REQUIRED_FRONTEND:
    if not f_vals.get(key):
      print(f"Frontend .env missing {key} at {frontend_env}", file=sys.stderr)
      ok = False

  return 0 if ok else 1

if __name__ == "__main__":
  raise SystemExit(main())
