import boto3

def stop_instance(instance_id):
    ec2_client = boto3.client('ec2')
    response = ec2_client.stop_instances(InstanceIds=[instance_id])

    print(response)


if __name__ == '__main__':
    instance_id = 'i-02adc26d9ec09dc64'
    stop_instance(instance_id=instance_id)