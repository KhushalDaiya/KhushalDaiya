import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    user='root', 
    password="khus", 
    database='python_batch'
)
cursor = connection.cursor(dictionary=True)
user_choice = {
    1: 'INSERT',
    2: 'UPDATE',
    3: 'DELETE',
    4: 'SELECT'
}
ask_user_choice = f"""
Please select your choice:
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

            while True:
                email = input('Enter email to insert: ')
                if 13 <= len(email) <= 20 and email.endswith('@gmail.com'):
                    break
                else:
                    print("Please enter a valid email address (length upto 13-20 characters).")
            
            while True:
                mobile = input('Enter mobile to insert: ')
                if mobile.isdigit() and len(mobile) == 10:
                    break
                else:
                    print("Please enter a valid 10-digit mobile number (only digits).")

            query = "INSERT INTO user (name, email, mobile) VALUES (%s, %s, %s)"
            cursor.execute(query, (name, email, mobile))
            connection.commit()
            print("Record inserted successfully")
        
        elif realvalid_choice == 'DELETE':
            while True:
                userid = input('Enter the user ID to delete: ')
                if userid.isdigit():
                    break
                else:
                    print("Please enter a valid integer ID.")

            cursor.execute("SELECT * FROM user WHERE id = %s", (userid,))
            record = cursor.fetchone()

            if record:
                cursor.execute("DELETE FROM user WHERE id = %s", (userid,))
                connection.commit()
                print(f"Record with ID {userid} deleted successfully.")
            else:
                print(f"No record found with ID {userid}.")
        else:
            print('WIP')
    else:
        print('Please enter a valid number')
