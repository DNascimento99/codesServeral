import boto3
from botocore.exceptions import ClientError
def list_empty_buckets():
    client = boto3.client('s3', region_name='sa-east-1', aws_access_key_id='', aws_secret_access_key='', aws_session_token='')
    response = client.list_buckets()
    for bucket in response['Buckets']:
        bucket_name = bucket['Name']
        try:
            response = client.list_objects_v2(Bucket=bucket_name, MaxKeys=1)
            if 'Contents' not in response:
                print(f'Bucket Vazio encontrado: {bucket_name}')
        except ClientError as e:
            if e.response['Error']['Code'] == 'AccessDenied':
                print(f"Access denied for bucket: {bucket_name}")
            else:
                print(f"Error occurred for bucket: {bucket_name}")
                print(e.response['Error']['Message'])
list_empty_buckets()