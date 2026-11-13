import boto3

s3 = boto3.client('s3')
bucket_name = 'my-new-bucket-2026'
s3.create_bucket(Bucket=bucket_name)
print('Bucket created successfully')