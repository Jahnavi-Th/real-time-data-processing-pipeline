import boto3
import json

sqs = boto3.client('sqs')

queue_url = 'https://sqs.us-east-1.amazonaws.com/************/ECommerceTransactionsQueue'  #replace *********** with IAM USER ID

message = {
    "transaction_id": 12345,
    "amount": 100,
    "timestamp": "2024-08-09T12:34:56Z"
}

response = sqs.send_message(
    QueueUrl=queue_url,
    MessageBody=json.dumps(message)
)

print('Message sent:', response)