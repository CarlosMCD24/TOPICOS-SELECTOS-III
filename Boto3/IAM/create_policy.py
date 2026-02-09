import boto3
import json

def create_policy():
    iam = boto3.client('iam')

    user_policy = {
        "Version":"2012-10-17",
        "Statement":[
            {
                "Effect": "Allow",
                "Action": "*",
                "Resource": "*"
            }
        ]
    }

    response = iam.create_policy(
        PolicyName = 'pyFullAccess',
        PolicyDocument=json.dumps(user_policy) # converts python objecto to json string
    )

    print(response)

if __name__ == '__main__':
    create_policy()