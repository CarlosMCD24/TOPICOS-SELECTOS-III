import boto3


def put_item(table_name, item):
    db = boto3.client('dynamodb')

    try:
        response = db.put_item(TableName=table_name, Item=item)
        return response
    except Exception as e:
        print(f"Error inserting item into {table_name}: {e}")

if __name__ == '__main__':
    item = {
        'emp_id': {
            'S':'4'
        },
        'name':{
            'S':'John'
        },

        'age': {
            'S':'25'
        }
    }
    table_name = 'employee'
    put_item(table_name=table_name, item=item)
