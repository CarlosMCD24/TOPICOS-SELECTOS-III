import boto3
import json

iam = boto3.client('iam')

role_name = "FlinkKinesisRole"
assume_role_policy = {
    "Version": "2012-10-17",
    "Statement": [{
        "Effect": "Allow",
        "Principal": {
            "Service": "kinesisanalytics.amazonaws.com"
        },
        "Action": "sts:AssumeRole"
    }]
}

# Create the role
try:
    iam.create_role(
        RoleName=role_name,
        AssumeRolePolicyDocument=json.dumps(assume_role_policy)
    )
    print(f"Created IAM role: {role_name}")
except iam.exceptions.EntityAlreadyExistsException:
    print(f"IAM role {role_name} already exists.")

# Attach managed policy
iam.attach_role_policy(
    RoleName=role_name,
    PolicyArn='arn:aws:iam::aws:policy/AmazonKinesisFullAccess'
)

iam.attach_role_policy(
    RoleName=role_name,
    PolicyArn='arn:aws:iam::aws:policy/AWSGlueConsoleFullAccess'
)

iam.attach_role_policy(
    RoleName=role_name,
    PolicyArn='arn:aws:iam::aws:policy/CloudWatchLogsFullAccess'
)
print("Attached policies.")

