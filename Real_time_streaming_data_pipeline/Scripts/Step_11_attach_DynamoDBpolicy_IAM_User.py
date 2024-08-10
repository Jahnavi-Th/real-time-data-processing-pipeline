import boto3

# Initialize IAM client
iam = boto3.client('iam')

# Define user name and policy ARN
user_name = 'JahnaviIAM'
policy_arn = 'arn:aws:iam::************:policy/DynamoDBAccessPolicy'
# Replace with your policy ARN
#replace *********** with IAM USER ID

try:
    # Attach the policy to the IAM user
    response = iam.attach_user_policy(
        UserName=user_name,
        PolicyArn=policy_arn
    )
    print(f'Policy {policy_arn} successfully attached to user {user_name}.')
except Exception as e:
    print(f'Error attaching policy to user: {e}')