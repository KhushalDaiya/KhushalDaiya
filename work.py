import mysql.connector
from dotenv import load_dotenv
import os
load_dotenv()

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
RESET = '\033[0m'

connection = mysql.connector.connect(
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USER'), 
    password=os.getenv('DB_PASSWORD'), 
    database=os.getenv('DB_DATABASE')
)
DB_TABLE = os.getenv('DB_TABLE')
cursor = connection.cursor(dictionary=True)

user_choice = {
    1: 'INSERT',
    2: 'UPDATE',
    3: 'DELETE',
    4: 'SELECT',
    5: 'EXIT'
}

ask_user_choice = f"""
{BLUE}Please select your choice:
Press 1 for Insert
Press 2 for Update
Press 3 for Delete
Press 4 for Select
Press 5 for Exit
:){RESET}"""


while True:
    user_select_choice = input(ask_user_choice)
    if not user_select_choice.isdigit():
        print(RED + 'Please enter a valid number' + RESET)
        continue

    realvalid_choice = user_choice.get(int(user_select_choice))

    if realvalid_choice:
        if realvalid_choice == 'INSERT':
            while True:
                name = input(BLUE + 'Enter name to insert: ' + RESET)
                if name.isalpha() and 5 <= len(name) <= 20:
                    break
                else:
                    print(RED + "Please enter a valid name (5-20 alphabetic characters)." + RESET)

            while True:
                email = input(BLUE + 'Enter email to insert: ' + RESET)
                if 13 <= len(email) <= 30 and email.endswith('@gmail.com'):
                    break
                else:
                    print(RED + "Please enter a valid email address (13-30 chars, must end with @gmail.com)." + RESET)

            while True:
                mobile = input(BLUE + 'Enter mobile to insert: ' + RESET)
                if mobile.isdigit() and len(mobile) == 10:
                    break
                else:
                    print(RED + "Please enter a valid 10-digit mobile number (only digits)." + RESET)

            query = f"INSERT INTO {DB_TABLE} (name, email, mobile) VALUES (%s, %s, %s)"
            cursor.execute(query, (name, email, mobile))
            connection.commit()
            print(GREEN + "Record inserted successfully" + RESET)

        elif realvalid_choice == 'DELETE':
            while True:
                userid = input(BLUE + 'Enter the user ID to delete: ' + RESET)
                if userid.isdigit():
                    break
                else:
                    print(RED + "Please enter a valid integer ID." + RESET)

            cursor.execute(f"SELECT * FROM {DB_TABLE} WHERE id = %s", (userid,))
            record = cursor.fetchone()

            if record:
                cursor.execute(f"DELETE FROM {DB_TABLE} WHERE id = %s", (userid,))
                connection.commit()
                print(GREEN + f"Record with ID {userid} deleted successfully." + RESET)
            else:
                print(RED + f"No record found with ID {userid}." + RESET)

        elif realvalid_choice == 'SELECT':
            offset = 0
            while True:
                cursor.execute(f"SELECT COUNT(*) as total FROM {DB_TABLE}")
                total_records = cursor.fetchone()['total']
                if total_records == 0:
                    print(RED + "No records found in database." + RESET)
                    break

                limit_input = input(BLUE + "How many rows you want to see: " + RESET)
                if not limit_input.isdigit() or int(limit_input) <= 0:
                    print(RED + "Please enter a valid positive number." + RESET)
                    continue

                limit = int(limit_input)

                cursor.execute(f"SELECT * FROM {DB_TABLE} LIMIT {limit} OFFSET {offset}")
                records = cursor.fetchall()

                if not records:
                    print(YELLOW + "No more records to show." + RESET)
                    break

                print(GREEN + f"\nShowing records {offset + 1} to {offset + len(records)}:\n" + RESET)
                for record in records:
                    print(f"ID: {record['id']},\n Name: {record['name']},\n Email: {record['email']},\n Mobile: {record['mobile']}")

                offset += limit
                if offset >= total_records:
                    print(YELLOW + "\nNo more records left to show." + RESET)
                    break

                print(f"\n{BLUE}Do you want to see more Records or want to check Main Menu?{RESET}")
                print(f"{YELLOW}1. See more\n2. Main menu{RESET}")
                next_action = input(BLUE + "Enter your choice: " + RESET)

                if next_action == '1':
                    continue
                elif next_action == '2':
                    print(GREEN + "Returning to main menu..." + RESET)
                    break
                else:
                    print(RED + "Invalid choice, returning to main menu." + RESET)
                    break
                
        elif realvalid_choice == 'EXIT':
            print(GREEN + "Exiting the program... Have a great day!" + RESET)
            break
        
        elif realvalid_choice == 'UPDATE':

            cursor.execute(f"SELECT * FROM {DB_TABLE}")
            records = cursor.fetchall()
            if not records:
                print(RED + "No records available to update." + RESET)
                continue

            print(GREEN + "\nAvailable Records:\n" + RESET)
            for record in records:
                print(f"ID: {record['id']}, Name: {record['name']}, Email: {record['email']}, Mobile: {record['mobile']}")

            while True:
                userid = input(BLUE + "\nPlease give ID which you want to update: " + RESET)
                if not userid.isdigit():
                    print(RED + "Invalid ID. Please enter a numeric value." + RESET)
                    continue

                cursor.execute(f"SELECT * FROM {DB_TABLE} WHERE id = %s", (userid,))
                existing = cursor.fetchone()

                if existing:
                    break
                else:
                    print(RED + "Invalid ID, please enter a valid ID." + RESET)

            print(YELLOW + "\nOld Values Rakhni hai Too Shidha Enter Kardo.\n" + RESET)

            while True:
                print(f"Old name: {existing['name']}")
                new_name = input(BLUE + "Enter new name: " + RESET)
                if new_name == '':
                    new_name = existing['name']
                    break
                elif new_name.isalpha() and 5 <= len(new_name) <= 20:
                    break
                else:
                    print(RED + "Please enter a valid name (5-20 alphabetic characters)." + RESET)

            while True:
                print(f"Old email: {existing['email']}")
                new_email = input(BLUE + "Enter new email: " + RESET)
                if new_email == '':
                    new_email = existing['email']
                    break
                elif 13 <= len(new_email) <= 30 and new_email.endswith('@gmail.com'):
                    break
                else:
                    print(RED + "Please enter a valid email address (13-30 chars, must end with @gmail.com)." + RESET)

            while True:
                print(f"Old mobile: {existing['mobile']}")
                new_mobile = input(BLUE + "Enter new mobile: " + RESET)
                if new_mobile == '':
                    new_mobile = existing['mobile']
                    break
                elif new_mobile.isdigit() and len(new_mobile) == 10:
                    break
                else:
                    print(RED + "Please enter a valid 10-digit mobile number." + RESET)

            update_query = f"UPDATE {DB_TABLE} SET name = %s, email = %s, mobile = %s WHERE id = %s"
            cursor.execute(update_query, (new_name, new_email, new_mobile, userid))
            connection.commit()
            print(GREEN + f"\nRecord with ID {userid} updated successfully!" + RESET)

        else:
            print(YELLOW + "Work in progress (coming soon...)" + RESET)
    else:
        print(RED + 'Please enter a valid number' + RESET)
