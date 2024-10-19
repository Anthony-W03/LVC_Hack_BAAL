import boto3, os
from dotenv import load_dotenv, dotenv_values 

# loading variables from .env file
load_dotenv() 

# Create a session using your AWS credentials
print(os.getenv('AWS_ACCESS_KEY_ID'))
session = boto3.Session(
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    aws_session_token=os.getenv('AWS_SESSION_TOKEN'),
    region_name=os.getenv('AWS_DEFAULT_REGION')  # e.g., 'us-west-2'
)

# Create a client for a specific AWS service (e.g., S3)
s3_client = session.client('s3')

# Now you can use s3_client to interact with S3
# For example, to list your S3 buckets:
response = s3_client.list_buckets()
for bucket in response['Buckets']:
    print(f'Bucket Name: {bucket["Name"]}')