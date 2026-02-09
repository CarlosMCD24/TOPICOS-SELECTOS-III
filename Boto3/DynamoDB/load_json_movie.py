import boto3
import json
from decimal import Decimal
from pprint import pprint

def load_json(json_data, table_name):
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table(table_name)

    for item in json_data:
        print(f"Adding item: {item}")
        table.put_item(Item=item)

    # # Construct DynamoDB item
    #     dynamodb_item = {
    #         'year': year,
    #         'title': title,
    #         'info': item.get('info', {})  # Keeping nested data under 'info'
    #     }


if __name__=="__main__":
    json_file_path = 'moviedata.json'
    table_name = 'Movies'

    # Load Json
    with open(json_file_path) as json_file:
        movie_data = json.load(json_file, parse_float=Decimal)

    # Insert data into DynamoDB table

    load_json(json_data=movie_data, table_name=table_name)