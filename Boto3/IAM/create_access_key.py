import boto3


def create_access(username):
    iam = boto3.client('iam')

    response = iam.create_access_key(
        UserName=username
    )

    print(response)


def update_access():
    iam = boto3.client('iam')
    iam.update_access_key(
        AccessKeyId='AKIARSTBXIQFPSB43477',
        Status='Inactive',
        UserName='testuser'

    )

if __name__ == '__main__':
    #create_access(username='testuser')
    update_access()




