import boto3

logs = boto3.client('logs')

response = logs.put_metric_filter(
    logGroupName='/aws/lambda/AssignmentOneFunction',  # Replace with your Lambda log group name
    filterName='ErrorMetricFilter',
    filterPattern='ERROR',
    metricTransformations=[
        {
            'metricName': 'LambdaErrors',
            'metricNamespace': 'YourNamespace',
            'metricValue': '1'
        }
    ]
)

print('Metric filter created:', response)