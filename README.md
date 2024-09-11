# Real-Time Data Processing Pipeline

![Real-Time Data Pipeline](https://github.com/Jahnavi-Th/real-time-data-processing-pipeline/blob/main/Real_time_data_pipeline.webp "Real-Time Data Pipeline")

## Objective
Build a real-time data processing pipeline for e-commerce transactions.

## Overview
This project involves creating a real-time data processing pipeline using AWS services to handle and analyze e-commerce transaction data. The pipeline includes data collection, processing, storage, and monitoring components. The pipeline is designed to efficiently process transaction data in real-time and trigger notifications.

## Architecture

### 1. Data Collection
- **Source**: E-commerce transaction events.
- **Service**: Amazon Simple Queue Service (SQS) for queueing transaction events.

### 2. Data Processing
- **Service**: AWS Lambda for processing transaction data from the SQS queue.
- **Tasks**:
  - Parse incoming messages.
  - Transform and validate data.
  - Store processed data in DynamoDB.

### 3. Data Storage
- **Service**: Amazon DynamoDB for storing processed transaction data.

### 4. Notifications
- **Service**: Amazon Simple Notification Service (SNS) for sending notifications about transactions.

### 5. Monitoring
- **Service**: Amazon CloudWatch for monitoring Lambda execution and setting up alarms.

## Steps Followed
- Configured AWS SDK.
- Created all the required IAM policies, attached them to corresponding roles and IAM users, and verified them.
- Set up SQS, SNS, DynamoDB Table, CloudWatch alarms, and metrics.
- Developed `lambda_function.py` (located in the `lambda_function` folder), zipped, and deployed using the respective `.py` files.
- Created `sqs_queue_policy`, updated visibility timeout, and set up Lambda SQS Trigger.
- Ran a sample `sqs_test.py` file to test the trigger, which ran successfully.
- Subscribed Lambda to SNS and published a message to SNS to send a notification if the transaction amount exceeds 1000.
- Continuously monitored logs in CloudWatch.

## Components

### 1. Amazon SQS
- **Queue Name**: ECommerceTransactionsQueue
- **Purpose**: To receive and queue transaction messages for processing.

### 2. AWS Lambda
- **Function Name**: AssignmentOneFunction
- **Trigger**: Linked to the SQS queue.
- **Purpose**:
  - Parse and process transaction messages.
  - Store data in DynamoDB.
  - Send notifications via SNS.

### 3. Amazon DynamoDB
- **Table Name**: ECommerceTransactions
- **Purpose**: To store processed transaction data.

### 4. Amazon SNS
- **Topic Name**: ECommerceNotificationsTopic
- **Purpose**: To send notifications about transactions.
- **ARN**: `arn:aws:sns:us-east-1:************`

### 5. Amazon CloudWatch
- **Purpose**:
  - Monitor Lambda function performance and errors.
  - Create custom metrics for monitoring.

## Testing

### 1. SQS Sample Test
- Run `sqs_input_test.py` to send input and test the Lambda Trigger.

### 2. Publish a Test Message
- Use AWS CLI or AWS Management Console to publish a test message to the SNS topic:
  ```bash
  aws sns publish --topic-arn arn:aws:sns:us-east-1:************:ECommerceNotificationsTopic \
    --message '{"transaction_id": 12345, "amount": 100, "timestamp": "2024-08-09T12:34:56Z"}' \
    --subject "Transaction Alert" \
    --message-attributes '{"TransactionType": {"DataType": "String", "StringValue": "Purchase"}}'
  > **Note**: Replace `************` with your IAM User ID.

### 3. Verify Processing
- Check DynamoDB for the stored transaction data.
- Verify that the Lambda function executed correctly.
- Check CloudWatch for logs and metrics.

## Troubleshooting

### Common Issues
- **Missing Permissions**: Ensure the IAM roles associated with Lambda, SNS, and DynamoDB have the necessary permissions.
- **Message Format**: Ensure the message format sent to SQS and SNS matches the expected format in the Lambda function.
- **Lambda Execution Errors**: Check Lambda logs in CloudWatch for error details.

## Conclusion
This project demonstrates the creation of a real-time data processing pipeline using AWS services. The pipeline efficiently processes and stores e-commerce transaction data and provides real-time notifications.


  
