import boto3

cloudwatch = boto3.client('cloudwatch')

# Define the alarm
response = cloudwatch.put_metric_alarm(
    AlarmName='LambdaErrorsAlarm',
    MetricName='Errors',
    Namespace='AWS/Lambda',
    Statistic='Sum',
    Period=300,  # 5 minutes
    Threshold=1,  # Trigger if errors are greater than 1
    ComparisonOperator='GreaterThanOrEqualToThreshold',
    EvaluationPeriods=1,
    AlarmActions=[],  # List of ARN for SNS topics or other actions
    OKActions=[],  # Actions to take when the alarm state is OK
    Unit='Count',
    Dimensions=[
        {
            'Name': 'FunctionName',
            'Value': 'YourLambdaFunctionName'  # Replace with your Lambda function name
        }
    ]
)

print('Alarm created:', response)