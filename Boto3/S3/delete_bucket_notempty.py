import boto3

def delete_bucket(bucket_name):

    bucket_name = bucket_name

    s3_resource = boto3.resource('s3')

    s3_bucket = s3_resource.Bucket(bucket_name)


    def clean_up():

        #delete the object
        for s3_object in s3_bucket.objects.all():
            s3_object.delete()


        #delete bucket versioning
        for s3_object_ver in s3_bucket.object_versions.all():
            s3_object_ver.delete()

        print("S3 bucket cleaned")


    clean_up()

    s3_bucket.delete()

    print(f"The bucket {bucket_name} has been deleted")

if __name__ == '__main__':
    delete_bucket(bucket_name='tsiii-ivant-ejercicios-copy')