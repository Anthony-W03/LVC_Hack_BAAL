from postgres_utils import sqlUtils
from dataclasses import dataclass, asdict
from typeing import List
from db_access import GlobalDatabasePool, DatabaseAccessor

@dataclass
class network:  
    @dataclass
    class node:
        node_id: int # Can't have id variable where id function exist. At least it's bad practice.
        name: str
        
        def dict(self):
            return {'id': self.node_id, 'name': self.name}
        
    @dataclass
    class link:
        source: int
        target: int
        
        def dict(self):
            return {k: str(v) for k, v in asdict(self).items()}
        
    nodes: List[node] = []
    links: List[link] = []
    
    def add_node(self, node_id: int, name: str):
        self.nodes.append(self.node(node_id, name))
    
    def add_link(self, source: int, target: int):
        self.nodes.append(self.link(source, target))
    
    def dict(self):
        return {'nodes': [dict(node) for node in self.nodes],
                'links': [dict(link) for link in self.links]}
    
@dataclass
class user:
    # Personal Details.
    user_id: int
    email: str
    password: str
    fname: str
    lname: str
    username: str
    
    def fullname(self) -> str:
        return f"{self.fname} {self.lname}"

class User(DatabaseAccessor):
    def __init__(self):
        self.user = None
        self.networks = {}
    
    def login() -> bool:
        pass
    
    # FETCH DATA
    
    # UPDATE DATA
    
    # ADD DATA
    
    