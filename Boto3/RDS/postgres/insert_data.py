import psycopg2

def insert_data():
    try:
        conn = psycopg2.connect(
            database="rdstest", user="admins", password="password",
            host="rdstest.c9rhzfcjvz27.us-east-2.rds.amazonaws.com",
            port=5432
        )

        cur = conn.cursor()

        query = "INSERT INTO Employee (ID, NAME, EMAIL) VALUES (1, 'parwiz', 'par@gmail.com')"
        cur.execute(query)
        conn.commit()
        print("Data has been added")

    except:
        print("Can not add data")

if __name__ == '__main__':
    insert_data()

