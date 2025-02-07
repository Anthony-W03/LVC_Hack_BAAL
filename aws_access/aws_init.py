import boto3, os, time
from dotenv import load_dotenv, dotenv_values 

# loading variables from .env file
load_dotenv() 

# Create a session using your AWS credentials
session = boto3.Session(
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    aws_session_token=os.getenv('AWS_SESSION_TOKEN'),
    region_name=os.getenv('AWS_DEFAULT_REGION')  # e.g., 'us-west-2'
)

# Create the Athena client
athena_client = session.client('athena')

# Function to create a database
def create_database(database_name, s3_output_location):
    # SQL query to create the database
    query = f"CREATE DATABASE IF NOT EXISTS {database_name};"
    
    # Start the query execution
    response = athena_client.start_query_execution(
        QueryString=query,
        QueryExecutionContext={
            'Database': 'default'  # Athena requires specifying an existing database; 'default' is always available.
        },
        ResultConfiguration={
            'OutputLocation': s3_output_location  # S3 location where query results will be stored
        }
    )
    
    # Query Execution ID
    query_execution_id = response['QueryExecutionId']
    print(f"Query execution ID: {query_execution_id}")
    
    # Wait for the query to finish
    return wait_for_query_to_complete(query_execution_id)

# Function to check query execution status
def wait_for_query_to_complete(query_execution_id):
    while True:
        # Get the execution status of the query
        response = athena_client.get_query_execution(QueryExecutionId=query_execution_id)
        status = response['QueryExecution']['Status']['State']
        
        if status in ['SUCCEEDED', 'FAILED', 'CANCELLED']:
            return status
        else:
            print("Query is still running... Checking again in 5 seconds.")
            time.sleep(5)

# Replace with your desired database name and S3 bucket location for output
database_name = "hackathon_f2024_baal_database"
s3_output_location = "s3://hackathon-f2024-baal/database"

# Create the database
status = create_database(database_name, s3_output_location)
print(f"Database creation status: {status}")