import mysql.connector

connection = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root', 
    password="khus", 
    database = 'python_batch'
)
cursor = connection.cursor(dictionary=True)
user_choice = {
    1: 'INSERT',
    2: 'UPDATE',
    3: 'DELETE',
    4: 'SELECT'
}

ask_user_choice = f"""
Please select your choice
Press 1 for Insert
Press 2 for Update
Press 3 for Delete
Press 4 for Select
"""

while True:
    user_select_choice = input(ask_user_choice)
    realvalid_choice = user_choice.get(int(user_select_choice))
    if realvalid_choice:
        if realvalid_choice == 'INSERT':
            while True:
                name = input('Enter name to insert: ')
                if len(name) >= 5 and len(name) <= 20:
                    break
                else:
                    print("Please enter a valid name with Min 5 and Max 10 and all char should be Alpha")

            email = input('Enter email to insert: ')
            mobile = input('Enter mobile to insert: ')

            query = "insert into user (name,email,mobile) values (%s,%s,%s)"
            cursor.execute(query,(name,email,mobile))
            connection.commit()
            print("Record inserted successfully")
        else:
            print('🥲')
    else:
        print('Please enter a valid no')
