# Mohit Kharbanda
# Employee Incentive System

# import modules for Tkinter GUI
from tkinter import *
import sqlite3

root = Tk()

# code for creating the database
db = sqlite3.connect('loginDetails.db')
cur = db.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS employees"
            "(name TEXT, username TEXT, password TEXT)")
db.commit()
db.close()

# defining variables
newnameE = StringVar()
newunE = StringVar()
newpwE = StringVar()


def insert():

    name1 = newnameE.get()
    un1 = newunE.get()
    pw1 = newpwE.get()

    conn = sqlite3.connect('loginDetails.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO employees(name, username, password) VALUES(?,?,?)',
                       (name1.get(), un1.get(), pw1.get(),))
    db.close()
    print(newnameE.get())


def show():
    connt = sqlite3.connect('loginDetails.db')
    cursor = connt.cursor()
    cursor.execute('SELECT * FROM employees')
    for row in cursor.fetchall():
        print(row)


class login():

    def loginstart():
        # coding the login page

        root.title("Monitro System")
        root.geometry("800x600")
        root.configure(bg="cyan2")
        # code for on labels
        introttl = Label(root, text="Monitro System",
                         width=100, font="calibri 40 bold underline",
                         bg="cyan2", fg="#ffffff")
        introttl.pack()
        welcomettl = Label(root,
                           text="Welcome to the Employee Incentive System",
                           width=200, font="calibri 18",
                           bg="cyan2", fg="#ffffff")
        welcomettl.pack()
        # code for entry fields and associated labels
        un_prompt = Label(root, bg="cyan2", fg="white",
                          text="Please enter your username: ")
        un_prompt.place(x=225, y=130)
        un_entry = Entry(root)
        un_entry.place(x=400, y=130)
        pw_prompt = Label(root, bg="cyan2", fg="white",
                          text="Please enter your password: ")
        pw_prompt.place(x=225, y=170)
        pw_entry = Entry(root, show="*")
        pw_entry.place(x=400, y=170)
        # code for buttons on login page
        SignIn = Button(root,  text="Login", bg="white", fg="black")
        SignIn.place(x=375, y=300)
        Register = Button(root, text="Register", bg="white",
                          fg="black", command=registration.register)
        Register.place(x=425, y=300)


class registration():

    def register():

        # code for the registration page
        register_page = Tk()
        register_page.title("Please register")
        register_page.geometry("700x500")
        register_page.configure(bg="cyan2")
        # code for entry fields and associated labels
        register_message = Label(register_page, bg="cyan2", fg="white",
                                 text="Please Register Here: ")
        newname_prompt = Label(register_page, bg="cyan2", fg="white",
                               text="Please enter your full name")
        newnameE = Entry(register_page)
        newun_prompt = Label(register_page, bg="cyan2", fg="white",
                             text="Please enter a username: ")
        newunE = Entry(register_page)
        newpw_prompt = Label(register_page, bg="cyan2", fg="white",
                             text="Please enter a password: ")
        newpwE = Entry(register_page, show="*")
        newpw_prompt2 = Label(register_page, bg="cyan2", fg="white",
                              text="Please re-enter your password: ")
        newpw2 = Entry(register_page, show="*")
        # code for buttons on registration page
        register_btn = Button(
            register_page, text="Save Details", command=insert)
        register_message.pack()
        reg_SignIn = Button(register_page, text="Sign In", command=show)
        newname_prompt.pack()
        newnameE.pack()
        newun_prompt.pack()
        newunE.pack()
        newpw_prompt.pack()
        newpwE.pack()
        newpw_prompt2.pack()
        newpw2.pack()
        register_btn.pack()
        reg_SignIn.pack()


login.loginstart()


root.mainloop()
