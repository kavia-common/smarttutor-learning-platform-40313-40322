-- Quick setup for local Postgres
-- psql -U postgres -f scripts/create_local_db.sql
DO
$$
BEGIN
   IF NOT EXISTS (
      SELECT FROM pg_catalog.pg_roles WHERE rolname = 'smarttutor'
   ) THEN
      CREATE ROLE smarttutor LOGIN PASSWORD 'smarttutor';
   END IF;
END
$$;

CREATE DATABASE smarttutor OWNER smarttutor;
GRANT ALL PRIVILEGES ON DATABASE smarttutor TO smarttutor;
