import psycopg2

def delete_data():
    try:
        conn = psycopg2.connect(
            database="rdstest", user="admins", password="password",
            host="rdstest.c9rhzfcjvz27.us-east-2.rds.amazonaws.com",
            port=5432
        )

        cur = conn.cursor()

        query = "DELETE FROM Employee WHERE id=1"

        cur.execute(query)
        conn.commit()
        print("Data deleted")
        print("Total number of row deleted " + str(cur.rowcount))

    except:
        print("Unable to delete the data")

if __name__ == '__main__':
    delete_data()