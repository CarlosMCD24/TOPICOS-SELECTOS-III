import boto3

def delete_streams(stream_names, region):
    client = boto3.client('kinesis', region_name=region)

    for stream_name in stream_names:
        try:
            response = client.delete_stream(
                StreamName=stream_name,
                EnforceConsumerDeletion=True
            )
            print(f"Deleting stream: {stream_name}")
        except client.exceptions.ResourceNotFoundException:
            print(f"Stream {stream_name} not found.")
        except Exception as e:
            print(f"Error deleting stream {stream_name}: {e}")

if __name__ == "__main__":

    STREAM_NAMES = ['CadabraOrders', 'alarm-stream', 'trigger-count-stream']
    REGION = 'us-east-2'

    delete_streams(stream_names=STREAM_NAMES,
                   region=REGION)
