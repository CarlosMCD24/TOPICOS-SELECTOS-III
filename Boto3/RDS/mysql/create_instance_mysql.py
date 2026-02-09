import boto3
from pprint import pprint

def create_instance():

    rds_client = boto3.client('rds')


    response = rds_client.create_db_instance(
        DBName="rdstest",
        DBInstanceIdentifier="rdstest",
        AllocatedStorage=20,
        DBInstanceClass='db.t3.micro',
        Engine='MySQL',
        MasterUsername='admin',
        MasterUserPassword='password',
        Port=3306,
        EngineVersion='8.0.32',
        PubliclyAccessible=True,
        StorageType='gp2',
        BackupRetentionPeriod=0  # ← disables automated backups, but also disables point-in-time recovery. Only for test, not production
    )

    pprint(response)

if __name__ == '__main__':
    create_instance()