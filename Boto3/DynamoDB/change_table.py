import boto3

def change_table(table_name):

    db = boto3.client('dynamodb')

    response = db.update_table(
        TableName=table_name,
        BillingMode='PROVISIONED',

        ProvisionedThroughput={
            'ReadCapacityUnits':1,
            'WriteCapacityUnits':1
        }
    )

    print(response)

if __name__ == '__main__':
    table_name = 'employee'
    change_table(table_name=table_name)
