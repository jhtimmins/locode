import boto3
import config
import json


def send_message(repo):
    aws_client = boto3.client('sqs', region_name=config.sqs['region'])

    response = aws_client.send_message(
        QueueUrl=config.sqs['url'],
        MessageBody=json.dumps({'repo': repo}),
    )

    return response
