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
current_user = {
    "user_id": None,
    "email": None,
    "password": None,
    "fname": None,
    "lname": None,
    "username": None,
}


## USERS
@app.route("/api/validate/login", methods=["POST"])
def validate_login():
    args = request.get_json()
    (
        email,
        password,
    ) = args.values()


@app.route("/api/fetch/user", methods=["POST"])
def fetch_user():
    args = request.get_json()
    (userID,) = args.values()


## Networks
@app.route("/api/fetch/network", methods=["POST"])
def fetch_network():
    args = request.get_json()
    (
        userID,
        networkID,
    ) = args.values()

    dummy_network = {
        "nodes": [
            {"id": "You", "name": "You"},
            {"id": "Alice", "name": "Alice"},
            {"id": "Bob", "name": "Bob"},
            {"id": "Charlie", "name": "Charlie"},
        ],
        "links": [
            {"source": "You", "target": "Alice"},
            {"source": "You", "target": "Bob"},
            {"source": "Alice", "target": "Charlie"},
        ],
    }
    return jsonify(dummy_network)


@app.route("/api/create/network", methods=["POST"])
def create_network():
    args = request.get_json()
    (userID,) = args.values()


## Connections
@app.route("/api/fetch/connection", methods=["POST"])
def fetch_connection():
    args = request.get_json()
    (
        userID,
        connectionID,
    ) = args.values()


@app.route("/api/update/connection", methods=["POST"])
def update_connection():
    args = request.get_json()
    (
        userID,
        connectionID,
        networkID,
    ) = args.values()


@app.route("/api/create/connection", methods=["POST"])
def create_connection():
    args = request.get_json()
    (
        userID,
        networkID,
        email,
        fname,
        lname,
        source,
        target,
    ) = args.values()


@app.route("/api/fetch/connection-menu", methods=["POST"])
def fetch_connections_menu():
    args = request.get_json()
    (
        userID,
        networkID,
        connectionID,
    ) = args.values()

    menu = [
        {"connection_id": -1, "fname": "fname", "lname": "lname", "email": "email"},
        {"connection_id": -2, "fname": "fname2", "lname": "lname2", "email": "email2"},
    ]
    return jsonify(menu)


if __name__ == "__main__":
    db.connect()
    app.run(debug=True, port=5000)
    db.close()  # Close the connection after the app is closed. Note: This is not ideal.
