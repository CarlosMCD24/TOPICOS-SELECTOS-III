import boto3

def create_backup(table_name, backup_name):

    db = boto3.client('dynamodb')
    response = db.create_backup(
        TableName=table_name,
        BackupName=backup_name
    )

    print(response)


def delete_backup(backup_arn):
    db = boto3.client('dynamodb')
    response = db.delete_backup(
        BackupArn=backup_arn

    )

    print(response)

if __name__ == '__main__':
    table_name = 'employee'
    backup_name = 'employeebackup'
    backup_arn = 'arn:aws:dynamodb:us-east-2:108652872714:table/employee/backup/01740619331999-6ea59f79'
    #create_backup(table_name=table_name, backup_name=backup_name)
    delete_backup(backup_arn=backup_arn)
