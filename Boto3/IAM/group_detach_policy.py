import boto3


def detach_group(arn, user_group):
    iam = boto3.client('iam')

    response = iam.detach_group_policy(
        GroupName=user_group,
        PolicyArn = arn
    )

    print(response)

if __name__ == '__main__':
    detach_group('arn:aws:iam::108652872714:policy/pyFullAccess','S3Admins')
