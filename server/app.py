from flask import Flask, jsonify, request
from flask_cors import CORS
from interact import User, Network

app = Flask(__name__)
CORS(app)  # This allows CORS for all domains on all routes

## User
@app.route('/api/validate/login', methods=['GET'])
@app.route('/api/fetch/user', methods=['GET'])

## Networks
@app.route('/api/fetch/network', methods=['GET'])
@app.route('/api/create/network', methods=['GET'])

## Connections
@app.route('/api/fetch/connection', methods=['GET'])
@app.route('/api/update/connection', methods=['GET'])
@app.route('/api/create/connection', methods=['GET'])

#####
########
@app.route('/api/node/<node_id>', methods=['GET'])
def get_user_info(user_id: int):
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


@app.route('/api/graph', methods=['GET'])
def get_graph_data(user_id: int, network_id: int):
    # Create a user object. (If the user exists)
    user = User(user_id)    
    if not user.exists(): # Does the user exist.
        return None
    
    # Create the network object. (If the network exists)
    net = Network(user_id, network_id)    
    if not net.exists(): # Does the user exist.
        return None
    
    # Query and Init the network. Return the graph/adjacency list.
    net.init_network()
    return jsonify(net.network)

if __name__ == '__main__':
    app.run(debug=True)