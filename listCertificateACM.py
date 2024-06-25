import boto3
import os

def get_acm_client():
    aws_access_key_id = ''
    aws_secret_access_key = ''
    aws_session_token = ''
    aws_region = 'us-east-1'  # Substitua pela sua região

    
    return boto3.client('acm', aws_access_key_id=aws_access_key_id,
                               aws_secret_access_key=aws_secret_access_key,
                               aws_session_token=aws_session_token,
                               region_name=aws_region)

def list_certificates(output_file='certificates_output.txt'):
    acm_client = get_acm_client()

    # Obtém o caminho para a área de trabalho
    desktop_path = os.path.join(os.path.expanduser("~"), 'Desktop')

    # Cria o caminho completo para o arquivo de saída
    output_file_path = os.path.join(desktop_path, output_file)

    # Listar certificados
    certificates = acm_client.list_certificates()['CertificateSummaryList']

    with open(output_file_path, 'w') as file:
        for cert in certificates:
            arn = cert['CertificateArn']

            # Obter detalhes do certificado
            cert_details = acm_client.describe_certificate(CertificateArn=arn)['Certificate']

            # Escrever informações no arquivo
            file.write(f'ARN: {arn}\n')
            file.write(f'Nome: {cert_details["DomainName"]}\n')
            file.write(f'Data de Expiração: {cert_details["NotAfter"]}\n')
            file.write(f'Recursos atrelado: {cert_details["InUseBy"]}\n\n')

if __name__ == "__main__":
    list_certificates()