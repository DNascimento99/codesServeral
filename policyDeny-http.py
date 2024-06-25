import boto3
import json

client = boto3.client('s3', aws_access_key_id="",
                            aws_secret_access_key="",
                            aws_session_token="")
array = [''] 

for bucket_name in array:
    try:
        current_policy = client.get_bucket_policy(Bucket=bucket_name)['Policy']
        current_policy = json.loads(current_policy)
    except Exception as e:
        current_policy = None
    new_policy = {
        'Version': '2012-10-17',
        'Statement': [{
            'Sid': 'DenyHTTP',
            'Effect': 'Deny',
            'Principal': '*',
            'Action': ['s3:*'],
            'Resource': [f"arn:aws:s3:::{bucket_name}/*", f"arn:aws:s3:::{bucket_name}"],
            'Condition': {
                'Bool': {
                    'aws:SecureTransport': 'false'
                }
            }
        }]
    }
    if current_policy:
        current_policy['Statement'].extend(new_policy['Statement'])
        updated_policy = current_policy
    else:
        updated_policy = new_policy

    response = client.put_bucket_policy(
        Bucket=bucket_name,
        Policy=json.dumps(updated_policy)
    )
    print(response)