from dataclasses import dataclass
      
@dataclass
class Connection:
    connection_id: int
    user_id: int
    network_id: int
    fname: str
    lname: str
    connection_through: int
    linkedin: str | None = None
    website: str | None = None
    email: str | None = None
    phone: str | None = None
    address: str | None = None
    employment: str | None = None