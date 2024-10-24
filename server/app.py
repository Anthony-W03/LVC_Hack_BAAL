from flask import Flask, jsonify, request
from flask_cors import CORS
from postgres_utils import sqlUtils

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

# Get a new incremented id, per some id field.
def get_next_id(table: str, id_field: str):
    return -1

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
        current_user['password'] = results[0][5]
        is_current_user = True
        return jsonify({'vaildLogin': True, 'userID': -1})
    else:
        # There was not a valid login.
        print("Invalid Login Attempt.")
        return jsonify({'vaildLogin': False, 'userID': -1})
    
# Clear all variables. There is no current user.
def logout():
    is_current_user = False
    current_user = {'user_id':None,
                'email':None,
                'password':None,
                'fname':None,
                'lname':None,
                'username':None}
    networks = {}
    

@app.route('/api/fetch/user', methods=['GET'])
def fetch_user():
    # Fetch the current users
    if not is_current_user: 
        return jsonify('null')
    else:
        return jsonify(current_user)

## Networks
@app.route('/api/fetch/network', methods=['POST'])
def fetch_network():
    args = request.get_json()
    userID, networkID = args.values()
        
    # query all relevant connections.
    results = db.query(
        """
        SELECT *
        FROM connections
        WHERE user_id = %s
        AND network_id = %s
        """ % (current_user['user_id'], network_id)
    )
    
    # The internal network data
    network = {'nodes':[], 'links':[]}
    
    # Add the current user to the network nodes.
    network['nodes'].append({'id':current_user['user_id'], 'name':current_user['username']})
    
    # method to add new node to the network
    def add_connection(conn_id: int, name: str, target: int):
        if target <= 0: # This connection points directly at the user.
            target = current_user['user_id']
            
        # Add the node details.
        network['nodes'].append({'id':conn_id, 'name':name})
        
        # Add the link details.
        network['links'].append({'source':conn_id, 'target':target})

    # Populate the network dictionary.
    for connection in results:
        name = f"{connection['fname']} {connection['lname']}"
        add_connection(conn_id=connection['id'], name=name, target=connection['connected_through'] )
    
    # Return the json network
    return jsonify(network)

def get_next_id(table_name):
    result = db.query(
        """
        SELECT max(id) FROM %s
        """ % table_name
    )
    return result[0][0] + 1

@app.route('/api/create/network', methods=['GET'])
def create_network(name):

    new_max_id = get_next_id("networks")

    db.other_action(
        """
        INSERT INTO networks(id, name, user_id)
        VALUES (%d, %s, %d)
        """ % (new_max_id, name, current_user['user_id'])
    )
    
    return None

## Connections
@app.route('/api/fetch/connection', methods=['GET'])
def fetch_connection(user_id: int, network_id: int):
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

@app.route('/api/fetch/connection-menu', methods=['POST'])
def fetch_connections_menu():
    print(request.values)
    menu = [{'connection_id': -1, 'fname':"fname", "lname":"lname", "email":"email"},
            {'connection_id': -2, 'fname':"fname2", "lname":"lname2", "email":"email2"}]
    return jsonify(menu)

if __name__ == '__main__':
    db.connect()
    app.run(debug=True, port=5000)
    db.close() # Close the connection after the app is closed. Note: This is not ideal.
    