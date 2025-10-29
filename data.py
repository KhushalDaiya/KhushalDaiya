import mysql.connector  

connection = mysql.connector.connect(host='127.0.0.1',user='root',password="khus" ,database='database')
    
# print(connection.is_connected())

# cursor = connection.cursor()

# query_to_execute = "SELECT * FROM user;"

# cursor.execute(query_to_execute)
# data  = cursor.fetchall()
# print(data)

# # print(cursor)


cursor = connection.cursor()

name = input("Enter Name : ")
email = input("Enter Email : ")
mobile = input("Enter Mobile no.: ")


if not name.strip() or not email.strip() or not mobile.strip():
    print("Name, Email, and Mobile number cannot be empty.")

elif not email.endswith("@gmail.com"):
    print("Email must end with '@gmail.com'.")

elif not mobile.isdigit():
    print("Mobile number must contain only digits.")

elif len(mobile) != 10:
    print("Mobile number must be exactly 10 digits.")

else:
    query = "INSERT INTO user (name, email, mobile) VALUES (%s, %s, %s)"
    values = (name, email, mobile)
    cursor.execute(query, values)
    connection.commit()
    print("Data inserted successfully!")


