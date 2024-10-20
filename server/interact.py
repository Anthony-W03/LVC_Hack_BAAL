   
class User():
    def __init__(self, id: int):
        self.id = id
        self.connections = {}
        self.networks = []
        
    def get_personal_info(self) -> dict:
        pass
        
    def get_connections(self, network: int):
        net = network(self.user_id, network)
        net.init_network()
        return net.network()
    
    def add_connection(self, network: int):
        pass
    
    

class Connection():
    def __init__(self, connection_id: int, fname: str, lname: str, email: str | None):
        self.connection_id = connection_id
        self.fname = fname
        self.lname = lname
        self.email = email

class Network():
    def __init__(self, user_id: int, network_id: int):
        self.user_id = user_id
        self.netork_id = network_id
        self.network = {}
        
    def update_network(self, connection: Connection):
        if connection.connection_id in self.network.keys():
            self.network[connection.connection_id]
        else:
            
    
            