import boto3
import os

lambda_client = boto3.client('lambda')

# Path to your existing ZIP file
zip_filename = 'lambda_function.zip'


def deploy_lambda_function():
    with open(zip_filename, 'rb') as f:
        zipped_code = f.read()

    function_name = 'AssignmentOneFunction'
    role_arn = 'arn:aws:iam::************:role/LambdaExecutionRole'  #replace *********** with IAM USER ID

    try:
        # Try to create the Lambda function
        response = lambda_client.create_function(
            FunctionName=function_name,
            Runtime='python3.12',
            Role=role_arn,
            Handler='lambda_function.lambda_handler',
            Code={
                'ZipFile': zipped_code
            },
            Timeout=300,
            MemorySize=128
        )
        print('Lambda function created:', response)
    except lambda_client.exceptions.ResourceConflictException:
        # If function already exists, update the function code
        print(f'Lambda function {function_name} already exists. Updating...')
        response = lambda_client.update_function_code(
            FunctionName=function_name,
            ZipFile=zipped_code
        )
        print('Lambda function updated:', response)
    except Exception as e:
        print(f"Error deploying Lambda function: {e}")


deploy_lambda_function()