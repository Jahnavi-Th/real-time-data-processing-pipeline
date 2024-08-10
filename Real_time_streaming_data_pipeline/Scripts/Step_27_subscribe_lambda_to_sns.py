import boto3

sns = boto3.client('sns')

response = sns.subscribe(
    TopicArn='arn:aws:sns:us-east-1:************:ECommerceNotificationsTopic', #replace *********** with IAM USER ID,  # Replace with your SNS topic ARN
    Protocol='lambda',
    Endpoint='arn:aws:lambda:us-east-1:************:function:AssignmentOneFunction'  #replace *********** with IAM USER ID,  # Replace with your Lambda function ARN
)

print('Subscription ARN:', response['SubscriptionArn'])