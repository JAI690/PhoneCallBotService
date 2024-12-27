import json
from vonage import Vonage, Auth
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('CallDetails')

    for record in event['Records']:
        body = json.loads(record['body'])
        phone_number = body['phone_number']
        timestamp = body['timestamp']
        message = body['message']

        try:
            auth = Auth(application_id="YOUR_APP_ID", private_key="YOUR_PRIVATE_KEY")
            vonage_client = Vonage(auth=auth)
            ncco = [{"action": "talk", "text": message}]

            response = vonage_client.voice.create_call({
                "to": [{"type": "phone", "number": phone_number}],
                "ncco": ncco
            })

            table.put_item(Item={
                "CallID": response["uuid"],
                "PhoneNumber": phone_number,
                "Timestamp": timestamp,
                "Status": "Success",
                "Message": message
            })
        except Exception as e:
            print(f"Error processing call for {phone_number}: {e}")
