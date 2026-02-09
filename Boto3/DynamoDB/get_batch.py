import boto3
from pprint import pprint

def get_batch(table_name, keys):
    '''
    Retrieves multiple items from a DynamoDB table using batch_get_item().

    :param table_name: Name of the DynamoDB table.
    :param keys: List of dictionaries representing the keys of the items to retrieve.
    :return: Retrieved items from DynamoDB.
    '''

    db = boto3.resource('dynamodb')

    response = db.batch_get_item(
        RequestItems={
            table_name:{
                'Keys':keys
            }
        }
    )

    pprint(response['Responses'])

if __name__ == '__main__':
    table_name='employee'
    keys = [{'emp_id': str(i)} for i in range(1, 5)]  
    get_batch(table_name=table_name, keys=keys)