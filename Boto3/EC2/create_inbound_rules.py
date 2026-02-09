import boto3


def create_inbound_rules(sg_id):
    ec2_client = boto3.client('ec2')

    response = ec2_client.authorize_security_group_ingress(
        GroupId=sg_id,
        IpPermissions=[
            {
                'IpProtocol':'tcp',
                'FromPort':80,
                'ToPort':80,
                'IpRanges':[{'CidrIp':'0.0.0.0/0', 'Description':'My description'}]
            },
    {
                'IpProtocol':'tcp',
                'FromPort':22,
                'ToPort':22,
                'IpRanges':[{'CidrIp':'0.0.0.0/0', 'Description':'My description'}]
            }
        ]
    )

    print(response)

if __name__ == '__main__':
    sg_id = 'sg-09b9ab986cbea7bcf'
    create_inbound_rules(sg_id=sg_id)