import pymysql


def show_data():
    try:
        dbname = input("Please enter the database name : ")
        tablename = input("Please enter the table name : ")

        mydb = pymysql.connect(
            host="rdstest.c9rhzfcjvz27.us-east-2.rds.amazonaws.com",
            user="admin",
            password="password",
            database=dbname
        )

        mycursor = mydb.cursor()

        mycursor.execute("SELECT * FROM {} ".format(tablename))

        result = mycursor.fetchall()

        for data in result:
            print(data)


    except pymysql.MySQLError as e:
        print("Can not show the data ".format(e))

if __name__ == '__main__':
    show_data()