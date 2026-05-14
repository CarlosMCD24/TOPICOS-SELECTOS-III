from __future__ import print_function
import boto3

sns_client = boto3.client('sns')
TOPIC_ARN = 'arn:aws:sns:us-east-2:406260045278:OrderAlarmTopic'
ORDER_THRESHOLD = 10

def lambda_handler(event, context):
    """
    Triggered by Kinesis stream with a 10-second tumbling window.
    If orders in the window >= ORDER_THRESHOLD, fires an SNS alarm.
    """
    order_count = len(event['Records'])
    print(f'Orders in this window: {order_count}')

    if order_count >= ORDER_THRESHOLD:
        try:
            sns_client.publish(
                TopicArn=TOPIC_ARN,
                Message=f'Investigate sudden surge in orders. Count: {order_count}',
                Subject='Cadabra Order Rate Alarm'
            )
            print('Successfully delivered alarm message')
        except Exception as e:
            print(f'Delivery failure: {e}')
