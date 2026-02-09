import boto3

def copy_object(bucket_origin, bucket_destination, object_key, object_key_destination):
    s3 = boto3.resource('s3')

    copy_source = {
        'Bucket':bucket_origin,
        'Key':object_key
    }

    s3.meta.client.copy(copy_source, bucket_destination, object_key_destination)

if __name__ == '__main__':
    bucket_origin = "tsiii-ivant-ejercicios"
    bucket_destination = "tsiii-ivant-ejercicios-copy"
    object_key = "mtcars.csv"
    object_key_destination = "mtcars.csv"
    copy_object(bucket_origin=bucket_origin, bucket_destination=bucket_destination, object_key=object_key, object_key_destination=object_key_destination)
