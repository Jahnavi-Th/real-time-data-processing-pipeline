import boto3
import json

sqs = boto3.client('sqs')

queue_url = 'https://sqs.us-east-1.amazonaws.com/************/ECommerceTransactionsQueue'
# Replace with your SQS queue URL
#replace *********** with IAM USER ID

policy = {
    "Version": "2012-10-17",
    "Id": "QueuePolicy",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "SQS:SendMessage",
            "Resource": queue_url,
            "Condition": {
                "ArnEquals": {
                    "aws:SourceArn": "arn:aws:sns:us-east-1:***********:ECommerceNotificationsTopic"  # Your SNS topic ARN
                    #replace *********** with IAM USER ID
                }
            }
        }
    ]
}

response = sqs.set_queue_attributes(
    QueueUrl=queue_url,
    Attributes={
        'Policy': json.dumps(policy)
    }
)

print('Queue policy set:', response)