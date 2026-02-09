import boto3

def get_item(table_name, key):

    db = boto3.resource('dynamodb')
    table = db.Table(table_name)


    response = table.get_item(
        Key = key)

    print(response['Item'])

if __name__ == '__main__':
    table_name = 'employee'
    key = {
            'emp_id':"5"
        }
    get_item(table_name=table_name, key=key)
