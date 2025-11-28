import boto3
from botocore.exceptions import ClientError

session = boto3.Session(profile_name='default')

s3_client = boto3.client('s3')

print('Connecting to AWS...')

response = s3_client.list_buckets()

buckets = response['Buckets']

print(f"Found {len(buckets)} buckets:")

for bucket in buckets:
    print(f"- {bucket['Name']}")