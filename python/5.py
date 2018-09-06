import json
import boto3

lambda_client = boto3.client('lambda')


def lambda_handler(event, context):
    files = event['files'].split()

    complete_return = ''
    for f in files:
        payload = { 'filename': f }
        invoke_response = lambda_client.invoke(FunctionName="ec-read-files-from-s3-pt3",
                                           InvocationType='RequestResponse',
                                           Payload = json.dumps(payload)
                                           )
        txt_response = invoke_response['Payload'].read()
        complete_return += str(txt_response)

    return str(complete_return)

