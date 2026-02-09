import boto3

def list_files_prefix(bucket_name, prefix):

    s3_resource = boto3.resource('s3')

    s3_bucket = s3_resource.Bucket(bucket_name)

    print("Listing Filtered File")

    for obj in s3_bucket.objects.filter(Prefix=prefix):
        print(obj.key)

if __name__ == '__main__':
    bucket_name = "tsiii-ivant-ejercicios"
    prefix = "bebidas"
    list_files_prefix(bucket_name=bucket_name, prefix=prefix)
