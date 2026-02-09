import boto3

def send_templated_email(
    source_email,
    to_addresses,
    cc_addresses=None,
    reply_to_addresses=None,
    template_name='DefaultTemplate',
    template_data='{}'
):
    ses_client = boto3.client('ses')

    response = ses_client.send_templated_email(
        Source=source_email,
        Destination={
            'ToAddresses': to_addresses,
            'CcAddresses': cc_addresses or []
        },
        ReplyToAddresses=reply_to_addresses or [],
        Template=template_name,
        TemplateData=template_data
    )

    print(response)

if __name__ == '__main__':
    source = 'toledano.ivan16@gmail.com'
    to = ['eduardo.fletes1892@alumnos.udg.mx']
    cc = ['ivan.toledano@academicos.udg.mx']
    reply_to = ['toledano.ivan16@gmail.com']
    template = 'TemplateTest'
    data = '{"replace":"value"}'

    send_templated_email(
        source_email=source,
        to_addresses=to,
        cc_addresses=cc,
        reply_to_addresses=reply_to,
        template_name=template,
        template_data=data
    )