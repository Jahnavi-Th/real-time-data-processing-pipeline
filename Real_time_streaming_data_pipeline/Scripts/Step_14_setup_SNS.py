import boto3

sns = boto3.client('sns')

response = sns.create_topic(
    Name='ECommerceNotificationsTopic'
)

print('Topic ARN:', response['TopicArn'])