import boto3
from botocore.exceptions import ClientError
def list_objects_v2():
    client = boto3.client('s3', region_name='sa-east-1', aws_access_key_id='', aws_secret_access_key='', aws_session_token='')
    response = client.list_buckets()
    for bucket in response['Buckets']:
        bucket_name = bucket['Name']
        try:
            response = client.list_objects_v2(Bucket=bucket_name)
            if 'Contents' in response:
                total_size = sum(obj['Size'] for obj in response['Contents'])
                print(f'{bucket_name} | {total_size}')
            else:
                print(f'{bucket_name} | Vazio')
        except ClientError as e:
            if e.response['Error']['Code'] == 'AccessDenied' or 'Content':
                print(f"{bucket_name} | Não acessível")
            else:
                print(f"{bucket_name} | Erro ao acessar o Bucket")
                print(e.response['Error']['Message'])
list_objects_v2()