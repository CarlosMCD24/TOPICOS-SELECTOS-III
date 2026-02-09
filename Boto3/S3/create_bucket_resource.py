import boto3

def create_bucket(bucket_name):
    bucket = boto3.resource('s3')

    response = bucket.create_bucket(
        Bucket = bucket_name,
        ACL="private", # default permissions, others: public-read (for user in a group), public-read-access 
        CreateBucketConfiguration={
            'LocationConstraint':'us-east-2'
        }
    )

    
    print(response)

if __name__ == '__main__':
    create_bucket(bucket_name="tsiii-ivant-ejercicios")