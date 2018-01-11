import boto3
import config
import json

def queue_repo(repo):
    aws_client = boto3.client('sqs', region_name=config.sqs['region'])

    response = aws_client.send_message(
        QueueUrl=config.sqs['repo_url'],
        MessageBody=json.dumps({'repo': repo}),
    )

    return response
