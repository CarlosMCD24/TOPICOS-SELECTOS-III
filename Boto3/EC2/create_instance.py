import boto3

# Configuration
REGION = 'us-east-2'
AMI_ID = 'ami-0f30a9c3a48f3fa79'
INSTANCE_TYPE = 't2.micro'
KEY_NAME = 'tsii_key'
SECURITY_GROUP_NAME = 'security-group-mlflow'

# Initialize EC2 resource
ec2 = boto3.resource('ec2', region_name=REGION)

# Create a security group if it doesn't exist
def create_security_group():
    ec2_client = boto3.client('ec2', region_name=REGION)
    try:
        response = ec2_client.create_security_group(
            GroupName=SECURITY_GROUP_NAME,
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

# Launch EC2 instance
def launch_instance():
    sg_id = create_security_group()

    instance = ec2.create_instances(
        ImageId=AMI_ID,
        InstanceType=INSTANCE_TYPE,
        KeyName=KEY_NAME,
        SecurityGroupIds=[sg_id],
        MinCount=1,
        MaxCount=1,
        TagSpecifications=[{
            'ResourceType': 'instance',
            'Tags': [{'Key': 'Name', 'Value': 'FreeTierInstance'}]
        }]
    )[0]

    print("Launching instance, please wait...")
    instance.wait_until_running()
    instance.reload()
    print(f'Instance launched with ID: {instance.id}')
    print(f'Public DNS: {instance.public_dns_name}')
    print(f'Public IP: {instance.public_ip_address}')

if __name__ == "__main__":
    launch_instance()
