import boto3

def lambda_handler(event, context):
    ddbClient = boto3.resource('dynamodb')
    ddbTable = ddbClient.Table('Pets')
    response = ddbTable.put_item(
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
        'statusCode': response['ResponseMetadata']['HTTPStatusCode'],
        'body': 'Record ' + event['id'] + ' Added'
    }