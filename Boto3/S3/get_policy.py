
import boto3

def get_policy(bucket_name):

    s3_client = boto3.client('s3')

    response = s3_client.get_bucket_policy(Bucket=bucket_name)
    print(response['Policy'])

if __name__ == '__main__':
    bucket_name = "tsiii-ivant-ejercicios"
    get_policy(bucket_name=bucket_name)
