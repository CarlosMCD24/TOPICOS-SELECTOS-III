import boto3


# with boto3 client
# client = boto3.client('s3')

# bucket_name = "parwizforogh7777"

# client.delete_bucket(Bucket=bucket_name)

# print("S3 Bucket has been deleted")


#Delete bucket with aws resource

def delete_bucket(bucket_name):
    resource = boto3.resource('s3')

    bucket_name = bucket_name

    s3_bucket =resource.Bucket(bucket_name)

    s3_bucket.delete()

    print(f" The bucket {s3_bucket} has been deleted  ")

if __name__ == '__main__':
    delete_bucket(bucket_name='tsiii-ivant-ejercicios')
