import mysql.connector  

connection = mysql.connector.connect(host='127.0.0.1',user='root',password="Satyampurohit0000" ,database='axixa')
    
# print(connection.is_connected())

# cursor = connection.cursor()

# query_to_execute = "SELECT * FROM bacha;"

# cursor.execute(query_to_execute)
# data  = cursor.fetchall()
# print(data)

# # print(cursor)


cursor = connection.cursor()

name = input("Name dalo: ")
email = input("Email dalo: ")
mobile = input("Mobile number dalo: ")


if email.endswith("@gmail.com"):
    query = "INSERT INTO bacha (name, email, mobile) VALUES (%s, %s, %s)"
    values = (name, email, mobile)
    cursor.execute(query, values)
    connection.commit()

    print("✅ Data inserted successfully!")
else:
    print("❌ Invalid email! Please enter a Gmail address (must end with @gmail.com).")