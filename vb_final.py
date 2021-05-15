import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


def createconnection():  # connect to database
    global conn, cursor
    conn = sqlite3.connect("vus_db.db")
    cursor = conn.cursor()


def mainwindow():
    main = Tk()

    x = main.winfo_screenwidth()/2 - w/2
    y = main.winfo_screenheight()/2 - h/2
    main.geometry("%dx%d+%d+%d" % (w, h, x, y))
    main.title("Vus Booking")
    main.config(bg="black")
    main.rowconfigure((0, 1, 2, 3, 5), weight=1)
    main.columnconfigure((0, 1, 2, 3, 4), weight=1)

    return main


def startmenu(main):  # login or register
    global mail_ent, pwd_ent, start_frm
    start_frm = Frame(main, bg="#F6E71D")
    start_frm.rowconfigure((0, 1, 2, 3, 4), weight=1)
    start_frm.columnconfigure((0, 1), weight=1)
    # text

    Label(start_frm, image=logo_img, compound=LEFT, text="Vus Booking", font="helvetica 30 bold", fg="black",
          bg="#F6E71D").grid(row=0, column=0, columnspan=2)
    Label(start_frm, text="Email", font="helvetica 23 bold", fg="black",
          bg="#F6E71D").grid(row=1, column=0, sticky=E)
    Label(start_frm, text="Password", font="helvetica 23 bold", fg="black",
          bg="#F6E71D").grid(row=2, column=0, sticky=E)
    # Entry
    mail_ent = Entry(start_frm, width=18, textvariable=mail_info)
    mail_ent.grid(row=1, column=1, ipady=5)
    mail_info.set("email")
    pwd_ent = Entry(start_frm, width=18, textvariable=pwd_info)
    pwd_ent.grid(row=2, column=1, ipady=5)

    # Button
    Button(start_frm, text="Register", width=12, command=regisframe).grid(
        row=3, column=0, ipady=13, sticky=E)
    Button(start_frm, text="Login", width=12, command=loginclick).grid(
        row=3, column=1, ipady=13, sticky=W, padx=30)
    start_frm.grid(row=1, column=1, rowspan=3, columnspan=3, sticky=NSEW)


def loginclick():
    global mail_gb
    print("Login clicked")
    if mail_info.get() == "":
        messagebox.showwarning("Admin", "Please enter username")
        mail_ent.focus_force()
    else:
        sql = "select * from customer where email=?"
        cursor.execute(sql, [mail_info.get()])
        result = cursor.fetchall()
        print(result)
        if result:
            if pwd_info.get() == "":
                messagebox.showwarning("Admin", "Please enter password")
                pwd_ent.focus_force()
            else:
                sql = "select * from customer where email=? and pwd=?"
                cursor.execute(sql, [mail_info.get(), pwd_info.get()])
                result = cursor.fetchone()
                print(result)
                if result:
                    messagebox.showwarning("Admin", "Login Succesfully")
                    mainMenu(mail_info.get())
                    mail_gb = mail_info.get()
                else:
                    messagebox.showwarning(
                        "Admin", "Username or Password\nInvalid")
                    pwd_ent.delete(0, END)
                    pwd_ent.focus_force()


def regisframe():
    global fname_ent, lname_ent, gender_spin, phone_ent, newmail_ent, newpwd_ent, cfpwd_ent, regis_frm
    start_frm.destroy()
    main.title("VUS B : Registration")
    regis_frm = Frame(main, bg="#F6E71D")
    regis_frm.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8), weight=1)
    regis_frm.columnconfigure((0, 1, 2), weight=1)
    # Header
    Label(regis_frm, image=regis_img, compound=LEFT,
          text="Register", font="helvetica 30 bold", bg="#F6E71D").grid(row=0, columnspan=3)
    # Body
    for i, data in enumerate(regis_list):
        Label(regis_frm, text=regis_list[i]+" :",
              font="helvetica 18 bold", bg="#F6E71D").grid(row=i+1, column=0, sticky=E)
    # Insert data part
    fname_ent = Entry(regis_frm, width=20, textvariable=fname_info)
    fname_ent.grid(row=1, column=1, columnspan=2, sticky=W, padx=(5, 0))

    lname_ent = Entry(regis_frm, width=20, textvariable=lname_info)
    lname_ent.grid(row=2, column=1, columnspan=2, sticky=W, padx=(5, 0))

    gender_spin = Spinbox(regis_frm, values=gender_list,
                          width=19, justify=CENTER)
    gender_spin.grid(row=3, column=1, columnspan=2, sticky=W, padx=(5, 0))

    phone_ent = Entry(regis_frm, width=20, textvariable=phone_info)
    phone_ent.grid(row=4, column=1, columnspan=2, sticky=W, padx=(5, 0))

    newmail_ent = Entry(regis_frm, width=20, textvariable=newmail_info)
    newmail_ent.grid(row=5, column=1, columnspan=2, sticky=W, padx=(5, 0))

    newpwd_ent = Entry(regis_frm, width=20, textvariable=newpwd_info)
    newpwd_ent.grid(row=6, column=1, columnspan=2, sticky=W, padx=(5, 0))

    cfpwd_ent = Entry(regis_frm, width=20, textvariable=newcfpwd_info)
    cfpwd_ent.grid(row=7, column=1, columnspan=2, sticky=W, padx=(5, 0))

    Button(regis_frm, width=10, text="Cancel").grid(row=8, column=0)
    Button(regis_frm, width=10, text="Register",
           command=registration).grid(row=8, column=2)

    regis_frm.grid(row=1, column=1, rowspan=3, columnspan=3, sticky=NSEW)


def registration():  # Notification for registration
    if fname_info.get() == "":
        messagebox.showwarning("Admin", "Please enter Fullname")
        fname_ent.focus_force()
    elif lname_info.get() == "":
        messagebox.showwarning("Admin", "Please enter Lastname")
        lname_ent.focus_force()
    elif gender_spin.get() == "-":
        messagebox.showwarning("Admin", "Please select gender")
    elif phone_info.get() == "":
        messagebox.showwarning("Admin", "Please enter phone number")
        phone_ent.focus_force()
    elif newmail_info.get() == "":
        messagebox.showwarning("Admin", "Please enter Email")
        newmail_ent.focus_force()
    elif newpwd_info.get() == "":
        messagebox.showwarning("Admin", "Please enter new password")
        newpwd_ent.focus_force()
    elif newcfpwd_info.get() == "":
        messagebox.showwarning("Admin", "Please enter confirm")
        cfpwd_ent.focus_force()
    else:
        sql = "select * from customer where email=?"
        cursor.execute(sql, [newmail_info.get()])
        result = cursor.fetchall()
        if result:
            messagebox.showwarning(
                "Admin", "Email is already exists\nPlease try another email")
            newmail_ent.select_range(0, END)
            newmail_ent.focus_force()
        else:
            if newpwd_info.get() == newcfpwd_info.get():
                sql_insert = "insert into customer (email,pwd,fname,lname,phonenum,gender)values(?,?,?,?,?,?)"
                cursor.execute(sql_insert, [newmail_info.get(), newpwd_info.get(), fname_info.get(
                ), lname_info.get(), phone_info.get(), gender_spin.get()])
                conn.commit()
                # retrivedata()
                messagebox.showinfo("Admin", "Registration Successfully")
                fname_ent.delete(0, END)
                lname_ent.delete(0, END)
                phone_ent.delete(0, END)
                newmail_ent.delete(0, END)
                newpwd_ent.delete(0, END)
                cfpwd_ent.delete(0, END)
                regis_frm.destroy()
                startmenu(main)
                mail_ent.focus_force()
            else:
                messagebox.showwarning(
                    "admin", "The confirm password not match")


def mainMenu(user):
    print("This main menu")
    main.title("Vus Booking : MainMenu")
    main_menu = Frame(main, bg="#F6E71D")
    main_menu.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), weight=1)
    main_menu.columnconfigure((0, 1), weight=1)

    # Text
    Label(main_menu, image=logo_img, compound=LEFT, text="Vus Booking", font="helvetica 30 bold", fg="black",
          bg="#F6E71D").grid(row=0, column=0, columnspan=2)
    Label(main_menu, text='Select starting point', font="helvetica 16 bold", fg="black",
          bg="#F6E71D").grid(row=1, column=0, columnspan=2)
    Label(main_menu, text='Select destination point', font="helvetica 16 bold", fg="black",
          bg="#F6E71D").grid(row=3, column=0, columnspan=2)
    # Value Combobox
    province = ('Pathum Thani', 'Nakhon Nayok', 'Bangkok', 'Nakhon Pathom',
                'Chon Buri', 'Rayong', 'Phetchaburi', 'Saraburi', 'Ayutthaya', 'Ratchaburi')
    # use Combobox starting point
    province_select_sp = ttk.Combobox(
        main_menu, textvariable=selected_province)
    province_select_sp['values'] = province
    province_select_sp['state'] = 'readonly'
    province_select_sp.grid(row=2, column=0, columnspan=2,
                            sticky='n', ipady=5, ipadx=5)

    # use Combobox destination point
    province_select_dp = ttk.Combobox(main_menu, textvariable=province)
    province_select_dp['values'] = province
    province_select_dp['state'] = 'readonly'
    province_select_dp.grid(row=4, column=0, columnspan=2,
                            sticky='n', ipady=5, ipadx=5)

    main_menu.grid(row=1, column=1, rowspan=3, columnspan=3, sticky='news')


w = 600
h = 750
createconnection()
main = mainwindow()
# all variables
regis_list = ["Name", "Lastname", "Gender", "Phone num",
              "Email", "Password", "Confirm Password"]
gender_list = ["-", "Male", "Female", "Other"]
mail_info = StringVar()
pwd_info = StringVar()
fname_info = StringVar()
lname_info = StringVar()
gender_info = StringVar()
phone_info = StringVar()
newmail_info = StringVar()
newpwd_info = StringVar()
newcfpwd_info = StringVar()
selected_province = StringVar()
logo_img = PhotoImage(
    file="image/logo.png").subsample(3, 3)
regis_img = PhotoImage(file="image/register.png").subsample(3, 3)

startmenu(main)
main.mainloop()
cursor.close()  # close cursor
conn.close()  # close database connection
