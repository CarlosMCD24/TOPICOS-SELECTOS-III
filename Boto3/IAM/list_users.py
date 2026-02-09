import boto3

def all_users():
    iam = boto3.client('iam')

    #paginator object
    #abstraction over the process of iterating over an entire result set of a truncated API operation.
    paginator = iam.get_paginator('list_users')

    for response in paginator.paginate():
        for user in response['Users']:
            username = user['UserName']
            Arn = user['Arn']
            print(f'Username : {username}, Arn : {Arn}')

if __name__ == '__main__':
    all_users()