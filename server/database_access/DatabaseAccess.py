import psycopg2, os
from contextlib import contextmanager
from typing import Generator
from psycopg2.extensions import connection


class DatabasePool:
    """
    This class holds the database connection pool for the PostGres SQL server.
    Once this class is initialized, all methods are global class methods which
    interact statically across all instances.
    """

    _instance = None
    pool = None
    config = {
        "database": os.getenv("DB_DATABASE"),
        "host": os.getenv("DB_URL"),
        "user": os.getenv("DB_USERNAME"),
        "password": os.getenv("DB_PASSWORD"),
        "port": os.getenv("DB_PORT"),
    }

    def __new__(cls) -> "DatabasePool":
        if cls._instance is None:
            cls._instance = super(DatabasePool, cls).__new__(cls)
            cls._instance.pool = None
        return cls._instance

    @classmethod
    def initialize(cls, minconn: int, maxconn: int) -> "DatabasePool":
        """
        Initializes the database connection pool with a minimum and maximum number of connections
        and returns the singleton instance of the DatabasePool.

        If the pool is already initialized, it returns the existing instance.

        Args:
            minconn (int): Minimum number of connections to maintain in the pool.
            maxconn (int): Maximum number of connections allowed in the pool.

        Returns:
            DatabasePool: The singleton instance of the DatabasePool class.

        """
        if cls._instance is None:
            cls._instance = cls()
            cls.pool = psycopg2.pool.ThreadedConnectionPool(
                minconn, maxconn, **cls.config
            )
        return cls._instance

    @classmethod
    @contextmanager
    def get_connection(cls) -> Generator[connection, None, None]:
        """
        This method yields a database connection from the connection pool for use
        within a `with` statement. It ensures that the connection is properly
        returned to the pool after the block is executed, even if an exception
        is raised.

        Raises:
            RuntimeError: If the database connection pool has not been initialized
                        (i.e., `cls.pool is None`).

        Yields:
            Generator[connection, None, None]: A database connection from the pool
                                            that can be used within the `with`
                                            statement.
        """
        if cls.pool is None:
            raise RuntimeError(
                "Database pool not initialized. Call DatabasePool.initialize() first."
            )
        conn = cls.pool.getconn()
        try:
            yield conn
        finally:
            cls.pool.putconn(conn)

    @classmethod
    def close_all_connections(cls) -> None:
        """
        This method closes all connections within the internal database pool. The pool is also destroyed.
        """
        if cls.pool:
            cls.pool.closeall()
            cls.pool = None

    @classmethod
    def destroy(cls) -> None:
        """
        This method destroys the internal pool and also destroys the singleton instance of this class.
        This is not necessary, but it is a helpful step if the connection pool needs to be re-created.
        """
        if cls._instance is not None:
            if cls._instance.pool:
                cls._instance.pool.closeall()
            cls._instance = None


class DatabaseAccessor:
    """
    A class used to manage database access and cursor handling.

    This class provides a convenient way to retrieve and manage a database
    cursor using a context manager, ensuring that database transactions
    are either committed or rolled back appropriately, and that resources
    are properly cleaned up.

    Yields:
        psycopg2.extensions.cursor: A database cursor object that can be used
        to execute SQL queries within a `with` block.
    """

    @contextmanager
    def get_cursor(self):
        """
        A context manager that provides a database cursor from the connection pool.

        This method uses the connection pool to retrieve a database connection and
        then creates a cursor for executing SQL queries. It ensures that any changes
        are committed to the database if the operation is successful, or rolled back
        in case of an exception. The cursor is automatically closed at the end of the
        block, whether the operation succeeds or fails.

        Usage example:

        ```
        with DatabaseAccessor().get_cursor() as cursor:
            cursor.execute("SELECT * FROM my_table")
            results = cursor.fetchall()
        ```

        Yields:
            psycopg2.extensions.cursor: A cursor for executing database queries.

        Raises:
            Exception: If an exception occurs during the execution of the SQL queries,
                       the transaction is rolled back, and the exception is re-raised.
        """
        with DatabasePool.get_connection() as conn:
            cursor = conn.cursor()
            try:
                yield cursor
                conn.commit()
            except:
                conn.rollback()
                raise
            finally:
                cursor.close()
                

    def get_next_id(self, table_name):
        """
        Retrieve the next highest ID from a given table.

        Args:
            table_name (str): The name of the table from which to get the next ID.

        Returns:
            int: The next ID value (max ID + 1).
        """
        with self.get_cursor() as cursor:
            query = (
                """
                SELECT max(id) FROM %s
                """
                % table_name
            )
            cursor.execute(query)
            result = cursor.fetchone()  # Fetch the single result from the query
            next_id = (result[0] or 0) + 1  # Ensure 0 if None, then add 1
            return next_id
