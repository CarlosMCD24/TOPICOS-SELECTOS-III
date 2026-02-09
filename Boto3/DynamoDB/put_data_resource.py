import boto3

def put_item(table_name, item):
    """
    Inserts an item into a DynamoDB table.

    :param table_name: Name of the DynamoDB table.
    :param item: Dictionary representing the item to be inserted.
    :return: Response from DynamoDB.
    """
    db = boto3.resource('dynamodb')
    table = db.Table(table_name)

    try:
        response = table.put_item(Item=item)
        return response
    except Exception as e:
        print(f"Error inserting item into {table_name}: {e}")

if __name__ == '__main__':
    item = {
        'emp_id':"1",
            'name':"Pascal",
            'age':27
    }
    table_name = 'employee'
    put_item(table_name=table_name, item=item)
