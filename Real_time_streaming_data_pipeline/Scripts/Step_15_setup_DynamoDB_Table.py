import boto3

dynamodb = boto3.client('dynamodb')

response = dynamodb.create_table(
    TableName='ECommerceTransactions',
    KeySchema=[
        {'AttributeName': 'transaction_id', 'KeyType': 'HASH'},
    ],
    AttributeDefinitions=[
        {'AttributeName': 'transaction_id', 'AttributeType': 'N'},
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

print('Table created:', response['TableDescription']['TableName'])