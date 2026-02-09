import boto3
from boto3.dynamodb.conditions import Key, Attr
from pprint import pprint

# Scan permite recuperar todos los items de la tabla o índice
# también permite aplicar condiciones para filtrar la informacion

def scan_data(table_name, filter_conditions=None):

    db = boto3.resource('dynamodb')
    table = db.Table(table_name)

    scan_kwargs = {}

    if filter_conditions:
        filter_expr = None
        for attr, value in filter_conditions.items():
            condition = Attr(attr).eq(value)
            filter_expr = condition if filter_expr is None else filter_expr & condition
        scan_kwargs['FilterExpression'] = filter_expr

    try:
        response = table.scan(**scan_kwargs)
        data = response['Items']
        pprint(data)
        return data
    except Exception as e:
        print(f"Error scanning table {table_name}: {e}")
        return None

if __name__ == '__main__':
    table_name = 'employee'
    filter_conditions = {
        "age": "35",
        "name": "anothername"
    }
    scan_data(table_name=table_name, filter_conditions=filter_conditions)