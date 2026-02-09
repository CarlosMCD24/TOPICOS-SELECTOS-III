import boto3

def list_tables():
    db = boto3.client('dynamodb')
    response = db.list_tables()

    print(response['TableNames'])

if __name__ == '__main__':
    list_tables()
