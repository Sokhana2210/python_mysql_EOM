from tkinter import *
import mysql.connector
from tkinter import messagebox as mb
import sys
import os


root = Tk()
root.title("Databases")
root.geometry("350x300")
root.config(bg="light blue")
canvas = Canvas(root, width=335, height=135, bg="light blue")
canvas.place(x=0, y=125)
img = PhotoImage(file="index.png")
canvas.create_image(20, 20, anchor=NW, image=img)


def restart():
    py = sys.executable
    os.execl(py, py, * sys.argv)


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
            if fName.get() == '' or username.get() == "":
                mb.showerror()
            else:

                mycursor = mydb.cursor()
                sql = "Insert into users(full_name, username, password) values(%s,%s,%s)"
                mycursor.execute(sql, [(fn), (us), (pw)])
                mydb.commit()
                mb.showinfo("success", "Successfully registered")
                reg.destroy()
        except:
            mb.showerror("Error", "Error connecting to mysql")

    reg = Tk()
    reg.title("Registration")
    reg.geometry("450x450")
    reg.config(bg="yellow")

    fName_lbl = Label(reg, text="Full Name:")
    user_lbl = Label(reg, text="Username:")
    pswrd_lbl = Label(reg, text="Password:")
    fName = Entry(reg)
    username = Entry(reg)
    password = Entry(reg, show="*")
    reg_btn = Button(reg, text="Register", command=create)
    bck_btn = Button(reg, text="Back to MAIN MENU", command=restart)

    fName_lbl.place(x=5, y=10)
    user_lbl.place(x=5, y=55)
    pswrd_lbl.place(x=5, y=100)
    fName.place(x=80, y=10)
    username.place(x=80, y=55)
    password.place(x=80, y=100)
    reg_btn.place(x=150, y=150)
    bck_btn.place(x=200, y=250)


def admin_menu():
    def display():
        mydb = mysql.connector.connect(
        host="localhost",
        user="lifechoices",
        password="@Lifechoices1234",
        database="LifechoicesOnline",
        auth_plugin="mysql_native_password")

        mycursor= mydb.cursor()
        mycursor.execute("select * from users")

        for i in mycursor:
            listbox.insert('end', str(i))

    def remove():
        print(type(x),x)
        import mysql.connector
        mydb = mysql.connector.connect(
        host="localhost",
        user="lifechoices",
        password="@Lifechoices1234",
        database="LifechoicesOnline",
        auth_plugin ="mysql_native_password")

        mycursor = mydb.cursor()
        try:
            sql = "Delete from users where id=%s"
            mycursor.execute(sql, [x])
            mydb.commit()
        except:
            mb.showerror("error")

        print(mycursor.rowcount, "record removed.")

    def insertion():
        mydb = mysql.connector.connect(
        host="localhost",
        user="lifechoices",
        password="@Lifechoices1234",
        database="LifechoicesOnline",
        auth_plugin="mysql_native_password")

        mycursor= mydb.cursor()
        mycursor.execute("insert * from users")

        for i in mycursor:
            listbox.insert('end', str(i))

    def improve():
        mydb = mysql.connector.connect(
        host="localhost",
        user="lifechoices",
        password="@Lifechoices1234",
        database="LifechoicesOnline",
        auth_plugin="mysql_native_password")

        mycursor= mydb.cursor()
        mycursor.execute("select * from users")

        for i in mycursor:
            listbox.insert('end', str(i))

    adm = Tk()
    adm.title("Admin Menu")
    adm.geometry("500x500")
    adm.config(bg="green")
    id_get = Entry(adm)
    x=id_get.get()
    sel_btn = Button(adm, text="Display Registered Users", command=display)
    del_btn = Button(adm, text="Delete", command=remove)
    ins_btn = Button(adm, text="Insert", command=insertion)
    upd_btn = Button(adm, text="Update", command=improve)
    listbox = Listbox(adm, width=70)
    sel_btn.place(x=5, y=100)
    del_btn.place(x=200, y=100)
    ins_btn.place(x=200, y=150)
    upd_btn.place(x=200, y=200)
    listbox.place(x=5, y=230)

    id_get.place(x=3, y=30)
    adm.mainloop()


def admin():
    root.destroy()

    def admin_login():
        mydb = mysql.connector.connect(
            host="localhost",
            user="lifechoices",
            password="@Lifechoices1234",
            database="LifechoicesOnline",
            auth_plugin="mysql_native_password"
        )

        mycursor = mydb.cursor()
        usr1 = username1.get()
        psw1 = password1.get()
        sql = "select * from adminlogin where username = %s and password = %s"
        mycursor.execute(sql, [usr1, psw1])
        result1 = mycursor.fetchall()

        if result1:
            for i in result1:
                mb.showinfo("Welcome", "Admin login successful")
                admin_menu()
                break
        else:
            mb.showerror("Login Fail", "Error Somewhere")

    admin = Tk()
    admin.title("Administration Login")
    admin.geometry("450x450")
    admin.config(bg="black")

    user_lbl = Label(admin, text="Username:")
    pswrd_lbl = Label(admin, text="Password:")
    username1 = Entry(admin)
    password1 = Entry(admin, show="*")
    admin_btn = Button(admin, text="LOGIN", command=admin_login)
    bck_btn = Button(admin, text="Back to MAIN MENU", command=restart)

    user_lbl.place(x=5, y=55)
    pswrd_lbl.place(x=5, y=100)
    username1.place(x=80, y=55)
    password1.place(x=80, y=100)
    admin_btn.place(x=150, y=150)
    bck_btn.place(x=200, y=250)


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
