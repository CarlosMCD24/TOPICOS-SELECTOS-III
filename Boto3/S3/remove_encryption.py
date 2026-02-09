import boto3


def remove_encryption(bucket_name):

    s3_client = boto3.client('s3')
    response = s3_client.delete_bucket_encryption(Bucket=bucket_name)
    print(response)


if __name__ == '__main__':
    bucket_name = "tsiii-ivant-ejercicios"
    remove_encryption(bucket_name=bucket_name)
