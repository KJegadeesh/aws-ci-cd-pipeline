import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table_name = os.environ['TABLE_NAME']
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    body = json.loads(event['body'])
    name = body.get('name')
    email = body.get('email')
    message = body.get('message')

    table.put_item(
        Item={
            'email': email,
            'name': name,
            'message': message
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Form submitted successfully'})
    }
