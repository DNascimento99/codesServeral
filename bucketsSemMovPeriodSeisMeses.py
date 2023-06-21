import boto3
from botocore.exceptions import ClientError
from datetime import datetime, timedelta, timezone
client = boto3.client(
    's3',
    region_name='sa-east-1',
    aws_access_key_id='',
    aws_secret_access_key='',
    aws_session_token=''
)
seis_meses_atras = datetime.now(timezone.utc) - timedelta(days=180)
response = client.list_buckets()
buckets_sem_movimentacao = []
for bucket in response['Buckets']:
    bucket_name = bucket['Name']
    try:
        response = client.list_objects_v2(Bucket=bucket_name)
        if 'Contents' not in response or len(response['Contents']) == 0:
            buckets_sem_movimentacao.append(bucket_name)
        else:
            objetos = response['Contents']
            objetos_recentes = [obj for obj in objetos if obj['LastModified'] >= seis_meses_atras]
            if not objetos_recentes:
                buckets_sem_movimentacao.append(bucket_name)
    except ClientError as e:
        if e.response['Error']['Code'] == 'AccessDenied':
            print(f"Access denied for bucket: {bucket_name}")
        else:
            print(f"Error occurred for bucket: {bucket_name}")
            print(e.response['Error']['Message'])
for bucket_name in buckets_sem_movimentacao:
    print(bucket_name)
