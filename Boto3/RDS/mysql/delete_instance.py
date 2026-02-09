import boto3

def delete_instance():

    rds_client = boto3.client('rds')

    response = rds_client.delete_db_instance(
        DBInstanceIdentifier="rdstest",
        SkipFinalSnapshot=True,
        #FinalDBSnapshotIdentifier="rdstest-final-snapshot", # if you want to make a final snapshot
        DeleteAutomatedBackups=True
    )

    print(response)

if __name__ == '__main__':
    delete_instance()