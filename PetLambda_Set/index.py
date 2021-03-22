import boto3
import json

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Pets')
    response = table.put_item(
        Item={
            'id': event['id'],
            'name': event['name'],
            'breed': event['breed'],
            'gender': event['gender'],
            'owner': event['owner'],
            'birthday': event['birthday']
        }
    )
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }