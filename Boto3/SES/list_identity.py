import boto3

def list_identity():
    ses_client = boto3.client('ses')

    response = ses_client.list_identities(
        IdentityType='EmailAddress'
    )

    print(response['Identities'])

if __name__ == '__main__':
    list_identity()