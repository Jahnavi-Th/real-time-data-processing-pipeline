import boto3

iam = boto3.client('iam')

# Replace with your role names
roles = ['LambdaExecutionRole', 'SQSExecutionRole', 'SNSExecutionRole']

for role in roles:
    response = iam.list_attached_role_policies(RoleName=role)
    print(f'Attached policies for {role}:', response['AttachedPolicies'])