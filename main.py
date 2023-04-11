from tkinter import *
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect('users.db')
c=conn.cursor()
create = """CREATE TABLE IF NOT EXISTS users(username TEXT, pass TEXT)"""
c.execute(create)
INSERT_DATA = """INSERT INTO users VALUES(?,?)"""
SELECT_USER = """SELECT * FROM users where username=?"""
SELECT_DATA = """SELECT * FROM users where username=? and pass=?"""
temp = []


def login():
    username = t1.get()
    password = t2.get()
    c.execute(SELECT_USER, (username,))
    temp = c.fetchall()
    if (len(temp)):
        c.execute(SELECT_DATA, (username, password))
        if (len(c.fetchall())):
            messagebox.showinfo("Logged In!", "Successful Login")
            root.destroy()
        else:
            messagebox.showwarning("Unsuccessful", "Incorrect password")
    else:
        messagebox.showwarning("Unsuccessful", "User not found.")


def register():
    def submit():
        username = t3.get()
        password = t4.get()
        c.execute(SELECT_USER, (username,))
        temp = c.fetchall()
        if (len(temp)):
            messagebox.showerror("User Exists", "Username already exists. Please choose another username.")
        else:
            c.execute(INSERT_DATA, (username, password))
            conn.commit()
            messagebox.showinfo("New User saved!", "Registered Successfully")
            reg.withdraw()
            root.deiconify()

    reg = Toplevel()
    root.withdraw()
    reg.configure(background='white')
    reg.title("Simple App")
    l3 = Label(reg, text="Username: ")
    l4 = Label(reg, text="Password: ")
    t3 = Entry(reg)
    t4 = Entry(reg, show='*')
    b3 = Button(reg, text="Submit", command=submit)
    l3.grid(row=1, column=0)
    l4.grid(row=2, column=0)
    l3.configure(bg='white')
    l4.configure(bg='white')
    t3.grid(row=1, column=2)
    t4.grid(row=2, column=2)
    b3.grid(row=3, column=1)
    b3.configure(bg='white')


root = Tk()
root.configure(background='white')
root.title("Login App")
l1 = Label(root, text="Username: ")
l2 = Label(root, text="Password: ")
t1 = Entry(root)
t2 = Entry(root, show='*')
b1 = Button(root, text="Login", command=login)
b2 = Button(root, text="New User", command=register)
l1.grid(row=1, column=2)
l2.grid(row=2, column=2)
l1.configure(bg='white')
l2.configure(bg='white')
t1.grid(row=1, column=4)
t2.grid(row=2, column=4)
b1.grid(row=3, column=3)
b2.grid(row=4, column=3)
root.mainloop()