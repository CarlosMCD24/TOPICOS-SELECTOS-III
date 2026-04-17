import boto3
import json
import zipfile
import time

REGION = 'us-east-2'
FUNCTION_NAME = 'KinesisOrderAlarm'
ROLE_NAME = 'Lambda-Kinesis-SNS-Alarm-Role'
STREAM_NAME = 'Clientorders'

def create_role():
    iam = boto3.client('iam')

    trust_policy = {
        "Version": "2012-10-17",
        "Statement": [{
            "Effect": "Allow",
            "Principal": {"Service": "lambda.amazonaws.com"},
            "Action": "sts:AssumeRole"
        }]
    }

    try:
        role = iam.create_role(
            RoleName=ROLE_NAME,
            AssumeRolePolicyDocument=json.dumps(trust_policy)
        )
        role_arn = role['Role']['Arn']
        print(f'Role {ROLE_NAME} created: {role_arn}')
        time.sleep(10)
    except iam.exceptions.EntityAlreadyExistsException:
        role_arn = iam.get_role(RoleName=ROLE_NAME)['Role']['Arn']
        print(f'Role {ROLE_NAME} already exists: {role_arn}')

    inline_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": ["kinesis:GetRecords", "kinesis:GetShardIterator",
                           "kinesis:DescribeStream", "kinesis:ListStreams"],
                "Resource": f"arn:aws:kinesis:{REGION}:*:stream/{STREAM_NAME}"
            },
            {
                "Effect": "Allow",
                "Action": "sns:Publish",
                "Resource": "*"
            },
            {
                "Effect": "Allow",
                "Action": ["logs:CreateLogGroup", "logs:CreateLogStream", "logs:PutLogEvents"],
                "Resource": "arn:aws:logs:*:*:*"
            }
        ]
    }

    iam.put_role_policy(
        RoleName=ROLE_NAME,
        PolicyName='LambdaKinesisSNSPolicy',
        PolicyDocument=json.dumps(inline_policy)
    )
    print('Policies attached.')
    return role_arn

def create_function(role_arn):
    lambda_client = boto3.client('lambda', region_name=REGION)

    zip_path = '/tmp/lambda_alarm.zip'
    with zipfile.ZipFile(zip_path, 'w') as zf:
        zf.write('lambda_alarm.py', 'lambda_alarm.py')

    with open(zip_path, 'rb') as f:
        zip_content = f.read()

    try:
        response = lambda_client.create_function(
            FunctionName=FUNCTION_NAME,
            Runtime='python3.9',
            Role=role_arn,
            Handler='lambda_alarm.lambda_handler',
            Code={'ZipFile': zip_content},
            Timeout=60,
            MemorySize=128
        )
        print(f'Lambda {FUNCTION_NAME} created: {response["FunctionArn"]}')
        return response['FunctionArn']
    except lambda_client.exceptions.ResourceConflictException:
        response = lambda_client.get_function(FunctionName=FUNCTION_NAME)
        print(f'Lambda {FUNCTION_NAME} already exists.')
        return response['Configuration']['FunctionArn']

def add_kinesis_trigger():
    lambda_client = boto3.client('lambda', region_name=REGION)
    kinesis_client = boto3.client('kinesis', region_name=REGION)

    stream_arn = kinesis_client.describe_stream(StreamName=STREAM_NAME)['StreamDescription']['StreamARN']

    try:
        response = lambda_client.create_event_source_mapping(
            EventSourceArn=stream_arn,
            FunctionName=FUNCTION_NAME,
            StartingPosition='LATEST',
            BatchSize=100,
            # 10-second tumbling window — replicates the SQL sliding window logic
            TumblingWindowInSeconds=10
        )
        print(f'Kinesis trigger added. UUID: {response["UUID"]}')
    except lambda_client.exceptions.ResourceConflictException:
        print('Kinesis trigger already exists.')

if __name__ == '__main__':
    print('Creating IAM role...')
    role_arn = create_role()

    print('\nCreating Lambda function...')
    create_function(role_arn)

    print('\nAdding Kinesis trigger...')
    add_kinesis_trigger()

    print(f'\n✓ Done. Lambda "{FUNCTION_NAME}" is now monitoring stream "{STREAM_NAME}".')
