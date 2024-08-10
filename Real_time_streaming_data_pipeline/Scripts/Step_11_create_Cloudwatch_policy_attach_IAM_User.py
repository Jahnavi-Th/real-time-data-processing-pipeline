import boto3
import json

# Initialize IAM client
iam = boto3.client('iam')

# Define policy details
policy_name = 'ComprehensiveCloudWatchPolicy'
policy_document = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "cloudwatch:PutMetricAlarm",
                "cloudwatch:DescribeAlarms",
                "cloudwatch:DeleteAlarms",
                "cloudwatch:ListMetrics",
                "cloudwatch:GetMetricData",
                "cloudwatch:GetMetricStatistics",
                "cloudwatch:PutMetricData",
                "cloudwatch:DescribeAlarmHistory",
                "cloudwatch:ListTagsForResource",
                "cloudwatch:TagResource",
                "cloudwatch:UntagResource",
                "cloudwatch:PutDashboard",
                "cloudwatch:GetDashboard",
                "cloudwatch:DeleteDashboards",
                "cloudwatch:DescribeAlarmsForMetric",
                "cloudwatch:ListDashboards",
                "cloudwatch:PutAnomalyDetector",
                "cloudwatch:DescribeAnomalyDetectors",
                "cloudwatch:DeleteAnomalyDetector",
                "cloudwatch:PutInsightRule",
                "cloudwatch:DescribeInsightRules",
                "cloudwatch:DeleteInsightRules",
                "logs:PutMetricFilter",
                "logs:DescribeLogGroups",
                "logs:DescribeLogStreams",
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutRetentionPolicy",
                "logs:DeleteLogGroup",
                "logs:DeleteLogStream"
            ],
            "Resource": "*"
        }
    ]
}

# Create the policy
try:
    response = iam.create_policy(
        PolicyName=policy_name,
        PolicyDocument=json.dumps(policy_document)
    )
    print(f'Policy created successfully. Policy ARN: {response["Policy"]["Arn"]}')
    policy_arn = response['Policy']['Arn']
except Exception as e:
    print(f'Error creating policy: {e}')
    policy_arn = None

# Define user name
user_name = 'XXXXXXXXXXX'  # Replace with your username

# Attach the policy to the IAM user if policy creation was successful
if policy_arn:
    try:
        response = iam.attach_user_policy(
            UserName=user_name,
            PolicyArn=policy_arn
        )
        print(f'Policy {policy_arn} successfully attached to user {user_name}.')
    except Exception as e:
        print(f'Error attaching policy to user: {e}')