import pymysql


def update_data():
    try:
        mydb = pymysql.connect(
            host="rdstest.c9rhzfcjvz27.us-east-2.rds.amazonaws.com",
            user="admin",
            password="password",
            database="dbmlruns"
        )

        mycursor = mydb.cursor()

        query = "UPDATE Person SET name='updated' WHERE id='1'"

        mycursor.execute(query)
        mydb.commit()
        print(mycursor.rowcount, "record affected")

    except pymysql.MySQLError as e:
        print("Can not update data {} ".format(e))

if __name__ == '__main__':
    update_data()