   
class User():
    def __init__(self, id: int):
        self.id = id
        self.connections = {}
        
    def exists(self):
        pass
        
    def get_personal_info(self) -> dict:
        pass
        
    def get_connections(self, network: int):
        net = network(self.user_id, network)
        net.init_network()
        return net.network()
    
    def add_connection(self, network: int):
        pass
    

class Network():
    def __init__(self, user_id: int, network_id: int):
        self.user_id = user_id
        self.netork_id = network_id
        self.network = {}
        
    def exists(self):
        pass
        
    def init_network(self):
        pass
            