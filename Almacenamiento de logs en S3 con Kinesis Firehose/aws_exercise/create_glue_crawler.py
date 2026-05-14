import boto3
import json
import time

# Configuration
REGION = 'us-east-2'
BUCKET_NAME = 'ecom-purchaselogs-bucket'
GLUE_DB_NAME = 'ecom_logs_db'
CRAWLER_NAME = 'ecom-logs-crawler'
CRAWLER_ROLE_NAME = 'GlueCrawlerRole'

def create_glue_role():
    iam = boto3.client('iam')

    trust_policy = {
        "Version": "2012-10-17",
        "Statement": [{
            "Effect": "Allow",
            "Principal": {"Service": "glue.amazonaws.com"},
            "Action": "sts:AssumeRole"
        }]
    }

    try:
        role_arn = iam.create_role(
            RoleName=CRAWLER_ROLE_NAME,
            AssumeRolePolicyDocument=json.dumps(trust_policy),
            Description='Role for Glue Crawler to read S3'
        )['Role']['Arn']
        print(f'Role {CRAWLER_ROLE_NAME} created: {role_arn}')
        time.sleep(10)
    except iam.exceptions.EntityAlreadyExistsException:
        role_arn = iam.get_role(RoleName=CRAWLER_ROLE_NAME)['Role']['Arn']
        print(f'Role {CRAWLER_ROLE_NAME} already exists: {role_arn}')

    # AWSGlueServiceRole tiene los permisos base de Glue (logs, etc.)
    iam.attach_role_policy(
        RoleName=CRAWLER_ROLE_NAME,
        PolicyArn='arn:aws:iam::aws:policy/service-role/AWSGlueServiceRole'
    )

    # Permiso adicional para leer el bucket S3
    iam.put_role_policy(
        RoleName=CRAWLER_ROLE_NAME,
        PolicyName='GlueCrawlerS3Policy',
        PolicyDocument=json.dumps({
            "Version": "2012-10-17",
            "Statement": [{
                "Effect": "Allow",
                "Action": ["s3:GetObject", "s3:ListBucket"],
                "Resource": [
                    f"arn:aws:s3:::{BUCKET_NAME}",
                    f"arn:aws:s3:::{BUCKET_NAME}/*"
                ]
            }]
        })
    )
    print('Policies attached to role')
    return role_arn

def create_glue_database():
    glue = boto3.client('glue', region_name=REGION)

    try:
        glue.create_database(DatabaseInput={'Name': GLUE_DB_NAME})
        print(f'Glue database "{GLUE_DB_NAME}" created')
    except glue.exceptions.AlreadyExistsException:
        print(f'Glue database "{GLUE_DB_NAME}" already exists')

def create_crawler(role_arn):
    glue = boto3.client('glue', region_name=REGION)

    try:
        glue.create_crawler(
            Name=CRAWLER_NAME,
            Role=role_arn,
            DatabaseName=GLUE_DB_NAME,
            # Le decimos al crawler dónde están los datos en S3
            Targets={'S3Targets': [{'Path': f's3://{BUCKET_NAME}/logs/'}]},
            # Cada vez que corra, actualiza el esquema si cambia
            SchemaChangePolicy={
                'UpdateBehavior': 'UPDATE_IN_DATABASE',
                'DeleteBehavior': 'LOG'
            }
        )
        print(f'Crawler "{CRAWLER_NAME}" created')
    except glue.exceptions.AlreadyExistsException:
        print(f'Crawler "{CRAWLER_NAME}" already exists')

def run_crawler():
    glue = boto3.client('glue', region_name=REGION)

    glue.start_crawler(Name=CRAWLER_NAME)
    print(f'Crawler "{CRAWLER_NAME}" started. Waiting for it to finish...')

    # Esperar a que termine
    while True:
        state = glue.get_crawler(Name=CRAWLER_NAME)['Crawler']['State']
        if state == 'READY':
            print('Crawler finished successfully')
            break
        print(f'  State: {state}...')
        time.sleep(10)

    # Mostrar las tablas que encontró
    tables = glue.get_tables(DatabaseName=GLUE_DB_NAME)['TableList']
    print(f'\nTables discovered in "{GLUE_DB_NAME}":')
    for table in tables:
        print(f'  - {table["Name"]} ({len(table["StorageDescriptor"]["Columns"])} columns)')

if __name__ == '__main__':
    print('Creating IAM role for Glue...')
    role_arn = create_glue_role()

    print('\nCreating Glue database...')
    create_glue_database()

    print('\nCreating Glue Crawler...')
    create_crawler(role_arn)

    print('\nRunning crawler...')
    run_crawler()

    print(f'\n✓ Done. Database "{GLUE_DB_NAME}" is ready to query with Athena.')
