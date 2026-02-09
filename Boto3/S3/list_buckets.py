import boto3

# with client
#bucket = boto3.client('s3')

#response = bucket.list_buckets()

#print("Listing all buckets")

#for bucket in response['Buckets']:
#    print(bucket['Name'])

def list_buckets():
    resource = boto3.resource('s3')

    iterator = resource.buckets.all()

    print("Listing all buckets")

    for bucket in iterator:
        print(bucket.name)

if __name__ == '__main__':
    list_buckets()
