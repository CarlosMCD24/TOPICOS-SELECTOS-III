# launch_flink_studio_app_with_input.py
import boto3

region = 'us-east-2'
app_name = 'flink-alarm-app'
iam_role_arn = 'arn:aws:iam::108652872714:role/FlinkKinesisRole'
source_stream_name = 'CadabraOrders'

client = boto3.client('kinesisanalyticsv2', region_name=region)

def create_flink_studio_app():
    try:
        response = client.create_application(
            ApplicationName=app_name,
            RuntimeEnvironment='SQL-1_0',
            ServiceExecutionRole=iam_role_arn,
            ApplicationConfiguration={
                "SqlApplicationConfiguration": {
                    "Inputs": [
                        {
                            "NamePrefix": "SOURCE_SQL_STREAM",
                            "KinesisStreamsInput": {
                                "ResourceARN": f"arn:aws:kinesis:{region}:108652872714:stream/{source_stream_name}"
                            },
                            "InputSchema": {
                                "RecordFormat": {
                                    "RecordFormatType": "JSON",
                                    "MappingParameters": {
                                        "JSONMappingParameters": {
                                            "RecordRowPath": "$"
                                        }
                                    }
                                },
                                "RecordEncoding": "UTF-8",
                                "RecordColumns": [
                                    {
                                        "Name": "order_id",
                                        "Mapping": "$.order_id",
                                        "SqlType": "VARCHAR(64)"
                                    },
                                    {
                                        "Name": "event_time",
                                        "Mapping": "$.event_time",
                                        "SqlType": "TIMESTAMP"
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
        )
        print(f"Created Flink Studio application: {app_name}")
    except client.exceptions.ResourceInUseException:
        print(f"Application '{app_name}' already exists.")
    except Exception as e:
        print(f"Error creating application: {e}")

if __name__ == '__main__':
    create_flink_studio_app()

