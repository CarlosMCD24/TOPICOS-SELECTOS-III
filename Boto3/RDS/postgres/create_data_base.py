import psycopg2


def create_db():
    try:
        conn = psycopg2.connect(
            user="admins",
            password="password",
            host="rdstest.c9rhzfcjvz27.us-east-2.rds.amazonaws.com",
            port=5432,
            dbname="rdstest"
        )

        conn.autocommit=True

        mycursor = conn.cursor()

        query = "CREATE DATABASE mydb"

        mycursor.execute(query)
        print("Database created")

    except:
        print("Failed to create database")

if __name__ == '__main__':
    create_db()