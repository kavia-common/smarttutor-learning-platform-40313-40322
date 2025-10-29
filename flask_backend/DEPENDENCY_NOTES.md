Dependency Notes

- Requirements are pinned in requirements.txt.
- For deterministic builds across environments consider using pip-tools:
  pip install pip-tools
  pip-compile --generate-hashes -o requirements.txt pyproject.toml  # if a pyproject is added later
- PostgreSQL driver used: psycopg[binary] for convenience; for Alpine or constrained envs you may prefer psycopg (source build) with libpq.
