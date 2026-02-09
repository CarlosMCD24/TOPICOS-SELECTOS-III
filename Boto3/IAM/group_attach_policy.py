import boto3

def attach_policy(policy_arn, group_name):
    iam = boto3.client('iam')

    response = iam.attach_group_policy(
        GroupName=group_name,
        PolicyArn=policy_arn
    )

    print(response)

if __name__ == '__main__':
    attach_policy('arn:aws:iam::108652872714:policy/pyFullAccess','S3Admins')