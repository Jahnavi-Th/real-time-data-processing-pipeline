import json
import boto3

# Initialize AWS services
dynamodb = boto3.resource('dynamodb')
sns = boto3.client('sns')
table = dynamodb.Table('ECommerceTransactions')

# SNS Topic ARN
SNS_TOPIC_ARN = 'arn:aws:sns:us-east-1:************:ECommerceNotificationsTopic'
#replace *********** with IAM USER ID

def lambda_handler(event, context):
    for record in event['Records']:
        print(f"Record: {record}")
        try:
            body = record['body']
            # Check if the body is JSON
            try:
                message = json.loads(body)
                print(f"Processed JSON message: {message}")

                # Extract attributes
                transaction_id = int(message['transaction_id'])  # Ensure it's converted to int
                amount = message['amount']
                timestamp = message['timestamp']

                # Put item into DynamoDB
                response = table.put_item(
                    Item={
                        'transaction_id': transaction_id,
                        'amount': amount,
                        'timestamp': timestamp
                    }
                )
                print(f"DynamoDB response: {response}")

                # Publish SNS notification for large transactions
                if float(amount) > 1000:  # Example condition for large transactions
                    sns_message = {
                        'transaction_id': transaction_id,
                        'amount': amount,
                        'timestamp': timestamp
                    }
                    sns_response = sns.publish(
                        TopicArn=SNS_TOPIC_ARN,
                        Message=json.dumps(sns_message),
                        Subject='Large Transaction Alert'
                    )
                    print(f"SNS response: {sns_response}")

            except json.JSONDecodeError:
                print(f"Body is not JSON. Handling as plain text: {body}")

        except Exception as e:
            print(f"Error processing record: {e}")

    return {
        'statusCode': 200,
        'body': json.dumps('Processing complete')
    }