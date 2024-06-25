import boto3
import json

def lambda_handler(event, context):
    auto_scaling_group_name = "ASGV1"
    autoscaling_client = boto3.client('autoscaling')
    try:
        response = client.start_instance_refresh(
            AutoScalingGroupName='auto_scaling_group_name',
            DesiredConfiguration={
                'LaunchTemplate': {
                'LaunchTemplateName': 'TemplateV1',
                'Version': '$Latest',
                },
            },
            Preferences={
                'AlarmSpecification': {
                    'Alarms': [
                    'my-alarm',
                    ],
                },
                'AutoRollback': True,
                'InstanceWarmup': 200,
                'MinHealthyPercentage': 90,
                },
        )
        return {
            "statusCode": 200,
            "body": json.dumps(response)
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": f"Error: {str(e)}"
        }