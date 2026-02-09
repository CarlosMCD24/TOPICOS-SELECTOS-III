import pymysql


def create_table():
    try:
        mydb = pymysql.connect(
            host="rdstest.c9rhzfcjvz27.us-east-2.rds.amazonaws.com",
            user="admin",
            password="password",
            database="dbmlruns"
        )


        mycursor = mydb.cursor()

        mycursor.execute("CREATE TABLE Person (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), lastname VARCHAR(255))")
        print("Table is created")



    except pymysql.MySQLError as e:
        print("Failed to create table {} ".format(e))

if __name__ == '__main__':
    create_table()