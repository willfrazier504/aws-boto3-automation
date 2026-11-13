AWS Automation with Python and Boto3
Python scripts that work with AWS through Boto3.

create_s3_bucket.py - creates an S3 bucket
list_s3_buckets.py - lists all S3 buckets in the account

Setup: Python 3, pip install boto3, AWS credentials configured with the AWS CLI or environment variables.

Problems I solved: a Python PATH/interpreter conflict on Windows, and an S3 region error in us-east-1 (us-east-1 doesn’t accept a LocationConstraint setting).
