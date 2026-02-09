import boto3

def create_user(username:str):
    # Creamos un cliente IAM de boto3
    iam = boto3.client('iam')

    # crear usuario
    response = iam.create_user(UserName=username)
    print(response)


if __name__ == '__main__':
    create_user('testuser')