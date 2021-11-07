login Steps:
psql -d mydb -U myuser

psql -h myhost -d mydb -U myuser


Create database & new database user:

sam=# CREATE DATABASE newproject;
sam=# CREATE USER newprojectadminuser WITH PASSWORD 'adminpassword';
sam=# ALTER ROLE newprojectadminuser SET client_encoding TO 'utf8';
sam=# ALTER ROLE newprojectadminuser SET default_transaction_isolation TO 'read committed';
sam=# ALTER ROLE newprojectadminuser SET timezone TO 'UTC';
sam=# GRANT ALL PRIVILEGES ON DATABASE newproject TO newprojectadminuser;


connect to a db:

\c dbname

list tables

\dt
\d table_name


Copy from CSV to table

\copy table_name FROM '[Path to CSV file]' WITH DELIMITER ',' CSV HEADER;


create new role:
CREATE ROLE testuser WITH LOGIN PASSWORD 'password';
ALTER ROLE testuser WITH CREATEDB;
