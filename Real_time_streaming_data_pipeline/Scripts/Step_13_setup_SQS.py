import boto3

sqs = boto3.client('sqs')

response = sqs.create_queue(
    QueueName='ECommerceTransactionsQueue',
    Attributes={
        'DelaySeconds': '0',
        'MessageRetentionPeriod': '86400'
    }
)

print('Queue URL:', response['QueueUrl'])