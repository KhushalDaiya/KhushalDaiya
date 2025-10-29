import mysql.connector  

connection = mysql.connector.connect(host='127.0.0.1',user='root',password="khus" ,database='database')    
cursor = connection.cursor()
name = input("Enter Name : ")
email = input("Enter Email : ")
mobile = input("Enter Mobile no.: ")

if name.strip() == "" or email.strip() == "" or mobile.strip() == "":
    print("Name, Email, and Mobile number cannot be empty.")

else:
    query = "INSERT INTO user (name, email, mobile) VALUES (%s, %s, %s)"
    values = (name, email, mobile)
    cursor.execute(query, values)
    connection.commit()
    print("Data inserted successfully!")
