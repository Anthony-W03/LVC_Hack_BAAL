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
        
    def query(self, cmd: str, args: list = []):
        if self.open == False: return None
        try: 
            curr = self.connection.cursor()
            curr.execute(cmd, args)
            return curr.fetchall()
        except:
            return None






