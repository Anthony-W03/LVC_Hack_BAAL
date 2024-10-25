from postgres_utils import sqlUtils
from dataclasses import dataclass, asdict
from typeing import List
from server.database_access.DatabaseAccess import DatabaseAccessor


@dataclass
class Network:
    """
    A data class representing a network consisting of nodes and links between them.

    The class allows adding nodes and links and provides a dictionary
    representation of the network.

    Attributes:
        nodes (List[network.node]): A list of nodes in the network.
        links (List[network.link]): A list of links (edges) between nodes.
    """

    @dataclass
    class Node:
        """
        Represents a node in the network.

        Attributes:
            node_id (int): The unique identifier of the node.
            name (str): The name of the node.
        """

        node_id: int  # Can't have id variable where id function exist. At least it's bad practice.
        name: str

        def dict(self):
            """Returns a dictionary representation of the node."""
            return {"id": self.node_id, "name": self.name}

    @dataclass
    class Link:
        """
        Represents a link between two nodes in the network.

        Attributes:
            source (int): The ID of the source node.
            target (int): The ID of the target node.
        """

        source: int
        target: int

        def dict(self):
            """Returns a dictionary representation of the link."""
            return {k: str(v) for k, v in asdict(self).items()}

    # Members for the network class
    nodes: List[Node] = []
    links: List[Link] = []

    def add_node(self, node_id: int, name: str):
        """
        Adds a node to the network.

        Args:
            node_id (int): The ID of the node.
            name (str): The name of the node.
        """
        self.nodes.append(self.Node(node_id, name))

    def add_link(self, source: int, target: int):
        """
        Adds a link between two nodes.

        Args:
            source (int): The ID of the source node.
            target (int): The ID of the target node.
        """
        self.nodes.append(self.Link(source, target))

    def dict(self):
        """
        Returns a dictionary representation of the network, with nodes
        and links converted to dictionaries.

        Returns:
            dict: A dictionary containing the nodes and links of the network.
        """
        return {
            "nodes": [dict(node) for node in self.nodes],
            "links": [dict(link) for link in self.links],
        }
        
@dataclass
class Connection:
    connection_id: int
    user_id: int
    network_id: int
    fname: str
    lname: str
    connection_through: int
    linkedin: str
    website: str
    email: str
    phone: str
    address: str
    employment: str


@dataclass
class User:
    """
    A data class representing a user with personal details.

    Attributes:
        user_id (int): The unique identifier for the user.
        email (str): The user's email address.
        password (str): The user's password.
        fname (str): The user's first name.
        lname (str): The user's last name.
        username (str): The user's username.
    """

    # Personal Details.
    user_id: int
    email: str
    password: str
    fname: str
    lname: str
    username: str

    def fullname(self) -> str:
        """Returns the full name of the user."""
        return f"{self.fname} {self.lname}"


class UserInteract(DatabaseAccessor):
    """
    A class that extends DatabaseAccessor to interact with user-related data
    in the database. Provides methods for fetching and updating database entries.

    Methods:
        fetch(query: str, args: tuple = ()) -> list: Fetches data from the database.
        update(query: str, args: tuple = ()) -> None: Updates data in the database.
    """

    # FETCH FROM DATABASE
    def fetch_database(self, query: str, args: tuple = ()) -> list:
        """
        Fetches data from the database based on a SQL query.

        Args:
            query (str): The SQL query to be executed.
            args (tuple, optional): The arguments to be passed to the query.

        Returns:
            list: The result of the query execution as a list of records.
        """
        with self.get_cursor as cursor:
            cursor.execute(query, args)
            results = cursor.fetchall()
            return results

    # UPDATE DATABASE
    def update_database(self, query: str, args: tuple = ()) -> None:
        """
        Updates the database using the provided SQL query.

        Args:
            query (str): The SQL query to be executed.
            args (tuple, optional): The arguments to be passed to the query.
        """
        with self.get_cursor as cursor:
            cursor.execute(query, args)
            return


class Profile(UserInteract):
    """
    A class that extends UserInteract to handle user profile management.

    Attributes:
        user (user): The user object for the currently logged-in user.
        network (dict): A dictionary of network objects indexed by network ID.

    Methods:
        is_logged_in() -> bool: Checks if a user is logged in.
        login(): Logs the user in (not implemented).
        logout(): Logs the user out (not implemented).
    """

    def __init__(self):
        super().__init__()  # This is really not necessary, but why not.
        self.user = None
        self.networks = {}  # Network objects, indexed by the network ID.

    # Login Functionality
    def is_logged_in(self) -> bool:
        """
        Returns a boolean indicating whether there is a user connected
        to this profile object.

        Returns:
            bool: True if a user is logged in, False otherwise.
        """
        return self.user is not None

    def login(self, email: str, password: str) -> bool:
        cmd = """
            SELECT *
            FROM useraccounts
            WHERE email = '%s'
            AND password = '%s';
            """ % (
            email,
            password,
        )
        results = self.fetch_database(cmd)
        if len(results) == 1:
            self.user = User(
                results[0][0],
                results[0][4],
                results[0][5],
                results[0][2],
                results[0][3],
                results[0][1],
            )
            return True
        else:
            return False

    def logout(self):
        self.user = None
        
    def fetch_network(self, network_id: int) -> dict:
        if network_id in self.networks.keys():
            return dict(self.networks[network_id])
        else:
            results = self.fetch_database(
                """
                SELECT *
                FROM connections
                WHERE user_id = %s
                AND network_id = %s
                """ % (self.user.user_id, network_id)
            )
            
            # The internal network data
            network = Network()
            network.add_node(self.user.user_id, self.user.username) # Add self.
            for connection in results:
                name = f"{connection['fname']} {connection['lname']}"
                target = connection['connected_through']
                if target <= 0: # This connection points directly at the user.
                    target = self.user.user_id
                    
                # Add the node details and link details
                network.add_node(connection['id'], name)
                network.add_link(connection['id'], target)

            # Add the new network to the local dictionary
            self.networks[network_id] = network
            
            # return the new network.
            return dict(network)
    
    def new_network(self) -> int:
        new_id = self.get_next_id('networks')
        self.networks[new_id] = Network()
        return new_id
    
    def update_network(self):
        pass
    
    def fetch_connection(self, connection_id: int):
        results = self.fetch_database(
                """
                SELECT *
                FROM connections
                WHERE id = %s
                """ % (connection_id)
            )
        
    
    def new_connection(self, network_id: int, connection_id: int):
        new_id = self.get_next_id('connections')
    
    def update_connection(self, network_id: int, connection_id: int):
        pass