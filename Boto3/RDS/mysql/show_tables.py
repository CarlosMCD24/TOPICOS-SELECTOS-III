import pymysql


def show_tables():
    try:
        mydb = pymysql.connect(
            host="rdstest.c9rhzfcjvz27.us-east-2.rds.amazonaws.com",
            user="admin",
            password="password",
            database="dbmlruns"
        )

        mycursor = mydb.cursor()

        mycursor.execute("SHOW TABLES")

        for table in mycursor:
            print(table)


    except pymysql.MySQLError as e:
        print("Can not show the tables {} ".format(e))

if __name__ == '__main__':
    show_tables()
