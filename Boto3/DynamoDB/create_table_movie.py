import boto3

def create_table(table_name, key_schema, attribute_definitions, provisioned_throughput):
    dynamodb = boto3.resource('dynamodb')
    
    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=key_schema,
        AttributeDefinitions=attribute_definitions,
        ProvisionedThroughput=provisioned_throughput

    )

    return table


if __name__ == "__main__":
    table_name = 'Movies'
    key_schema=[
            {
                'AttributeName':'year',
                'KeyType':'HASH'
            },

            {
                'AttributeName': 'title',
                'KeyType': 'RANGE'
            }
        ]
    attribute_definitions=[
            {
                'AttributeName': 'year',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'title',
                'AttributeType': 'S'
            }
        ]
    provisioned_throughput = {
            'ReadCapacityUnits':5,
            'WriteCapacityUnits':5
        }
    movie_table = create_table(table_name=table_name,
                               key_schema=key_schema,
                               attribute_definitions=attribute_definitions,
                               provisioned_throughput=provisioned_throughput)
    print("Table status : ", movie_table.table_status)
