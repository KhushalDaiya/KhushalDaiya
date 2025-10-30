import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password="khus",
    database="python_batch"
)
def show_row():
    cursor = connection.cursor()
    query = "select name, email, mobile from user order by id asc"
    cursor.execute(query)
    while True:
        user_choice = input("ENTER no. OF ROWS YOU WANT TO SEE:) ")
        show_rows = int(user_choice)

        if show_rows == 0:
            break
        record = cursor.fetchmany(show_rows)
        if not record:
            break
        for i in record:
            name, email, mobile = i
            print(f"Name: {name}")
            print(f"Email: {email}")
            print(f"Mobile: {mobile}")

    print("All records displayed")

show_row()
