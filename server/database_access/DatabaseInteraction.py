from .DatabaseAccess import DatabaseAccessor
from .DatabaseAccess import DatabasePool

class DatabaseInteractor(DatabaseAccessor):
    """
    A class that extends DatabaseAccessor to interact with user-related data
    in the database. Provides methods for fetching and updating database entries.

    Methods:
        fetch(query: str, args: tuple = ()) -> list: Fetches data from the database.
        update(query: str, args: tuple = ()) -> None: Updates data in the database.
    """

    # FETCH FROM DATABASE
    def fetch_database(self, query: str, args: tuple = ()) -> list:
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
    def update_database(self, query: str, args: tuple = ()) -> None:
        """
        Updates the database using the provided SQL query.

        Args:
            query (str): The SQL query to be executed.
            args (tuple, optional): The arguments to be passed to the query.
        """
        with self.get_cursor as cursor:
            cursor.execute(query, args)
            return
