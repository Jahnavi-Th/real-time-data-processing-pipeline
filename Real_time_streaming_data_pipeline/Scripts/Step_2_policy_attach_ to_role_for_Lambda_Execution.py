import boto3
from botocore.exceptions import ClientError

iam = boto3.client('iam')

role_name = 'LambdaExecutionRole'
policy_arn = 'arn:aws:iam::************:policy/LambdaExecutionPolicy'
#replace *********** with IAM USER ID

# Attach the policy to the role
try:
    iam.attach_role_policy(
        RoleName=role_name,
        PolicyArn=policy_arn
    )
    print(f"Policy {policy_arn} successfully attached to role {role_name}.")
except ClientError as e:
    print(f"Error attaching policy: {e}")