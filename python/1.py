import json
import boto3

def lambda_handler(event, context):
    # TODO implement

    client = boto3.client('s3')
    s3 = boto3.client('s3')
    data = s3.get_object(Bucket='ec-lamba-test', Key='fadetoblack.txt')
    contents = data['Body'].read().decode('utf-8') 
    return contents
    #print(contents)


