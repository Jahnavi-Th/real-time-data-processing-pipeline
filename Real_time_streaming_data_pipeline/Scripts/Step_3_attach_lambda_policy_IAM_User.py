import boto3

iam = boto3.client('iam')

policy_arn = 'arn:aws:iam::************:policy/LambdaExecutionPolicy'
#replace *********** with IAM USER ID
# Replace with your policy ARN
user_name = 'XXXXXXXXXX'  # Replace with the name of your IAM user

# Attach the policy to the user
response = iam.attach_user_policy(
    UserName=user_name,
    PolicyArn=policy_arn
)

print('Policy attached successfully:', response)