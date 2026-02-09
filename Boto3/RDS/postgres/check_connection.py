import psycopg2

def check_connection():
    try:
        conn = psycopg2.connect(
            database="mydb",
            user="admins",
            password="password",
            host="rdstest.c9rhzfcjvz27.us-east-2.rds.amazonaws.com",
            port=5432
        )

        print("Database connected")

    except:
        print("Faild to connect the database")

if __name__ == '__main__':
    check_connection()