import boto3


def attach_policy(policy_arn, username):
    iam = boto3.client('iam')

    response = iam.attach_user_policy(
        UserName=username,
        PolicyArn=policy_arn
    )

    print(response)


if __name__ == '__main__':
    attach_policy('arn:aws:iam::108652872714:policy/pyFullAccess', 'testuser')