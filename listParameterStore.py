import boto3

# Defina suas credenciais AWS
aws_access_key_id = ''
aws_secret_access_key = ''
aws_session_token = ''
aws_region = 'us-east-1'

# Crie uma sessão com o boto3 usando as credenciais fornecidas
session = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    aws_session_token=aws_session_token,
    region_name=aws_region
)

ssm_client = session.client('ssm')
resourcegroupstaggingapi_client = session.client('resourcegroupstaggingapi')

def get_parameters_and_tags():
    # Use um paginador para iterar por todas as páginas de resultados
    paginator = ssm_client.get_paginator('describe_parameters')
    page_iterator = paginator.paginate()
    
    result = []

    for page in page_iterator:
        parameters = page['Parameters']
        
        for parameter in parameters:
            param_name = parameter['Name']
            
            # Obtenha o ARN correto para cada parâmetro
            arn = f'arn:aws:ssm:{session.region_name}:{session.client("sts").get_caller_identity()["Account"]}:parameter/{param_name}'
            tags_response = resourcegroupstaggingapi_client.get_resources(
                ResourceARNList=[arn]
            )
            
            tags = tags_response['ResourceTagMappingList'][0]['Tags'] if tags_response['ResourceTagMappingList'] else []
            tag_str = ", ".join([f"{tag['Key']}:{tag['Value']}" for tag in tags])
            
            result.append((param_name, tag_str))
    
    return result

if __name__ == "__main__":
    params_and_tags = get_parameters_and_tags()
    
    # Imprima os resultados em formato de tabela com | como separador
    print(f"{'Nome':<40} | Tags")
    for param, tags in params_and_tags:
        print(f"{param:<40} | {tags}")
