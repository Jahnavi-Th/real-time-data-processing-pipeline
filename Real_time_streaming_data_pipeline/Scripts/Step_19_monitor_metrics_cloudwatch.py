import boto3

cloudwatch = boto3.client('cloudwatch')

response = cloudwatch.list_metrics(
    Namespace='AWS/Lambda',
    MetricName='Errors',
    Dimensions=[
        {
            'Name': 'FunctionName',
            'Value': 'AssignmentOneFunction'  # Replace with your Lambda function name
        }
    ]
)

print('Metrics:', response)