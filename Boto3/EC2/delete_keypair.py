import boto3

def delete_key_pair(key_name):
    ec2_client = boto3.client('ec2')

    response = ec2_client.delete_key_pair(
        KeyName=key_name
    )

    print(response)

if __name__ == '__main__':
    key_name = 'mykey'
    delete_key_pair(key_name=key_name)
