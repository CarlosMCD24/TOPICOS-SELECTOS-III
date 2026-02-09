import boto3
from pprint import pprint

DB_INSTANCE_ID = "mlflow-db"
DB_NAME = "mlflow_db"
USERNAME = "mlflow"
PASSWORD = "password"

def create_instance():
    rds_client = boto3.client('rds')

    response = rds_client.create_db_instance(
        DBName=DB_NAME,  # PostgreSQL requires lowercase db names
        DBInstanceIdentifier=DB_INSTANCE_ID,
        AllocatedStorage=20,
        DBInstanceClass='db.t3.micro',
        Engine='postgres',
        MasterUsername=USERNAME,
        MasterUserPassword=PASSWORD,
        Port=5432,
        EngineVersion='17.2',  # You can change to another supported version if needed
        PubliclyAccessible=True,
        StorageType='gp2',
        BackupRetentionPeriod=0  # No automated backups
    )

    pprint(response)

def wait_until_available():
    rds_client = boto3.client('rds')
    print("Waiting for RDS instance to be available...")
    waiter = rds_client.get_waiter('db_instance_available')
    waiter.wait(DBInstanceIdentifier=DB_INSTANCE_ID)
    response = rds_client.describe_db_instances(DBInstanceIdentifier=DB_INSTANCE_ID)
    endpoint = response['DBInstances'][0]['Endpoint']['Address']
    print(f"RDS is available at: {endpoint}")
    return endpoint


if __name__ == '__main__':
    create_instance()
    endpoint = wait_until_available()
