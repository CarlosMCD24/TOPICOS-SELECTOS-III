import boto3
from pprint import pprint

def create_key_pair(key_name, key_type, store=False):
    ec2_client = boto3.client('ec2')

    resp = ec2_client.create_key_pair(
        KeyName = key_name,
        KeyType= key_type
    )

    #pprint(resp['KeyMaterial'])

    #store the pem file
    if store:
        file = open('mykey.pem', 'w')
        file.write(resp['KeyMaterial'])
        file.close()

if __name__ == '__main__':
    key_name = 'tsii_key'
    key_type = 'rsa'

    create_key_pair(key_name=key_name, key_type=key_type,store=False)