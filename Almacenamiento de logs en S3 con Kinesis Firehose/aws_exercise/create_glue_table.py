import boto3

REGION = 'us-east-2'
BUCKET_NAME = 'ecom-purchaselogs-bucket'
GLUE_DB_NAME = 'ecom_logs_db'
TABLE_NAME = 'purchase_logs'

# Schema matches the CSV columns from LogGenerator / Kinesis Agent config:
# InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, Customer, Country
COLUMNS = [
    {'Name': 'invoiceno',    'Type': 'string'},
    {'Name': 'stockcode',    'Type': 'string'},
    {'Name': 'description',  'Type': 'string'},
    {'Name': 'quantity',     'Type': 'int'},
    {'Name': 'invoicedate',  'Type': 'string'},
    {'Name': 'unitprice',    'Type': 'double'},
    {'Name': 'customer',     'Type': 'string'},
    {'Name': 'country',      'Type': 'string'},
]

def create_database(glue):
    try:
        glue.create_database(DatabaseInput={'Name': GLUE_DB_NAME})
        print(f'Database "{GLUE_DB_NAME}" created')
    except glue.exceptions.AlreadyExistsException:
        print(f'Database "{GLUE_DB_NAME}" already exists')

def create_table(glue):
    table_input = {
        'Name': TABLE_NAME,
        'StorageDescriptor': {
            'Columns': COLUMNS,
            'Location': f's3://{BUCKET_NAME}/logs/',
            'InputFormat': 'org.apache.hadoop.mapred.TextInputFormat',
            'OutputFormat': 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat',
            'SerdeInfo': {
                'SerializationLibrary': 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe',
                'Parameters': {
                    'field.delim': ',',
                    'serialization.format': ','
                }
            },
            'Compressed': False,
        },
        'TableType': 'EXTERNAL_TABLE',
        'Parameters': {'classification': 'csv'},
    }

    try:
        glue.create_table(DatabaseName=GLUE_DB_NAME, TableInput=table_input)
        print(f'Table "{TABLE_NAME}" created with explicit schema')
    except glue.exceptions.AlreadyExistsException:
        glue.update_table(DatabaseName=GLUE_DB_NAME, TableInput=table_input)
        print(f'Table "{TABLE_NAME}" updated with explicit schema')

if __name__ == '__main__':
    glue = boto3.client('glue', region_name=REGION)
    create_database(glue)
    create_table(glue)
    print(f'\n✓ Table "{GLUE_DB_NAME}.{TABLE_NAME}" points to s3://{BUCKET_NAME}/logs/')
    print('Ready to query with Athena.')
