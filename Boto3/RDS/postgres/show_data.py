import psycopg2

def show_data():
    try:
        conn = psycopg2.connect(
            database="rdstest", user="admins", password="password",
            host="rdstest.c9rhzfcjvz27.us-east-2.rds.amazonaws.com",
            port=5432
        )

        cur = conn.cursor()

        query = "SELECT * FROM Employee"

        cur.execute(query)

        rows = cur.fetchall()

        for data in rows:
            print("ID : " + str(data[0]))
            print("Name : " + data[1])
            print("Email : " + data[2])

    except:
        print("Can not read the data")

if __name__ == '__main__':
    show_data()