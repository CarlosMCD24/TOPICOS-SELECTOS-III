import boto3

def delete_object(bucket_name, object_keys):

    client = boto3.client('s3')

    objects_to_delete = [{'Key': key} for key in object_keys]
    
    response = client.delete_objects(
        Bucket=bucket_name,
        Delete={'Objects': objects_to_delete}
    )

    print(response)

if __name__ == '__main__':
    bucket_name = "tsiii-ivant-ejercicios"
    object_keys = ['mtcars.csv', 'coffee.png']
    delete_object(bucket_name=bucket_name, object_keys=object_keys)