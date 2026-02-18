import boto3
import json
from botocore.exceptions import ClientError

# Funciones para crear un usuario en IAM usando boto3

def create_user(username:str):
    # Creamos un cliente IAM de boto3
    iam = boto3.client('iam')

    # crear usuario
    response = iam.create_user(UserName=username)
    print(response)

# Funcion para crear un grupo en IAM usando boto3

def create_group(group_name):
    iam = boto3.client('iam')
    iam.create_group(GroupName=group_name)

# Funcion para agregar un usuario a un grupo en IAM usando boto3
def add_user_to_group(username, group_name):
    iam = boto3.client('iam')

    response = iam.add_user_to_group(
        UserName=username,
        GroupName=group_name
    )

# Funcion para crear una política de solo lectura para un bucket de S3 en IAM usando boto3

def create_readonly_s3_policy(policy_name, bucket_name):
    iam = boto3.client("iam")

    policy_document = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": ["s3:ListAllMyBuckets"],
                "Resource": "*"
            },
            {
                "Effect": "Allow",
                "Action": ["s3:GetObject"],
                "Resource": f"arn:aws:s3:::{bucket_name}/*"
            }
        ]
    }

    try:
        response = iam.create_policy(
            PolicyName=policy_name,
            PolicyDocument=json.dumps(policy_document)
        )
        return response

    except ClientError as e:
        if e.response["Error"]["Code"] == "EntityAlreadyExists":
            print("La política ya existe.")
        else:
            raise e


    print(response)

# Funcion para agregar un usuario a un grupo en IAM usando boto3

def attach_policy(policy_arn, group_name):
    iam = boto3.client('iam')

    response = iam.attach_group_policy(
        GroupName=group_name,
        PolicyArn=policy_arn
    )

    print(response)

# Funcion para listar todos los usuarios en IAM usando boto3

def all_users():
    iam = boto3.client('iam')

    #paginator object
    #abstraction over the process of iterating over an entire result set of a truncated API operation.
    paginator = iam.get_paginator('list_users')

    for response in paginator.paginate():
        for user in response['Users']:
            username = user['UserName']
            Arn = user['Arn']
            print(f'Username : {username}, Arn : {Arn}')

# Funcion para actualizar el estado de una clave de acceso para un usuario en IAM usando boto3

def create_access(username):
    iam = boto3.client('iam')

    response = iam.create_access_key(
        UserName=username
    )

    print(response)

# Funcion para eliminar un usuario en IAM usando boto3

def detach_group(arn, user_group):
    iam = boto3.client('iam')

    response = iam.detach_group_policy(
        GroupName=user_group,
        PolicyArn = arn
    )

    print(response)

# Funcion para eliminar un usuario de un grupo en IAM usando boto3

def delete_user_group(username, groupName):
    iam = boto3.resource('iam')

    group = iam.Group(groupName)

    response = group.remove_user(
        UserName=username
    )

    print(response)

# Funcion para eliminar un usuario en IAM usando boto3
def delete_user(username):
    iam = boto3.client('iam')

    response = iam.delete_user(
        UserName=username
    )

    print(response)

# Listar access keys
def list_access_keys(username):
    iam = boto3.client("iam")
    return iam.list_access_keys(UserName=username)

# Eliminar access key
def delete_access_key(username, access_key_id):
    iam = boto3.client("iam")
    return iam.delete_access_key(
        UserName=username,
        AccessKeyId=access_key_id
    )

# Listar políticas adjuntas a usuario
def list_user_policies(username):
    iam = boto3.client("iam")
    return iam.list_attached_user_policies(UserName=username)

# Desadjuntar política de usuario
def detach_user_policy(username, policy_arn):
    iam = boto3.client("iam")
    return iam.detach_user_policy(
        UserName=username,
        PolicyArn=policy_arn
    )

# Listar políticas del grupo
def list_group_policies(group_name):
    iam = boto3.client("iam")
    return iam.list_attached_group_policies(GroupName=group_name)

# Eliminar grupo
def delete_group(group_name):
    iam = boto3.client("iam")
    return iam.delete_group(GroupName=group_name)

# Eliminar policy personalizada
def delete_policy(policy_arn):
    iam = boto3.client("iam")
    return iam.delete_policy(PolicyArn=policy_arn)

