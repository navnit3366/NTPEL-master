import mysql.connector
import tkinter as tk

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Ankita@227",
  database="test"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")
for x in mycursor:
     print(x)

sql = "INSERT INTO people (name, phone) VALUES (%s, %s)"
val = ("Aaru", "5689921")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

sql = "DELETE FROM people WHERE name = 'Harsha'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")

sql = "UPDATE people SET phone = '8888888' WHERE name = 'Peter'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected") 



#print(mydb)