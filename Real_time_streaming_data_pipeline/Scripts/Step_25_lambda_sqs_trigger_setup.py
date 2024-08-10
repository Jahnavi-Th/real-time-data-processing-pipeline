import boto3

lambda_client = boto3.client('lambda')

response = lambda_client.create_event_source_mapping(
    EventSourceArn='arn:aws:sqs:us-east-1:************:ECommerceTransactionsQueue',
    # Replace with your SQS queue ARN
    #replace *********** with IAM USER ID
    FunctionName='AssignmentOneFunction',  # Replace with your Lambda function name
    Enabled=True,
    BatchSize=1,  # You can adjust this value based on how many messages you want to process at once
)

print('Event source mapping created:', response['UUID'])