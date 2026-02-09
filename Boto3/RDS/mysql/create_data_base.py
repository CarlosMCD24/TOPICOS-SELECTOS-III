import pymysql

def create_db():
    # database -> dbmlruns
    # please modify mysql database inbound rules
    try:
        mydb = pymysql.connect(
            host="rdstest.c9rhzfcjvz27.us-east-2.rds.amazonaws.com",
            user="admin",
            password="password"
        )

        dbname = input("Please enter your database name :")

        cursor = mydb.cursor()

        cursor.execute("CREATE DATABASE {} ".format(dbname))
        print("Database created ")


    except pymysql.MySQLError as e:
        print("Failed to create database {} ".format(e))

if __name__ == '__main__':
    create_db()