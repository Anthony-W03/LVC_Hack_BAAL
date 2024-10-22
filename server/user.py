from postgres_utils import sqlUtils
from dataclasses import dataclass, asdict
from typeing import List
from db_access import DatabaseAccessor

@dataclass
class network:  
    """
    A data class representing a network consisting of nodes and links between them.

    The class allows adding nodes and links and provides a dictionary 
    representation of the network.

    Attributes:
        nodes (List[network.node]): A list of nodes in the network.
        links (List[network.link]): A list of links (edges) between nodes.
    """
    
    @dataclass
    class node:
        """
        Represents a node in the network.
        
        Attributes:
            node_id (int): The unique identifier of the node.
            name (str): The name of the node.
        """
        node_id: int # Can't have id variable where id function exist. At least it's bad practice.
        name: str
        
        def dict(self):
            """Returns a dictionary representation of the node."""
            return {'id': self.node_id, 'name': self.name}
        
    @dataclass
    class link:
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
    nodes: List[node] = []
    links: List[link] = []
    
    def add_node(self, node_id: int, name: str):
        """
        Adds a node to the network.

        Args:
            node_id (int): The ID of the node.
            name (str): The name of the node.
        """
        self.nodes.append(self.node(node_id, name))
    
    def add_link(self, source: int, target: int):
        """
        Adds a link between two nodes.

        Args:
            source (int): The ID of the source node.
            target (int): The ID of the target node.
        """
        self.nodes.append(self.link(source, target))
    
    def dict(self):
        """
        Returns a dictionary representation of the network, with nodes 
        and links converted to dictionaries.

        Returns:
            dict: A dictionary containing the nodes and links of the network.
        """
        return {'nodes': [dict(node) for node in self.nodes],
                'links': [dict(link) for link in self.links]}
    
@dataclass
class user:
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
        update(query: str, args: list = []) -> None: Updates data in the database.
    """

    # FETCH FROM DATABASE
    def fetch(self, query: str, args: tuple = ()) -> list:
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
    def update(self, query: str, args: tuple = ()) -> None:
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
        super().__init__() # This is really not necessary, but why not.
        self.user = None
        self.network = {} # Network objects, indexed by the network ID.
        
    # Login Functionality
    def is_logged_in(self) -> bool:
        """
        Returns a boolean indicating whether there is a user connected 
        to this profile object.

        Returns:
            bool: True if a user is logged in, False otherwise.
        """
        return self.user is not None
    
    def login(self):
        pass
    
    def logout():
        pass
    
    