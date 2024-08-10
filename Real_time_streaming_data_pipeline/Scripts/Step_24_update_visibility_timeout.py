import boto3

sqs = boto3.client('sqs')

queue_url = 'https://sqs.us-east-1.amazonaws.com/************/ECommerceTransactionsQueue' #replace *********** with IAM USER ID

response = sqs.set_queue_attributes(
    QueueUrl=queue_url,
    Attributes={
        'VisibilityTimeout': '360'  # Set to 6 minutes (360 seconds) or more
    }
)

print('Visibility timeout updated:', response)