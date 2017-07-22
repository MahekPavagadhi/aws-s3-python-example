import boto3
from botocore.client import Config
 
ID = 'xxxx' #AWS access ID
SECRET = 'xxx' #AWS secret access key
BUCKET_NAME = 'xxxxx' #s3 Bucket name

data = open('agne.jpg', 'rb')

s3 = boto3.resource(
    's3',
    aws_access_key_id=ID,
    aws_secret_access_key=SECRET,
    config=Config(signature_version='s3v4')
)
s3.Bucket(BUCKET_NAME).put_object(Key='agne.jpg', Body=data)

print ("Done")
