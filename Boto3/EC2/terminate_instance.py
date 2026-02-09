import boto3


def terminate_instance(instance_id):
    ec2_client = boto3.client('ec2')
    response = ec2_client.terminate_instances(InstanceIds=[instance_id])
    print(response)



if __name__ == '__main__':
    instance_id = 'i-02adc26d9ec09dc64'
    terminate_instance(instance_id=instance_id)