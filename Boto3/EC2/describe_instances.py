import boto3
from pprint import pprint

def describe_instances():
    ec2_client = boto3.client('ec2')

    response = ec2_client.describe_instances()

    pprint(response)

if __name__ == '__main__':
    describe_instances()
