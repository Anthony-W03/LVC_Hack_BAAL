import boto3, os, time
from dotenv import load_dotenv, dotenv_values 
from pathlib import Path

# loading variables from .env file
load_dotenv() 


class database_connection():
    def __init__(self):
        self.session = boto3.Session(
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
            aws_session_token=os.getenv('AWS_SESSION_TOKEN'),
            region_name=os.getenv('AWS_DEFAULT_REGION')  # e.g., 'us-west-2'
        )
        
        # Create the Athena client
        self.athena_client = self.session.client('athena')
        
        # Database path
        self.db_path = Path('')
        
        # Is open
        self.is_open = True
        
        # Function to run a general query
    def run_athena_query(self, query, database, s3_output_location):
        # Start the query execution
        response = self.athena_client.start_query_execution(
            QueryString=query,
            QueryExecutionContext={
                'Database': database  # Specify the database in which the query is run
            },
            ResultConfiguration={
                'OutputLocation': s3_output_location  # S3 location where query results will be stored
            }
        )
        
        # Get the query execution ID
        query_execution_id = response['QueryExecutionId']
        print(f"Query execution ID: {query_execution_id}")
        
        # Wait for the query to finish
        status = self.wait_for_query_to_complete(query_execution_id)
        
        if status == 'SUCCEEDED':
            # Get the query results
            results = self.get_query_results(query_execution_id)
            return results
        else:
            print(f"Query failed with status: {status}")
            return None

    # Function to check query execution status
    def wait_for_query_to_complete(self, query_execution_id):
        while True:
            # Get the execution status of the query
            response = self.athena_client.get_query_execution(QueryExecutionId=query_execution_id)
            
            print(response)
            status = response['QueryExecution']['Status']['State']
            
            if status in ['SUCCEEDED', 'FAILED', 'CANCELLED']:
                return status
            else:
                print("Query is still running... Checking again in 5 seconds.")
                time.sleep(5)

    # Function to fetch query results
    def get_query_results(self, query_execution_id):
        results = []
        
        # Fetch the query results from Athena
        response = self.athena_client.get_query_results(QueryExecutionId=query_execution_id)
        
        # Extract the rows
        rows = response['ResultSet']['Rows']
        for row in rows:
            data = [col.get('VarCharValue', 'NULL') for col in row['Data']]
            results.append(data)
        
        return results
        
        
db = database_connection()
db.db_path = Path("s3://hackathon_f2024_baal_database")


'''
db.run_athena_query(
    """
    CREATE EXTERNAL TABLE Users (
        id INT,
        username VARCHAR(255),
        email VARCHAR(255),
        password VARCHAR(255)
    )
    ROW FORMAT DELIMITED
    FIELDS TERMINATED BY ','
    LINES TERMINATED BY '\\n'
    STORED AS TEXTFILE
    LOCATION 's3://athena-hackathon-f2024-baal/database/user/';
    """,
    "hackathon_f2024_baal_database",
    "s3://athena-hackathon-f2024-baal/database"
)
'''

