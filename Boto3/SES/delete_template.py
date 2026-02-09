import boto3

def delete_template(template_name):
    ses_client = boto3.client('ses')

    response = ses_client.delete_template(
    TemplateName=template_name
)

    print(response)

if __name__ == '__main__':
    template_name = 'TemplateTest'
    delete_template(template_name=template_name)