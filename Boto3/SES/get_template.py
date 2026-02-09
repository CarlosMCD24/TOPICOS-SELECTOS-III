import boto3
from pprint import pprint

def get_template(template_name):

    ses_client = boto3.client('ses')

    response = ses_client.get_template(
        TemplateName=template_name
    )

    pprint(response['Template'])


def list_templates():

    ses_client = boto3.client('ses')

    response = ses_client.list_templates()
    print(response['TemplatesMetadata'])


if __name__ == '__main__':
    template_name = 'TemplateTest'
    #list_templates()
    get_template(template_name=template_name)