   
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
            