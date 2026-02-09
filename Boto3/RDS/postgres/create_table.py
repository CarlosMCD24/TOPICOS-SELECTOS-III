import psycopg2

def create_table():
    try:
        conn = psycopg2.connect(
            database="mydb", user="admins", password="password",
            host="rdstest.c9rhzfcjvz27.us-east-2.rds.amazonaws.com",
            port=5432,
            dbname='rdstest'
        )

        cur = conn.cursor()
        query = "CREATE TABLE Employee (ID INT PRIMARY KEY NOT NULL, NAME TEXT NOT NULL, EMAIL TEXT NOT NULL)"
        cur.execute(query)
        conn.commit()
        print("Table created")



    except:
        print("Can not create table")

if __name__ == '__main__':
    create_table()