import pymysql

# Define your database configuration
rds_proxy_endpoint = 'baal-hackathon-f2024-b.proxy-cwi2abhgazbq.us-west-2.rds.amazonaws.com'
db_username = 'admin'
db_password = 'Blackrook64'
db_name = 'database-1'
db_port = 3306  # Default MySQL port

# Establish a connection to the database through the proxy
try:
    conn = pymysql.connect(
        host=rds_proxy_endpoint,
        user=db_username,
        password=db_password,
        database=db_name,
        port=db_port
    )
    print("Connection successful!")

    # Use the connection
    cursor = conn.cursor()
    cursor.execute("SELECT VERSION();")
    db_version = cursor.fetchone()
    print("Database version:", db_version)

    # Close the cursor and connection
    cursor.close()
    conn.close()

except Exception as e:
    print("Error connecting to the database:", e)

