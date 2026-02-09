import boto3
import botocore.exceptions

def upload_files_encrypted(file_name, bucket, object_name=None, extra_args=None):
    
    s3_client = boto3.client('s3')

    if object_name is None:
        object_name = file_name

    # Ensure extra_args is not None and include encryption
    if extra_args is None:
        extra_args = {}

    extra_args['ServerSideEncryption'] = 'AES256'  # Enable AES-256 encryption

    s3_client.upload_file(file_name, bucket, object_name, ExtraArgs=extra_args)
    
    try:
        s3_client.upload_file(file_name, bucket, object_name, ExtraArgs=extra_args)
        print(f"{file_name} has been uploaded to {bucket}/{object_name} with AES-256 encryption")
    except botocore.exceptions.BotoCoreError as e:
        print(f"Upload failed: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")



# uploading with resource

# BUCKET_NAME =   "parwizforogh7777"

# s3_client = boto3.resource('s3')

# def upload_files(file_name, bucket, object_name=None, args=None):
#     if object_name is None:
#         object_name = file_name

#     s3_client.meta.client.upload_file(file_name, bucket, object_name, ExtraArgs=args)
#     print("{} has been uploaded to {} bucket".format(file_name, BUCKET_NAME))



# upload_files("myfile.txt", BUCKET_NAME)


if __name__ == '__main__':
    bucket_name = "tsiii-ivant-ejercicios"
    file_name = "mtcars.csv"
    upload_files_encrypted(file_name=file_name, bucket=bucket_name)