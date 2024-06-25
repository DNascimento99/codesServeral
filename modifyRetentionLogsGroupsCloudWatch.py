##Retention modify
import re
import boto3

client = boto3.client('logs', region_name='', aws_access_key_id='', aws_secret_access_key='', aws_session_token='')

newlist = []

response = client.describe_log_groups()

for logs in response['logGroups']:
    log_group_name = logs['logGroupName']
    if re.search('dev', log_group_name.lower()) or re.search('hml', log_group_name.lower()):
        if not re.search(r'devops|development', log_group_name.lower()):
            newlist.append(log_group_name)

while 'nextToken' in response:
    response = client.describe_log_groups(nextToken=response['nextToken'])
    for logs in response['logGroups']:
        log_group_name = logs['logGroupName']
        if re.search('dev', log_group_name.lower()) or re.search('hml', log_group_name.lower()):
            if not re.search(r'devops|development', log_group_name.lower()):
                newlist.append(log_group_name)

print(newlist)

print(newlist)
for i in newlist:
 log=client.put_retention_policy(
     logGroupName=i,
     retentionInDays=1
 )
print(newlist)