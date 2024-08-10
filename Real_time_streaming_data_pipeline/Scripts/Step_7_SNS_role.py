import boto3
import json

# Initialize the IAM client
iam = boto3.client('iam')

role_name = 'SNSExecutionRole'
policy_name = 'SNSExecutionPolicy'

# Define the updated policy document
updated_policy_document = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "sns:CreateTopic",
                "sns:DeleteTopic",
                "sns:ListTopics",
                "sns:GetTopicAttributes",
                "sns:SetTopicAttributes",
                "sns:Subscribe",
                "sns:Unsubscribe",
                "sns:ListSubscriptionsByTopic",
                "sns:Publish",
                "sns:ConfirmSubscription",
                "sns:GetSubscriptionAttributes",
                "sns:SetSubscriptionAttributes",
                "sns:RemovePermission",
                "sns:ListSubscriptions",
                "sns:AddPermission"
            ],
            "Resource": "arn:aws:sns:us-east-1:************:*"  #replace *********** with IAM USER ID
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
            "Resource": "arn:aws:sqs:us-east-1:************:*"  #replace *********** with IAM USER ID
        },
        {
            "Effect": "Allow",
            "Action": [
                "lambda:InvokeFunction"
            ],
            "Resource": "arn:aws:lambda:us-east-1:637423356513:function:AssignmentOneFunction",
            "Condition": {
                "ArnLike": {
                    "aws:SourceArn": "arn:aws:sns:us-east-1:************:ECommerceNotificationsTopic"#replace *********** with IAM USER ID
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "*"
        }
    ]
}

# Update the role's policy
try:
    # Check if the role exists
    role = iam.get_role(RoleName=role_name)
    print(f"Role {role_name} exists.")

    # Check if the policy already exists
    try:
        policy_arn = f"arn:aws:iam::************:policy/{policy_name}"  #replace *********** with IAM USER ID
        iam.get_policy(PolicyArn=policy_arn)

        # Create a new version of the existing policy
        iam.create_policy_version(
            PolicyArn=policy_arn,
            PolicyDocument=json.dumps(updated_policy_document),
            SetAsDefault=True
        )
        print(f"Policy {policy_name} updated.")
    except iam.exceptions.NoSuchEntityException:
        # If the policy doesn't exist, create it
        response = iam.create_policy(
            PolicyName=policy_name,
            PolicyDocument=json.dumps(updated_policy_document)
        )
        print(f"Policy {policy_name} created.")
        policy_arn = response['Policy']['Arn']

    # Attach the policy to the role
    iam.attach_role_policy(
        RoleName=role_name,
        PolicyArn=policy_arn
    )
    print(f"Policy {policy_name} attached to role {role_name}.")

except iam.exceptions.NoSuchEntityException:
    print(f"Role {role_name} does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")