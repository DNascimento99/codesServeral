import boto3
from prettytable import PrettyTable

def list_secrets(regions):
    all_secrets = []
    for region in regions:
        client = boto3.client('secretsmanager', region_name=region)
        paginator = client.get_paginator('list_secrets')
        for page in paginator.paginate():
            for secret in page['SecretList']:
                secret_metadata = client.describe_secret(SecretId=secret['ARN'])
                rotation_enabled = secret_metadata.get('RotationEnabled', False)
                all_secrets.append({
                    'Name': secret['Name'],
                    'Region': region,
                    'RotationEnabled': rotation_enabled,
                    'Tags': secret.get('Tags', [])
                })
    return all_secrets

def write_secrets_to_file(secrets, filename):
    table = PrettyTable()
    table.field_names = ["Region", "Secret Name", "Rotation Enabled", "Tags Keys", "Tags Values"]
    for secret in secrets:
        secret_name = secret['Name']
        region = secret['Region']
        rotation_enabled = "Enabled" if secret['RotationEnabled'] else "Disabled"
        tag_keys = '\n'.join([tag['Key'] for tag in secret['Tags']])
        tag_values = '\n'.join([tag['Value'] for tag in secret['Tags']])
        table.add_row([region, secret_name, rotation_enabled, tag_keys, tag_values])
    with open(filename, 'w') as file:
        file.write(str(table) + '\n')
        
if __name__ == "__main__":
    regions = ['us-east-1', 'sa-east-1']
    secrets = list_secrets(regions)
    write_secrets_to_file(secrets, 'brasilprev-dev-qa (8641-8608-0515).txt')
