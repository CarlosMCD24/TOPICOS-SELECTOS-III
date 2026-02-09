import pymysql


def delete_data():
    try:
        mydb = pymysql.connect(
            host="rdstest.c9rhzfcjvz27.us-east-2.rds.amazonaws.com",
            user="admin",
            password="password",
            database="dbmlruns"
        )

        mycursor = mydb.cursor()

        query = "DELETE FROM Person WHERE id='4'"

        mycursor.execute(query)

        mydb.commit()

        print(mycursor.rowcount, "record affected")


    except pymysql.MySQLError as e:
        print("Can not delete the item {} ".format(e))

if __name__ == '__main__':
    delete_data()