import boto3


def upload_image(path):
    client = boto3.client('s3')


    with open(path, 'rb') as f:
        data = f.read()


    response = client.put_object(
        ACL="private",
        Bucket = "tsiii-ivant-ejercicios",
        Body=data,
        Key='coffee.png'

    )

    print(response)

if __name__ == '__main__':
    upload_image('coffee.png')