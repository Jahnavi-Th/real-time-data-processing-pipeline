import boto3

iam = boto3.client('iam')

role_name = 'SNSExecutionRole'  # Replace with your SNS role name
policy_arn = 'arn:aws:iam::************:policy/SNSExecutionPolicy'  #replace *********** with IAM USER ID

try:
    response = iam.attach_role_policy(
        RoleName=role_name,
        PolicyArn=policy_arn
    )
    print(f"Policy ARN: {policy_arn} successfully attached to role {role_name}.")
except Exception as e:
    print(f"An error occurred: {e}")