import boto3

def object_summary(bucket_name, object_key):
    s3 = boto3.resource('s3')

    object_summary = s3.ObjectSummary(bucket_name, object_key)

    print(object_summary.bucket_name)
    print(object_summary.key)

if __name__ == '__main__':
    bucket_name = "tsiii-ivant-ejercicios"
    object_key = "mtcars.csv"
    object_summary(bucket_name=bucket_name, object_key=object_key)