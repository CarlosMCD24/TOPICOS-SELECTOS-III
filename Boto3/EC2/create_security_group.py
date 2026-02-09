import boto3

# Create a security group if it doesn't exist
def create_security_group(sg_name, region):
    ec2_client = boto3.client('ec2', region_name=region)
    try:
        response = ec2_client.create_security_group(
            GroupName=sg_name,
            Description='Security group for Free Tier EC2',
        )
        sg_id = response['GroupId']
        ec2_client.authorize_security_group_ingress(
            GroupId=sg_id,
            IpPermissions=[
                {
                    'IpProtocol': 'tcp',
                    'FromPort': 22,
                    'ToPort': 22,
                    'IpRanges': [{'CidrIp': '0.0.0.0/0'}],
                },
                {
                    'IpProtocol': 'tcp',
                    'FromPort': 5000,
                    'ToPort': 5000,
                    'IpRanges': [{'CidrIp': '0.0.0.0/0'}],
                }
            ]
        )
        ##Using 0.0.0.0/0 opens the port to the entire internet. For production or sensitive applications:

        ##Restrict SSH to your IP (e.g., 203.0.113.0/32)

        ##Use HTTPS and reverse proxies for web apps
        
        print(f'Security group {SECURITY_GROUP_NAME} created with ID: {sg_id}')
        return sg_id
    except ec2_client.exceptions.ClientError as e:
        if 'InvalidGroup.Duplicate' in str(e):
            print(f'Security group {SECURITY_GROUP_NAME} already exists.')
            groups = ec2_client.describe_security_groups(GroupNames=[SECURITY_GROUP_NAME])
            return groups['SecurityGroups'][0]['GroupId']
        else:
            raise

if __name__ == '__main__':
    SECURITY_GROUP_NAME = 'security-group-mlflow'
    REGION = 'us-east-2'
    create_security_group(sg_name=SECURITY_GROUP_NAME, region=REGION)