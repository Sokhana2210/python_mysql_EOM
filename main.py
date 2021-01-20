from tkinter import *
import mysql.connector
from tkinter import messagebox as mb

root = Tk()
root.title("Databases")
root.geometry("300x200")


def register():
    root.destroy()

    def create():
        fn = fName.get()
        us = username.get()
        pw = password.get()

        mydb = mysql.connector.connect(
            host="localhost",
            user="lifechoices",
            password="@Lifechoices1234",
            database="LifechoicesOnline",
            auth_plugin="mysql_native_password")

        try:
            mycursor = mydb.cursor()
            sql = "Insert into users(full_name, username, password) values(%s,%s,%s)"
            mycursor.execute(sql, [(fn), (us), (pw)])
            mydb.commit()
            mb.showinfo("success", "Successfully registered")
            reg.destroy()
        except:
            mb.showerror("Error","Error connecting to mysql")
            



    reg = Tk()
    reg.title("Registration")
    reg.geometry("450x450")

    fName_lbl = Label(reg, text="Full Name:")
    user_lbl = Label(reg, text="Username:")
    pswrd_lbl = Label(reg, text="Password:")
    fName = Entry(reg)
    username = Entry(reg)
    password = Entry(reg, show="*")
    reg_btn = Button(reg, text="Register", command=create)

    fName_lbl.place(x=5, y=10)
    user_lbl.place(x=5, y=55)
    pswrd_lbl.place(x=5, y=100)
    fName.place(x=80, y=10)
    username.place(x=80, y=55)
    password.place(x=80, y=100)
    reg_btn.place(x=150, y=150)


def admin_login():
    mb.showinfo("Success","Admin login successful")
    main = Tk()
    main.title("Databases")
    main.geometry("450x450")

    disp = Label(main, borderwidth=2, relief="ridge", width=55, anchor='w')

    disp.place(x=5, y=5)

    mybd = mysql.connector.connect(
        host="localhost",
        user="lifechoices",
        password="@Lifechoices1234",
        database="LifechoicesOnline",
        auth_plugin="mysql_native_password"
    )

    mycursor = mybd.cursor()
    xy = mycursor.execute('Select * from users')
    for i in mycursor:
        data = str(i)
        data = data[1: -1]
        data = data.split(',')
        disp['text'] += "\n"+str(data)

def admin():
        root.destroy()
        admin = Tk()
        admin.title("Administration Login")
        admin.geometry("450x450")

        user_lbl = Label(admin, text="Username:")
        pswrd_lbl = Label(admin, text="Password:")
        username = Entry(admin)
        password = Entry(admin, show="*")
        admin_btn = Button(admin, text="LOGIN", command=admin_login)

        user_lbl.place(x=5, y=55)
        pswrd_lbl.place(x=5, y=100)
        username.place(x=80, y=55)
        password.place(x=80, y=100)
        admin_btn.place(x=150, y=150)


def verify():
        mydb = mysql.connector.connect(
            host="localhost",
            user="lifechoices",
            password="@Lifechoices1234",
            database="LifechoicesOnline",
            auth_plugin="mysql_native_password"
        )

        mycursor = mydb.cursor()

        usr = username.get()
        psw = password.get()
        sql = "select * from users where username = %s and password = %s"
        mycursor.execute(sql, [usr, psw])
        result = mycursor.fetchall()

        if result:
            for i in result:
                logged()
                root.destroy()
                break
        else:
            mb.showerror("Login Fail", "Error Somewhere")


def logged():
    mb.showinfo("Success", "You have successfully logged in")
    root.destroy()


user_lbl = Label(root, text="Username:")
pswrd_lbl = Label(root, text="Password:")
username = Entry(root)
password = Entry(root, show="*")
login_btn = Button(root, text="Login", command=verify)
reg_btn = Button(root, text="Register", command=register)
admin_btn = Button(root, text="Admin Login", command=admin)

user_lbl.place(x=5, y=10)
pswrd_lbl.place(x=5, y=55)
username.place(x=80, y=10)
password.place(x=80, y=55)
login_btn.place(x=5, y=100)
reg_btn.place(x=100, y=100)
admin_btn.place(x=200, y=100)


root.mainloop()
