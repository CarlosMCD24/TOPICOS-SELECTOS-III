import boto3

def create_streams(stream_names, region, shard_count):
    client = boto3.client('kinesis', region_name=region)

    for stream_name in stream_names:
        try:
            response = client.create_stream(
                StreamName=stream_name,
                ShardCount=shard_count
            )
            print(f"Creating stream: {stream_name}")
        except client.exceptions.ResourceInUseException:
            print(f"Stream {stream_name} already exists.")
        except Exception as e:
            print(f"Error creating stream {stream_name}: {e}")

if __name__ == "__main__":

    STREAM_NAMES = ['CadabraOrders', 'alarm-stream', 'trigger-count-stream']
    REGION = 'us-east-2' 
    SHARD_COUNT = 1

    create_streams(stream_names=STREAM_NAMES,
                   region=REGION,
                   shard_count=SHARD_COUNT)
