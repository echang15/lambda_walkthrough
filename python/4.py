import json
import boto3
import operator
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    files = event['files'].split()

    client = boto3.client('s3')
    s3 = boto3.client('s3')
 
    
    word_count = dict()
    
    for f in files:
        #print(f)
        try:
            data = s3.get_object(Bucket='ec-lamba-test', Key=f)
            contents = data['Body'].read().decode('utf-8') 
            words=contents.split()
       
     
            for word in words:
                if word.lower() in word_count:
                    word_count[word.lower()] += 1
                else:
                    word_count[word.lower()]=1
        except ClientError as e:
            print(e)
    
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)


    return sorted_words
    
    #return contents
    #print(contents)


