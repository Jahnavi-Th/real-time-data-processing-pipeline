import boto3

cloudwatch = boto3.client('cloudwatch')

# Define the alarm
response = cloudwatch.put_metric_alarm(
    AlarmName='DynamoDBThrottlingAlarm',
    MetricName='ThrottledRequests',
    Namespace='AWS/DynamoDB',
    Statistic='Sum',
    Period=300,  # 5 minutes
    Threshold=5,  # Trigger if throttled requests are greater than 5
    ComparisonOperator='GreaterThanOrEqualToThreshold',
    EvaluationPeriods=1,
    AlarmActions=[],  # List of ARN for SNS topics or other actions
    OKActions=[],  # Actions to take when the alarm state is OK
    Unit='Count',
    Dimensions=[
        {
            'Name': 'TableName',
            'Value': 'ECommerceTransactions'  # Replace with your DynamoDB table name
        }
    ]
)

print('DynamoDB Throttling Alarm created:', response)