import boto3
from pprint import pprint

def describe_instance():
    rds_client = boto3.client('rds')

    response = rds_client.describe_db_instances(
        DBInstanceIdentifier = "rdstest"
    )

    pprint(response)

if __name__ == '__main__':
    describe_instance()