import boto3

def send_html_email(
    source_email,
    to_addresses,
    subject,
    html_body,
    charset="UTF-8"
):
    ses_client = boto3.client('ses')

    response = ses_client.send_email(
        Destination={
            "ToAddresses": to_addresses
        },
        Message={
            "Body": {
                "Html": {
                    "Charset": charset,
                    "Data": html_body
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
    html_content = """
        <html>
            <head></head>
            <body>
                <h1 style='text-align:center;'>Curso de AWS con Python y Boto3</h1>
                <p style='color:red;'>Bienvenidos al curso</p>
            </body>
        </html>
    """

    send_html_email(
        source_email="toledano.ivan16@gmail.com",
        to_addresses=["toledano.ivan16@gmail.com"],
        subject="Curso de AWS con Python y Boto3",
        html_body=html_content
    )
