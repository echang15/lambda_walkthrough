import json
import boto3
import operator

def lambda_handler(event, context):
   

    client = boto3.client('s3')
    s3 = boto3.client('s3')
    data = s3.get_object(Bucket='ec-lamba-test', Key='fadetoblack.txt')
    contents = data['Body'].read().decode('utf-8') 
    
    words=contents.split()
    word_count = dict()
 
    for word in words:
        if word.lower() in word_count:
            word_count[word.lower()] += 1
        else:
            word_count[word.lower()]=1
    
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)


    return sorted_words
    
    #return contents
    #print(contents)


