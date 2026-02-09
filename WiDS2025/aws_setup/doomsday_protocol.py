import boto3

def terminate_instance(instance_id):
    ec2_client = boto3.client('ec2')
    response = ec2_client.terminate_instances(InstanceIds=[instance_id])
    print(response)

def delete_bucket(bucket_name):
    bucket_name = bucket_name
    s3_resource = boto3.resource('s3')
    s3_bucket = s3_resource.Bucket(bucket_name)

    def clean_up():
        #delete the object
        for s3_object in s3_bucket.objects.all():
            s3_object.delete()
        #delete bucket versioning
        for s3_object_ver in s3_bucket.object_versions.all():
            s3_object_ver.delete()
        print("S3 bucket cleaned")

    clean_up()

    s3_bucket.delete()

    print(f"The bucket {bucket_name} has been deleted")

def delete_instance(db_id):

    rds_client = boto3.client('rds')

    response = rds_client.delete_db_instance(
        DBInstanceIdentifier=db_id,
        SkipFinalSnapshot=True,
        #FinalDBSnapshotIdentifier="rdstest-final-snapshot", # if you want to make a final snapshot
        DeleteAutomatedBackups=True
    )

    print(response)

if __name__ == '__main__':
    instance_id = 'i-0d4dcb8fb67a6d0d3'
    db_id = 'mlflow-db'
    terminate_instance(instance_id=instance_id)
    delete_bucket(bucket_name='tsiii-ivant-mlflow-artifacts-remote')
    delete_instance(db_id=db_id)