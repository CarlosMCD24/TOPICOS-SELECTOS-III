import pymysql

def check_connection():
    try:
        mydb = pymysql.connect(
            host="rdstest.c9rhzfcjvz27.us-east-2.rds.amazonaws.com",
            user="admin",
            password="password",
            database="dbmlruns"
        )

        print("Connection created")



    except pymysql.MySQLError as e:
        print("There is no connection {} ".format(e))

if __name__ == '__main__':
    check_connection()