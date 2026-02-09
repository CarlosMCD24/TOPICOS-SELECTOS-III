import boto3

def verify_email(email):

    ses_client = boto3.client('ses')

    response = ses_client.verify_email_address(
        EmailAddress=email
    )

    print(response)

if __name__ == '__main__':
    email = 'toledano.ivan16@gmail.com'
    verify_email(email=email)
