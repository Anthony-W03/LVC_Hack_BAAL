import itertools, uuid, re
from typing import (Optional, 
                    Tuple, 
                    Self)
from pathlib import Path

class UniqueID:
    _class_counters = {}

    def __init__(self):
        cls = self.__class__
        if cls not in UniqueID._class_counters:
            UniqueID._class_counters[cls] = uuid.uuid4()
        self.id = UniqueID._class_counters[cls]
        UniqueID._class_counters[cls] = uuid.uuid4()

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.id})"
    
    @property
    def str_id(self):
        return str(self.id)
    
class user():
    def __init__(self, id: int):
        self.id = id
        self.connections = {}
        
    def get_personal_info(self):
        pass
        
    def get_connections(self, network: int):
        pass
    
    def add_connection(self, network: int):
        pass
    

class network():
    def __init__(self, user_id: int, network_id: int):
        self.user_id = user_id
        self.netork_id = network_id
        self.network = {}
        
    def init_network(self):
        pass
            