import boto3
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email_attachment(
    source_email,
    to_addresses,
    subject,
    body_text,
    attachment_path
):
    # Create a multipart message
    msg = MIMEMultipart()
    msg["Subject"] = subject
    msg["From"] = source_email
    msg["To"] = ", ".join(to_addresses)

    # Add the body text
    body = MIMEText(body_text)
    msg.attach(body)

    # Attach the file
    with open(attachment_path, "rb") as f:
        part = MIMEApplication(f.read())
        part.add_header("Content-Disposition", "attachment", filename=attachment_path.split("/")[-1])
        msg.attach(part)

    # Send via SES
    ses_client = boto3.client("ses")
    response = ses_client.send_raw_email(
        Source=source_email,
        Destinations=to_addresses,
        RawMessage={"Data": msg.as_string()}
    )

    print(response)


if __name__ == '__main__':
    send_email_attachment(
        source_email="toledano.ivan16@gmail.com",
        to_addresses=["toledano.ivan16@gmail.com"],
        subject="Taller de análisis de datos con Python y Pandas",
        body_text="Gracias por tu participación en el taller. Se anexa el temario del curso.",
        attachment_path="README.md"
    )
