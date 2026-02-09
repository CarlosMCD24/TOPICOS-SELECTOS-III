import boto3
from pprint import pprint

def describe_sg():
    ec2_client = boto3.client('ec2')

    response = ec2_client.describe_security_groups()
    pprint(response)

if __name__ == '__main__':
    describe_sg()
