import boto3

def delete_sg(sg_id):
    ec2_client = boto3.client('ec2')

    response = ec2_client.delete_security_group(
        GroupId = sg_id
    )

    print(response)

if __name__ == '__main__':
    sg_id = 'sg-09b9ab986cbea7bcf'
    delete_sg(sg_id=sg_id)
