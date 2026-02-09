import psycopg2

def update_data():
    try:
        conn = psycopg2.connect(
            database="rdstest", user="admins", password="password",
            host="rdstest.c9rhzfcjvz27.us-east-2.rds.amazonaws.com",
            port=5432
        )

        cur = conn.cursor()

        query = "UPDATE Employee SET EMAIL = 'updated@gmail.com' WHERE id=1"
        cur.execute(query)

        conn.commit()
        print("Data updated")
        print("Total Row Affected " + str(cur.rowcount))



    except:
        print("Unable to update the data")

if __name__ == '__main__':
    update_data()