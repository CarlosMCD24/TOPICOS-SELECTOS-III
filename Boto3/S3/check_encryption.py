import boto3
from botocore.exceptions import ClientError


def check_encryption(bucket_name):
    s3_client = boto3.client('s3')

    try:
        response = s3_client.get_bucket_encryption(Bucket=bucket_name)
        print(response)

    except ClientError as e:
        print("No encryption is available in this bucket")


if __name__ == '__main__':
    bucket_name = "tsiii-ivant-ejercicios"
    check_encryption(bucket_name=bucket_name)