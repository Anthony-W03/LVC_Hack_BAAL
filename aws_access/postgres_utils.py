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
        except psycopg2.OperationalError as e:
            print('Unable to connect!\n{0}').format(e)
            return None

    def copy(self, cmd:str, filepath: str):
        if self.open == False: return None
        try:
            curr = self.connection.cursor()
            curr.copy_expert(cmd, open(filepath, "r"))
            return 0
        except psycopg2.OperationalError as e:
            print('Unable to connect!\n{0}').format(e)
            return None
        

db = sqlUtils()
db.connect()

'''
db.query(
    """
    DROP TABLE useraccounts CASCADE;
    """
)

test1 = db.query(
"""
CREATE TABLE useraccounts (
    id INT PRIMARY KEY,
    username VARCHAR(255),
    fname VARCHAR(255),
    lname VARCHAR(255),
    email VARCHAR(255) NOT NULL UNIQUE,
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


'''
test = db.copy(
"""
COPY useraccounts(id, username, fname, lname, email, password)
FROM STDIN
DELIMITER ','
CSV;
""",
"../Data/Users.csv"
)
print(test)


test = db.copy(
"""
COPY networks(id, name, user_id)
FROM STDIN
DELIMITER ','
CSV;
""",
"../Data/Networks.csv"
)
print(test)
'''



'''
db.query(
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
'''

'''
db.copy(
"""
COPY connections(id,
    user_id,
    network_id,
    fname,
    lname,
    connection_through,
    linkedin,
    website,
    email,
    phone,
    address,
    employment)
FROM STDIN
DELIMITER ','
CSV;
""",
"../Data/Connections.csv"
)
'''

'''
test4 = db.query(
"""
SELECT * FROM networks;
"""
)
print(test4)

test4 = db.query(
"""
SELECT * FROM useraccounts;
"""
)
print(test4)

test4 = db.query(
"""
SELECT * FROM connections;
"""
)
print(test4)
'''

username = 'John_Doe'
password = 'pw1'
pickling = db.query(
"""
SELECT *
FROM useraccounts
WHERE username = '%s'
AND password = '%s';
""" % (username, password)
)
print(pickling[0][0])
pickler = pickling[0][0]

idno = pickler
test = db.query(
"""
SELECT *
FROM useraccounts
WHERE id = %d
""" % idno
)
print(test)

idno = pickler
test = db.query(
"""
SELECT *
FROM networks
WHERE user_id = %d
""" % idno
)
print(test)

idno = '12345'
test = db.query(
"""
SELECT *
FROM connections
WHERE user_id = '%s'
""" % idno
)
print(test)

