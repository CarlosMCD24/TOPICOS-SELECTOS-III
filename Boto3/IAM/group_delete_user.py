import boto3

def delete_user_group(username, groupName):
    iam = boto3.resource('iam')

    group = iam.Group(groupName)

    response = group.remove_user(
        UserName=username
    )

    print(response)


if __name__ == '__main__':
    delete_user_group('testuser', 'S3Admins')