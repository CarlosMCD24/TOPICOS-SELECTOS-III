import boto3

def download_file(file_name,bucket_name):
    s3_resource = boto3.resource('s3')

    s3_object = s3_resource.Object(bucket_name, file_name)

    s3_object.download_file('s3_file.csv')

    print(f"File {file_name} has been downloaded")

if __name__ == '__main__':
    download_file(file_name='mtcars.csv', bucket_name='tsiii-ivant-ejercicios')
