import boto3
import json

iam = boto3.client('iam')

# Define the role
role_name = 'SQSExecutionRole'
trust_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "sns:Publish"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "sqs:CreateQueue",
                "sqs:ListQueues",
                "sqs:GetQueueAttributes",
                "sqs:SetQueueAttributes",
                "sqs:DeleteQueue",
                "sqs:SendMessage",
                "sqs:ReceiveMessage",
                "sqs:DeleteMessage",
                "sqs:PurgeQueue"
            ],
            "Resource": "arn:aws:sqs:us-east-1:************:*"   #replace *********** with IAM USER ID
        }
    ]
}

# Create the role
response = iam.create_role(
    RoleName=role_name,
    AssumeRolePolicyDocument=json.dumps(trust_policy)
)

print('SQS Role ARN:', response['Role']['Arn'])