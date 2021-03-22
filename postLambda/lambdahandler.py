import boto3
import json


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Pets')
    print(event)
    response = table.put_item(
        Item={
            'id': event['id'],
            'name': event['name'],

        }
    )
    return response
#    {
#        'statusCode': 200,
#        'body': json.dumps('Hello from Lambda!')
#    }