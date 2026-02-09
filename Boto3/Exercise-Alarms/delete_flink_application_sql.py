import boto3
import time

region = 'us-east-2'
app_name = 'flink-alarm-app'

client = boto3.client('kinesisanalyticsv2', region_name=region)

def delete_flink_app():
    try:
        # Get app status and creation timestamp
        response = client.describe_application(ApplicationName=app_name)
        status = response['ApplicationDetail']['ApplicationStatus']
        timestamp = response['ApplicationDetail']['CreateTimestamp']

        # Stop if running
        if status in ['RUNNING', 'STARTING']:
            print(f"Stopping application '{app_name}'...")
            client.stop_application(ApplicationName=app_name)
            while True:
                time.sleep(5)
                check = client.describe_application(ApplicationName=app_name)
                new_status = check['ApplicationDetail']['ApplicationStatus']
                print(f"Status: {new_status}")
                if new_status == 'STOPPED':
                    break

        # Delete the application
        print(f"Deleting application '{app_name}'...")
        client.delete_application(
            ApplicationName=app_name,
            CreateTimestamp=timestamp
        )
        print("Application deleted successfully.")

    except client.exceptions.ResourceNotFoundException:
        print(f"Application '{app_name}' not found.")
    except Exception as e:
        print(f"Error deleting application: {e}")

if __name__ == '__main__':
    delete_flink_app()

