import boto3
import csv
import json

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    sqs = boto3.client('sqs')

    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']
    queue_url = "https://sqs.us-east-1.amazonaws.com/YOUR_ACCOUNT_ID/calls-queue"

    response = s3.get_object(Bucket=bucket_name, Key=object_key)
    content = response['Body'].read().decode('utf-8')

    reader = csv.DictReader(content.splitlines())
    for row in reader:
        message = {
            "phone_number": row['phone_number'],
            "timestamp": row['timestamp'],
            "message": row['message']
        }
        sqs.send_message(QueueUrl=queue_url, MessageBody=json.dumps(message))
    return {"status": "File processed"}
