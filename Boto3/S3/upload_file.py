import boto3

def upload_files(file_name, bucket, object_name=None, args=None):
    
    s3_client = boto3.client('s3')

    if object_name is None:
        object_name = file_name

    s3_client.upload_file(file_name, bucket, object_name, ExtraArgs=args)
    print(f"{file_name} has been uploaded to {bucket} bucket")



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
    upload_files(file_name=file_name, bucket=bucket_name)