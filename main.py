from tkinter import *
import mysql.connector
from tkinter import messagebox as mb
import tkinter as tk

def verify():
    mydb = mysql.connector.connect(user= "lifechoices",
    password = "@Lifechoices1234",
    host= "localhost",
    database= "town",
    auth_plugin="mysql_native_password")

    mycursor = mydb.cursor()

    usr = "Sokhana"
    psw = "2210"
    sql = "select * from Login where username = %s and password = %s"
    mycursor.execute(sql, [ (usr),(psw)])
    result = mycursor.fetchall()

    if result:
        for i in result:
            logged()
            root.destroy()
            break
    else:
        mb.showerror("lOGIN FAIL","Error Somewhere")

def logged():
    mb.showinfo("Success","You have successfully logged in")

    main = Tk()
    main.title("Databases")
    main.geometry("450x450")

    disp = Label(main, borderwidth=2, relief="ridge", width=55, anchor='w')

    disp.place(x=5,y=5)

    mydb = mydb.cursor()
    xy = mycursor.execute('Select * from town')
    for i in mycursor:
        data = str(i)
        data = data[1: -1]
        data = data.split(',')
        for j in data:
            print(j)
            print(type(j))

        disp['text'] += "/n"+str(data)
        print(i)



root = Tk()
root.title("Databases")
root.geometry("300x200")

user_lbl = Label(root, text="Username:")
pswrd_lbl = Label(root, text="Password:")
username = Entry(root)
password = Entry(root, show="*")
login_btn = Button(root, text="Login", command=verify)
reg_btn = Button(root, text="Register")

user_lbl.place(x=5, y=10)
pswrd_lbl.place(x=5, y=55)
username.place(x=80, y=10)
password.place(x=80, y=55)
login_btn.place(x=5, y=100)
reg_btn.place(x=100, y=100)


root.mainloop()












