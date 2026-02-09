import boto3

def put_bash(table_name, items):

    db = boto3.resource('dynamodb')
    table = db.Table(table_name)

    with table.batch_writer() as batch:
        for item in items:
            batch.put_item(Item=item)
        print("Batch insert successful.")

if __name__ == '__main__':
    table_name = "employee"
    items = [
        {'emp_id': '2', 'name': 'Juan', 'age': '30'},
        {'emp_id': '3', 'name': 'Mario', 'age': '31'},
        {'emp_id': '5', 'name': 'anothername', 'age': '35'},
        {'emp_id': '6', 'name': 'abc', 'age': '32'},
        {'emp_id': '7', 'name': 'abc7', 'age': '37'}
    ]
    put_bash(table_name=table_name, items=items)

