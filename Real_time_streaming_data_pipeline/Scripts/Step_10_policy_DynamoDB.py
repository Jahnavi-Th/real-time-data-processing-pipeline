import boto3
import json

# Initialize IAM client
iam = boto3.client('iam')

policy_name = 'DynamoDBAccessPolicy'
existing_policy_arn = 'arn:aws:iam::************:policy/DynamoDBAccessPolicy'
# Replace with the actual ARN
#replace *********** with IAM USER ID

# Get the existing policy version
versions = iam.list_policy_versions(PolicyArn=existing_policy_arn)
current_version_id = versions['Versions'][0]['VersionId']  # Assuming the first version is the current one

# Create a new policy version
policy_document = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "dynamodb:CreateTable",
                "dynamodb:DeleteTable",
                "dynamodb:UpdateTable",
                "dynamodb:DescribeTable",
                "dynamodb:ListTables",
                "dynamodb:PutItem",
                "dynamodb:GetItem",
                "dynamodb:UpdateItem",
                "dynamodb:DeleteItem",
                "dynamodb:Scan",  # Added permission
                "dynamodb:Query"  # Added permission
            ],
            "Resource": "*"
        }
    ]
}

try:
    iam.create_policy_version(
        PolicyArn=existing_policy_arn,
        PolicyDocument=json.dumps(policy_document),
        SetAsDefault=True
    )
    print(f'Policy updated successfully.')
except Exception as e:
    print(f'Error updating policy: {e}')