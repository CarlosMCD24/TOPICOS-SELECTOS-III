import boto3


def add_user(username, group_name):
    iam = boto3.client('iam')

    response = iam.add_user_to_group(
        UserName=username,
        GroupName=group_name
    )

    print(response)


if __name__ == '__main__':
    add_user('testuser', 'S3Admins')
