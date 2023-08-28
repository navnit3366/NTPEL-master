import tkinter as tk
import mysql.connector
from tkinter import messagebox

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Ankita@227",
  database="test"
)

mycursor = mydb.cursor()

root = tk.Tk()
root.title("REGISTRATION FORM")
root.geometry("500x500")
usn = tk.StringVar()
name = tk.StringVar()
phone = tk.StringVar()
tk.Label(root,text="Enter your Name:").place(x=100,y=150)
tk.Entry(root,text=name).place(x=220,y=150)
tk.Label(root,text="Enter your USN:").place(x=100,y=200)
tk.Entry(root,text=usn).place(x=220,y=200)
tk.Label(root,text="Enter your phone no:").place(x=100,y=250)
tk.Entry(root,text=phone).place(x=220,y=250)
usn_get = usn.get()
name_get = name.get()
phone_get= phone.get()

def insert():
    usn_get = usn.get()
    name_get = name.get()
    phone_get = phone.get()
    sql_ins = "INSERT INTO people(usn,name,phone) VALUES(%s,%s,%s)"
    val = (usn_get,name_get,phone_get)
    mycursor.execute(sql_ins,val)
    #tk.Label(root,text="Registered Successfully!").pack(side=tk.BOTTOM)
    messagebox.showinfo('Result','Registered Successfully!')
    mydb.commit()

def update():
    usn_get = usn.get()
    name_get = name.get()
    phone_get = phone.get()
    sql_up = "UPDATE people SET name = %s,phone=%s WHERE usn=%s"
    val = (name_get,phone_get,usn_get)
    mycursor.execute(sql_up, val)
    #tk.Label(root,text="Updated Successfully!").pack(side=tk.BOTTOM)
    messagebox.showinfo('Result','Updated Successfully!')
    mydb.commit()


def delete():
    usn_get = usn.get()
    sql_del = "DELETE FROM people where usn= %s"
    val = (usn_get,)
    mycursor.execute(sql_del, val)
    #tk.Label(root,text="Deleted Successfully!").pack(side=tk.BOTTOM)
    messagebox.showinfo('Result','Deleted Successfully!')
    mydb.commit()

tk.Button(root,text="Register",command=insert).place(x=100,y=350)
tk.Button(root,text="Update",command=update).place(x=200,y=350)
tk.Button(root,text="Delete",command=delete).place(x=300,y=350)
root.mainloop()