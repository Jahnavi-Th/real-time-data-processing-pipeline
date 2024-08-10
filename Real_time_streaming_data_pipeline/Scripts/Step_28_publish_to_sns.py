import boto3
import json

# Initialize the SNS client
sns = boto3.client('sns')

# Define the SNS topic ARN
topic_arn = 'arn:aws:sns:us-east-1:************:ECommerceNotificationsTopic'  #replace *********** with IAM USER ID

# Define the message
message = {
    "transaction_id": 67890,
    "amount": 1500,
    "timestamp": "2024-08-10T12:34:56Z"
}

# Publish the message
response = sns.publish(
    TopicArn=topic_arn,
    Message=json.dumps(message)
)

# Print the response
print('Message published:', response)