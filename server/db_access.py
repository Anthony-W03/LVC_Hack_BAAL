import psycopg2, os
from psycopg2 import pool
from contextlib import contextmanager
from dotenv import load_dotenv, dotenv_values

class GlobalDatabasePool:
    """_summary_

    Raises:
        RuntimeError: _description_

    Returns:
        _type_: _description_

    Yields:
        _type_: _description_
    """
    _instance = None
    pool = None
    config = {
            "database":os.getenv('DB_DATABASE'),
            "host":os.getenv('DB_URL'),
            "user":os.getenv('DB_USERNAME'),
            "password":os.getenv('DB_PASSWORD'),
            "port":os.getenv('DB_PORT')
        }

    @classmethod
    def initialize(cls, minconn, maxconn):
        if cls._instance is None:
            cls._instance = cls()
            cls.pool = psycopg2.pool.ThreadedConnectionPool(minconn, maxconn, **cls.config)
        return cls._instance

    @classmethod
    @contextmanager
    def get_connection(cls):
        if cls.pool is None:
            raise RuntimeError("Database pool not initialized. Call GlobalDatabasePool.initialize() first.")
        conn = cls.pool.getconn()
        try:
            yield conn
        finally:
            cls.pool.putconn(conn)

    @classmethod
    def close_all_connections(cls):
        if cls.pool:
            cls.pool.closeall()
            cls.pool = None

class DatabaseAccessor:
    """_summary_

    Yields:
        _type_: _description_
    """
    @contextmanager
    def get_cursor(self):
        with GlobalDatabasePool.get_connection() as conn:
            cursor = conn.cursor()
            try:
                yield cursor
                conn.commit()
            except:
                conn.rollback()
                raise
            finally:
                cursor.close()

class UserRepository(DatabaseAccessor):
    def get_user_by_id(self, user_id):
        with self.get_cursor() as cursor:
            cursor.execute("SELECT * FROM useraccounts WHERE id = %s" % (user_id))
            return cursor.fetchone()

    def create_user(self, username, email):
        with self.get_cursor() as cursor:
            cursor.execute(
                "INSERT INTO users (username, email) VALUES (%s, %s) RETURNING id",
                (username, email)
            )
            return cursor.fetchone()[0]

# Example usage
if __name__ == "__main__":
    load_dotenv() 
    
    # Initialize the global database pool
    
    
    GlobalDatabasePool.initialize(
        minconn=1,
        maxconn=10
    )

    # Create a UserRepository instance (no need to pass the pool)
    user_repo = UserRepository()

    try:
        # Create a new user
        # new_user_id = user_repo.create_user("john_doe", "john@example.com")
        # print(f"Created new user with ID: {new_user_id}")

        # Retrieve the user
        new_user_id = 0
        user = user_repo.get_user_by_id(new_user_id)
        print(f"Retrieved user: {user}")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close all connections in the pool when you're done
        GlobalDatabasePool.close_all_connections()