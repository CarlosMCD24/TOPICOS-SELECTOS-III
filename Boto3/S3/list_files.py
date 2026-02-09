import boto3

def list_files(bucket_name):
    s3_resource = boto3.resource('s3')

    s3_bucket = s3_resource.Bucket(bucket_name)

    print("Listing Bucket Files or Objects")

    for obj in s3_bucket.objects.all():
        print(obj.key)

if __name__ == '__main__':
    bucket_name = "tsiii-ivant-ejercicios"
    list_files(bucket_name=bucket_name)