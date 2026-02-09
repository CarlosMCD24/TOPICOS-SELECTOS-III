import boto3
from pprint import pprint

def get_data(table_name):
    db = boto3.client('dynamodb')


    response = db.describe_table(
        TableName = table_name

    )

    pprint(response)

if __name__ == '__main__':
    table_name = 'employee'
    get_data(table_name=table_name)
