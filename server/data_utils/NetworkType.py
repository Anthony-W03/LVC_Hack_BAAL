from typing import List
from dataclasses import dataclass

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