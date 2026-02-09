import boto3

def list_policies():
    iam = boto3.client('iam')

    paginator = iam.get_paginator('list_policies')

    for response in paginator.paginate(Scope='Local'): # or 'Local' for custom policies or Scope = 'AWS'
        for policy in response['Policies']:
            policy_name = policy['PolicyName']
            Arn = policy['Arn']

            print(f'Policy Name : {policy_name}, Arn : {Arn}')

if __name__ == '__main__':
    list_policies()