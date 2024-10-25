from dataclasses import dataclass

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