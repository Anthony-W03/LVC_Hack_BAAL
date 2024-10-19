import psycopg2
import boto3, os, time
from dotenv import load_dotenv, dotenv_values 

# loading variables from .env file
load_dotenv() 

conn = psycopg2.connect(database=os.getenv('DB_DATABASE'),
                        host=os.getenv('DB_URL'),
                        user=os.getenv('DB_USERNAME'),
                        password=os.getenv('DB_PASSWORD'),
                        port=os.getenv('DB_PORT'))
print(conn)

cursor = conn.cursor()
cursor.execute("SELECT version();")
db_version = cursor.fetchone()
print(f"Connected to PostgreSQL database, version: {db_version}")

