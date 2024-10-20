from flask import Flask, jsonify, request
from flask_cors import CORS
from postgres_utils import sqlUtils
from dataclasses import dataclass
from psycopg2 import sql

# Create our internal App.
app = Flask(__name__)
CORS(app)  # This allows CORS for all domains on all routes

# Create database interaction utils.
db = sqlUtils()

# Set some important variables.
is_current_user = False
current_user = {'user_id':None,
                'email':None,
                'password':None,
                'fname':None,
                'lname':None,
                'username':None}
networks = {}

def build_user_networks():
    pass

## User
@app.route('/api/validate/login', methods=['GET'])
def validate_login(email: str, password: str):
    cmd = """
            SELECT *
            FROM useraccounts
            WHERE email = '%s'
            AND password = '%s';
            """ % (email, password)
    results = db.query(cmd)
    if len(results) == 1:
        # for current_users
        current_user['user_id'] = results[0][0]
        current_user['username'] = results[0][1]
        current_user['fname'] = results[0][2]
        current_user['lname'] = results[0][3]
        current_user['email'] = results[0][4]
        current_user['password'] = results[0][0]
        

        return jsonify({'vaildLogin': True, 'userID': -1})
    else:
        # There was not a valid login.
        print("Invalid Login Attempt.")
        return jsonify({'vaildLogin': False, 'userID': -1})
        

@app.route('/api/fetch/user', methods=['GET'])
def fetch_user(user_id: int):
    # Create a user object. (If the user exists)
    user = User(user_id)
    
    # Does the user exist.
    if not user.exists(): 
        return None
    
    # Get the users info.
    ## We assume this includes: fname, lname, email, and id.
    info = user.get_personal_info()
    
    # Get the user info.
    user_data = {
        'id': info.id,
        'fname': info.fname,
        'lname': info.lname,
        'email': info.email
    }
    
    # Return as a json object.
    return jsonify(user_data)

## Networks
@app.route('/api/fetch/network', methods=['GET'])
def fetch_network(network_id):
    
    pickling = db.query(
        """
        SELECT *
        FROM connections
        WHERE user_id = %d
        AND network_id = %d
        """ % (current_user['user_id'])
    )
    
    network = {
    'nodes': [
      { 'id': 'You', 'name': 'You' },
      { 'id': 'Alice', 'name': 'Alice' },
      { 'id': 'Bob', 'name': 'Bob' },
      { 'id': 'Charlie', 'name': 'Charlie' },
    ],
    'links': [
      { 'source': 'You', 'target': 'Alice' },
      { 'source': 'You', 'target': 'Bob' },
      { 'source': 'Alice', 'target': 'Charlie' },
    ]}
    return jsonify(network)

@app.route('/api/create/network', methods=['GET'])
def create_network(name):
    return None

## Connections
@app.route('/api/fetch/connection', methods=['GET'])
def fetch_connection(connID: int):
    return None

@app.route('/api/update/connection', methods=['GET'])
def update_connection():
    return None

@app.route('/api/create/connection', methods=['GET'])
def create_connection():
    return None

@app.route('/api/graph', methods=['GET'])
def get_graph_data(user_id: int, network_id: int):
    return None

@app.route('/fetch/connection-menu', methods=['GET'])
def fetch_connections_menu(user_id: int, network_id: int):
    menu = [{'connection_id': -1, 'fname':"fname", "lname":"lname", "email":"email"},
            {'connection_id': -2, 'fname':"fname2", "lname":"lname2", "email":"email2"}]
    return jsonify(menu)

if __name__ == '__main__':
    db.connect()
    app.run(debug=True)
    db.close() # Close the connection after the app is closed. Note: This is not ideal.
    