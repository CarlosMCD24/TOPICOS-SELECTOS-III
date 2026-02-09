import boto3
from pprint import pprint

def create_instance():
    rds_client = boto3.client('rds')

    response = rds_client.create_db_instance(
        DBName="rdstest",  # PostgreSQL requires lowercase db names
        DBInstanceIdentifier="rdstest",
        AllocatedStorage=20,
        DBInstanceClass='db.t3.micro',
        Engine='postgres',
        MasterUsername='admins',
        MasterUserPassword='password',
        Port=5432,
        EngineVersion='17.2',  # You can change to another supported version if needed
        PubliclyAccessible=True,
        StorageType='gp2',
        BackupRetentionPeriod=0  # No automated backups
    )

    pprint(response)

if __name__ == '__main__':
    create_instance()
