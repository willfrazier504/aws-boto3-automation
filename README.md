# AWS Automation with Python and Boto3

Python scripts that automate common AWS tasks using Boto3.

## Scripts
| Script | What it does |
|---|---|
| `create_s3_bucket.py` | Creates a new S3 bucket |
| `list_s3_buckets.py` | Lists all S3 buckets in the account |
| `list_ec2_instances.py` | Lists EC2 instances and their current state |

## Setup
1. Install Python 3
2. Install Boto3: `pip install boto3`
3. Configure AWS credentials: `aws configure` (never put keys in the code)

## How to run
python create_s3_bucket.py
python list_s3_buckets.py
python list_ec2_instances.py

## Problems I solved
- **Python PATH conflict on Windows:** scripts wouldn't run until I fixed which Python interpreter the terminal was using.
- **S3 region error in us-east-1:** us-east-1 is the default region and doesn't accept a `LocationConstraint` setting, so I removed it from the create call.

## Skills
AWS (S3, EC2, IAM credentials), Python, Boto3, command line troubleshooting
