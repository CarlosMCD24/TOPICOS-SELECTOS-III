import boto3

def send_email_text(
    source_email,
    to_addresses,
    subject,
    body_text,
    charset='UTF-8'
):
    ses_client = boto3.client('ses')

    response = ses_client.send_email(
        Destination={
            "ToAddresses": to_addresses
        },
        Message={
            "Body": {
                "Text": {
                    "Charset": charset,
                    "Data": body_text
                }
            },
            "Subject": {
                "Charset": charset,
                "Data": subject
            }
        },
        Source=source_email
    )

    print(response)


if __name__ == '__main__':
    send_email_text(
        source_email="toledano.ivan16@gmail.com",
        to_addresses=["toledano.ivan16@gmail.com"],
        subject="Topicos III: AWS SES y Boto3",
        body_text="Esta es la tarea de esta semana."
    )