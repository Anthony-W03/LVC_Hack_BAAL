from postgres_utils import sqlUtils
from dataclasses import dataclass, asdict
from typeing import List

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
        
    nodes: List[node]
    links: List[link]
    
    def dict(self):
        return {'nodes': [],
                'links': []}
    

@dataclass
class user:
    user_id: int
    email: str
    password: str
    fname: str
    lname: str
    username: str
    
    def fullname(self) -> str:
        return f"{self.fname} {self.lname}"
    
    
@dataclass
class connection:
    pass