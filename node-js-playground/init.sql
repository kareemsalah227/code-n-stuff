-- CREATE DATABASE forms_db;

\connect forms_db;

CREATE TABLE IF NOT EXISTS forms (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  preference TEXT CHECK (preference IN ('red', 'blue')) NOT NULL
);