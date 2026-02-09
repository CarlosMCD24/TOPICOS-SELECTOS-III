import boto3


def get_ip(instance_id):
    ec2_client = boto3.client('ec2')

    reservations = ec2_client.describe_instances(InstanceIds=[instance_id]).get('Reservations')

    for reservation in reservations:
        for instance in reservation['Instances']:
            print(instance.get('PublicIpAddress'))


if __name__ == '__main__':
    instance_id = 'i-01382a00dce563c4f'
    get_ip(instance_id=instance_id)