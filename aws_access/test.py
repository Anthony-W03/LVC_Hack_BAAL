from postgres_utils import sqlUtils

## First create the tables.
util = sqlUtils()
util.connect()
print(util.query(''' SELECT table_name, column_name
    FROM information_schema.columns
WHERE table_name IN (
  SELECT table_name
    FROM information_schema.tables
  WHERE table_type = 'BASE TABLE'
    AND table_schema NOT IN
        ('pg_catalog', 'information_schema')); '''))