import boto3

def create_group(group_name):
    iam = boto3.client('iam')
    iam.create_group(GroupName=group_name)

if __name__ == '__main__':
    create_group('S3Admins')