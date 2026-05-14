import boto3

REGION = 'us-east-2'
RESULTS_BUCKET = 'ecom-athena-results'
WORKGROUP_NAME = 'ecom-workgroup'

def create_results_bucket(s3):
    try:
        if REGION == 'us-east-1':
            s3.create_bucket(Bucket=RESULTS_BUCKET)
        else:
            s3.create_bucket(
                Bucket=RESULTS_BUCKET,
                CreateBucketConfiguration={'LocationConstraint': REGION}
            )
        print(f'Bucket "{RESULTS_BUCKET}" created')
    except s3.exceptions.BucketAlreadyOwnedByYou:
        print(f'Bucket "{RESULTS_BUCKET}" already exists')

def create_workgroup(athena):
    try:
        athena.create_work_group(
            Name=WORKGROUP_NAME,
            Configuration={
                'ResultConfiguration': {
                    'OutputLocation': f's3://{RESULTS_BUCKET}/results/'
                },
                'EnforceWorkGroupConfiguration': True,
                'PublishCloudWatchMetricsEnabled': False,
            },
            Description='Workgroup for ecom pipeline queries'
        )
        print(f'Workgroup "{WORKGROUP_NAME}" created')
    except athena.exceptions.InvalidRequestException as e:
        if 'already exists' in str(e):
            print(f'Workgroup "{WORKGROUP_NAME}" already exists')
        else:
            raise

if __name__ == '__main__':
    s3 = boto3.client('s3', region_name=REGION)
    athena = boto3.client('athena', region_name=REGION)

    print('Creating S3 bucket for Athena results...')
    create_results_bucket(s3)

    print('Creating Athena workgroup...')
    create_workgroup(athena)

    print(f'\n✓ Athena workgroup "{WORKGROUP_NAME}" ready.')
    print(f'  Results will be stored in s3://{RESULTS_BUCKET}/results/')
    print(f'\nExample query to run in Athena (workgroup: {WORKGROUP_NAME}):')
    print("  SELECT country, COUNT(*) as orders FROM ecom_logs_db.purchase_logs GROUP BY country ORDER BY orders DESC LIMIT 10;")
