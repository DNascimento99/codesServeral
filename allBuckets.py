import boto3
from botocore.exceptions import ClientError

def list_buckets_and_objects():
    try:
        session = boto3.Session(region_name='sa-east-1', aws_access_key_id='', aws_secret_access_key='', aws_session_token='')
        s3_client = session.client('s3')
        response = s3_client.list_buckets()
        for bucket in response['Buckets']:
            bucket_name = bucket['Name']
            print(f"Bucket: {bucket_name}")
            s3_resource = session.resource('s3')
            bucket = s3_resource.Bucket(bucket_name)
            for obj in bucket.objects.all():
                print(f"Object: {obj.key}")
    except ClientError as e:
        if e.response['Error']['Code'] == 'AccessDenied':
            print(f"Access denied for bucket: {bucket_name}")
        else:
            print(f"Error occurred for bucket: {bucket_name}")
            print(e.response['Error']['Message'])
list_buckets_and_objects()
