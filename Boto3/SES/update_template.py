import boto3

def update_template(template_name, subject_part, text_part, html_part):
    ses_client = boto3.client('ses')

    response = ses_client.update_template(
        Template={
            'TemplateName':template_name,
            'SubjectPart':subject_part,
            'TextPart':text_part,
            'HtmlPart':html_part
        }
    )

    print(response)

if __name__ == '__main__':
    template_name = 'TemplateTest'
    subject_part = 'Bienvenido al taller de análisis de datos con Pandas y AWS'
    text_part = 'Gracias por haberte inscrito al taller de análisis de datos con Pandas y Sklearn'
    html_part = 'Gracias por haberte inscrito al taller de análisis de datos con Pandas y Sklearn'

    update_template(template_name=template_name,
                    subject_part=subject_part,
                    text_part=text_part,
                    html_part=html_part)