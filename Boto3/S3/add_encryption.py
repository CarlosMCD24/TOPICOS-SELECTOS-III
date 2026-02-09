import boto3

def set_encryption(bucket_name):

    s3_client = boto3.client('s3')

    response = s3_client.put_bucket_encryption(
        Bucket=bucket_name,
        ServerSideEncryptionConfiguration={
            "Rules":[
                {"ApplyServerSideEncryptionByDefault": {"SSEAlgorithm" : "AES256"}}
            ]
        }
    )

    print(response)

if __name__ == '__main__':
    bucket_name = "tsiii-ivant-ejercicios"
    set_encryption(bucket_name=bucket_name)