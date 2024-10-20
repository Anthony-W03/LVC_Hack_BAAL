import psycopg2
import boto3, os, time
from dotenv import load_dotenv, dotenv_values 

# loading variables from .env file
load_dotenv() 

class sqlUtils():
    def __init__(self):
        self.config = {
            "database":os.getenv('DB_DATABASE'),
            "host":os.getenv('DB_URL'),
            "user":os.getenv('DB_USERNAME'),
            "password":os.getenv('DB_PASSWORD'),
            "port":os.getenv('DB_PORT')
        }
        self.open = False
        self.connection = None
        
    def connect(self):
        try:
            self.connection = psycopg2.connect(**self.config)
            self.connection.autocommit = True
            self.open = True
            print(f"Database connection opened successfully.")
        except:
            self.open = False
            print("Database not connected successfully.")
            
    def close(self):
        if self.open == True:
            self.connection.close()
            self.connection = None
            self.open = False
        else: return    
        
    def query(self, cmd: str):
        if self.open == False: return None
        try: 
            curr = self.connection.cursor()
            curr.execute(cmd)
            return curr.fetchall()
        except:
            return None
        

db = sqlUtils()
db.connect()

'''
test1 = db.query(
"""
CREATE TABLE useraccounts (
    id INT PRIMARY KEY,
    username VARCHAR(255),
    fname VARCHAR(255),
    lname VARCHAR(255),
    email VARCHAR(255),
    password VARCHAR(255)
);
"""
)
print(test1)

test2 = db.query(
"""
CREATE TABLE networks (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES useraccounts(id)
);
"""
)
print(test2)


test2 = db.query(
"""
CREATE TABLE connections (
    id INT PRIMARY KEY,
    user_id INT,
    network_id INT,
    fname VARCHAR(255),
    lname VARCHAR(255),
    connection_through INT,
    linkedin VARCHAR(255),
    website VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(255),
    address VARCHAR(255),
    employment VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES useraccounts(id),
    FOREIGN KEY (network_id) REFERENCES networks(id)
);

"""
)
print(test2)
'''


test3 = db.query(
"""
SELECT table_name, column_name
    FROM information_schema.columns
WHERE table_name IN (
  SELECT table_name
    FROM information_schema.tables
  WHERE table_type = 'BASE TABLE'
    AND table_schema NOT IN
        ('pg_catalog', 'information_schema'));
"""
)
print(test3)






