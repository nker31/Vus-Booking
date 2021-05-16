from os import stat_result
import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import *

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
    pwd_ent = Entry(start_frm, width=18, textvariable=pwd_info, show='*')
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
                    Profile_Menu(mail_info.get())
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

def Profile_Menu(user):
    print("This profile menu")
    global profile_menu, email
    main.title("Vus Booking : Profile Menu")
    profile_menu = Frame(main, bg="#F6E71D")
    profile_menu.columnconfigure((0,1,2), weight=1)
    profile_menu.rowconfigure((0,1,2,3,4,5,6), weight=1)

    # sql
    sql = "SELECT fname,lname,phonenum,birthdate,province FROM customer WHERE email=?"
    cursor.execute(sql,[mail_info.get()])
    result = cursor.fetchone()

    email = mail_info.get()
    print(email)

    #text
    Label(profile_menu, image=logo_img, compound=LEFT, text="Vus Booking", font="helvetica 30 bold", fg="black",
          bg="#F6E71D").grid(row=0, column=0, columnspan=3)
    Label(profile_menu, text="Welcome : "+result[0]+" "+result[1], font="helvetica 16 bold",
    bg="#F6E71D").grid(row=1, column=0, columnspan=2)

    #set real time

    #button
    Button(profile_menu, text="Booking or Buy Tickets", width=20,
    command=Booking_Menu).grid(row=2, column=0, columnspan=2, ipady=10)
    Button(profile_menu, text="Edit Profile", width=20,
    command=Edit_profile).grid(row=3, column=0, columnspan=2, ipady=10)
    Button(profile_menu, text='Exit', width=20,
    command=Exit_menu).grid(row=4, column=0, columnspan=2, ipady=10)

    profile_menu.grid(row=1, column=1, rowspan=3, columnspan=3, sticky=NSEW)

def Edit_profile():
    print("edit profile")
    global edit_profile,profi_fname,profi_lname,profi_phonenum,profi_birthdate,profi_province,profi_gender
    sql = "SELECT fname,lname,phonenum,birthdate,province,gender FROM customer WHERE email=?"
    cursor.execute(sql,[mail_info.get()])
    result_edt = cursor.fetchone()

    main.title("Vus Booking : Edit Profile")
    edit_profile = Frame(main, bg='#F6E71D')
    edit_profile.columnconfigure((0,1), weight=1)
    edit_profile.rowconfigure((0,1,2,3,4,5,6,7,8,9),weight=1)

    # text & entry
    Label(edit_profile, image=logo_img, compound=LEFT, text="Vus Booking", font="helvetica 30 bold", fg="black",
          bg="#F6E71D").grid(row=0, column=0, columnspan=2)
    Label(edit_profile, text='First Name', bg="#F6E71D", font="helvetica 16 bold").grid(row=1, column=0)
    profi_fname = Entry(edit_profile, width=20, textvariable=profi_fnameINFO, state=DISABLED)
    profi_fname.grid(row=1, column=1)

    Label(edit_profile, text='Last Name', bg="#F6E71D", font="helvetica 16 bold").grid(row=2, column=0)
    profi_lname = Entry(edit_profile, width=20, textvariable=profi_lnameINFO, state=DISABLED)
    profi_lname.grid(row=2, column=1)

    Label(edit_profile, text='Phone Number', bg="#F6E71D", font="helvetica 16 bold").grid(row=3, column=0)
    profi_phonenum = Entry(edit_profile, width=20, textvariable=profi_phonenumINFO, state=DISABLED)
    profi_phonenum.grid(row=3, column=1)

    Label(edit_profile, text='Birthdate', bg="#F6E71D", font="helvetica 16 bold").grid(row=4, column=0)
    profi_birthdate = Entry(edit_profile, width=20, textvariable=profi_birthdateINFO, state=DISABLED)
    profi_birthdate.grid(row=4, column=1)

    Label(edit_profile, text='Province', bg="#F6E71D", font="helvetica 16 bold").grid(row=5, column=0)
    profi_province = Entry(edit_profile, width=20, textvariable=profi_provinceINFO, state=DISABLED)
    profi_province.grid(row=5, column=1)

    Label(edit_profile, text='Gender', bg="#F6E71D", font="helvetica 16 bold").grid(row=6, column=0)
    profi_gender = Entry(edit_profile, width=20, textvariable=profi_genderINFO, state=DISABLED)
    profi_gender.grid(row=6, column=1)

    # button
    Button(edit_profile, text='Edit', command=Editable).grid(row=7, column=0)
    Button(edit_profile, text="Cancel", command=Cancel_edit).grid(row=7, column=1)

    #set text from sql
    profi_fnameINFO.set(result_edt[0])
    profi_lnameINFO.set(result_edt[1])
    profi_phonenumINFO.set(result_edt[2])
    profi_birthdateINFO.set(result_edt[3])
    profi_provinceINFO.set(result_edt[4])
    profi_genderINFO.set(result_edt[5])

    edit_profile.grid(row=1, column=1, rowspan=3, columnspan=3, sticky=NSEW)

def Editable():
    print("Editable")
    profi_fname.config(state=NORMAL)
    profi_lname.config(state=NORMAL)
    profi_phonenum.config(state=NORMAL)
    profi_birthdate.config(state=NORMAL)
    profi_province.config(state=NORMAL)
    profi_gender.config(state=NORMAL)
    Button(edit_profile, text='Update', command=Update_data).grid(row=8, column=0, columnspan=2)

def Update_data():
    print("update data")
    sql = """
            UPDATE customer
            SET fname=?, lname=?, phonenum=?, birthdate=?, province=?, gender=?
            WHERE email=?
    """
    cursor.execute(sql,[profi_fname.get(), profi_lname.get(), profi_phonenum.get(), profi_birthdate.get(), profi_province.get(), profi_gender.get(), email])
    conn.commit()
    messagebox.showinfo("Admin","Update Data Successfully")
    edit_profile.destroy()

def Booking_Menu():
    print("This booking menu")
    global booking_menu,province_select_sp,province_select_dp,date_button,date_text,date_show
    main.title("Vus Booking : Booking Menu")
    booking_menu = Frame(main, bg="#F6E71D")
    booking_menu.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), weight=1)
    booking_menu.columnconfigure((0, 1), weight=1)

    # Text
    Label(booking_menu, image=logo_img, compound=LEFT, text="Vus Booking", font="helvetica 30 bold", fg="black",
          bg="#F6E71D").grid(row=0, column=0, columnspan=2)
    Label(booking_menu, text='Select starting point', font="helvetica 16 bold", fg="black",
          bg="#F6E71D").grid(row=1, column=0, columnspan=2)
    Label(booking_menu, text='Select destination point', font="helvetica 16 bold", fg="black",
          bg="#F6E71D").grid(row=3, column=0, columnspan=2)
    
    # Value Combobox
    province = ('Pathum Thani', 'Nakhon Nayok', 'Bangkok', 'Nakhon Pathom',
                'Chon Buri', 'Rayong', 'Phetchaburi', 'Saraburi', 'Ayutthaya', 'Ratchaburi')
    
    # use Combobox starting point
    province_select_sp = ttk.Combobox(
        booking_menu, textvariable=selected_province_sp)
    province_select_sp['values'] = province
    province_select_sp['state'] = 'readonly'
    province_select_sp.grid(row=2, column=0, columnspan=2,
                            sticky='n', ipady=5, ipadx=5)

    # use Combobox destination point
    province_select_dp = ttk.Combobox(booking_menu, textvariable=selected_province_dp)
    province_select_dp['values'] = province
    province_select_dp['state'] = 'readonly'
    province_select_dp.grid(row=4, column=0, columnspan=2,
                            sticky='n', ipady=5, ipadx=5)
    
    # check buy or booking tickets
    bt_button = Radiobutton(booking_menu, text=tickets_list[0], variable=tickets,
    value=1, bg="#F6E71D", font="helvetica 16 bold", fg="black")
    bt_button.grid(row=5, column=0)

    bkt_button = Radiobutton(booking_menu, text=tickets_list[1], variable=tickets,
    value=2, bg="#F6E71D", font="helvetica 16 bold", fg="black")
    bkt_button.grid(row=5, column=1)
    
    # select how many do you want to buy or booking tickets
    Label(booking_menu, text='Tickets : ', bg="#F6E71D", font="helvetica 16 bold",
    fg="black").grid(row=6, column=0, sticky='e')
    tk_spin = Spinbox(booking_menu, from_= 0, to = 100, width=8,textvariable=spin_value)
    tk_spin.grid(row=6, column=1, sticky='w')

    #calendar
    date_button = Button(booking_menu,text="Date",width=10,command=calendar)
    date_button.grid(row=7,column=0,sticky=E)
    date_show = Label(booking_menu,text="",textvariable=check_date,bg="#F6E71D")
    date_show.grid(row=7,column=1,sticky=W,padx=20)
    # Button
    Button(booking_menu, text='Cancel', width=10, command=cancelbooking).grid(row=8, column=0)
    Button(booking_menu, text='OK', width=10, command=checkradiobutton).grid(row=8, column=1)

    booking_menu.grid(row=1, column=1, rowspan=3, columnspan=3, sticky='news')

def checkradiobutton():
    print(test_date)
    if province_select_sp.get() == "":
        messagebox.showinfo("system",'Please Select starting point.')
    elif province_select_dp.get() == "":
        messagebox.showinfo("system",'Please Select destination point.')
    elif province_select_sp.get() == province_select_dp.get():
        messagebox.showinfo("system",'Please Select Different place.')
    elif tickets.get() == 0:
        messagebox.showinfo("system",'Please Select type tickets.')
    elif spin_value.get() == "0":
        messagebox.showinfo("system",'Please Enter the number of your tickets.')
    elif tickets.get() == 1:
        messagebox.showinfo("system",'you selected buy tickets.')
        return 1
    elif tickets.get() == 2:
        messagebox.showinfo('system','you selected booking ticket.')
        return 2
    elif check_date.get() == "":
        messagebox.showinfo("system",'Please Enter your date.')
    else :
        print("I")
    
def calendar():
    global calendar_frame,date,cal
    print("calendar")
    calendar_frame = Frame(main, bg="#F6E71D")
    calendar_frame.rowconfigure((0, 1, 2, 3), weight=1)
    calendar_frame.columnconfigure((0, 1), weight=1)
    #calendar
    cal = Calendar(calendar_frame, selectmode = 'day',year = 2021, month = 5,day = 16)
    cal.grid(row=0,column=0,columnspan=2,sticky='NEWS',pady=15,padx=15)

    #button
    Button(calendar_frame, text = "Get Date",command = grad_date).grid(row=2,column=0,columnspan=2)
    Button(calendar_frame, text = "Cancel",command = cancel_cal).grid(row=3,column=0,columnspan=2)

    
    calendar_frame.grid(row=1, column=1, rowspan=3, columnspan=3, sticky='news')

def grad_date():
    global test_date
    test_date = cal.get_date()
    check_date.set(cal.get_date())
    date_show.config(text= ":" + test_date)
    calendar_frame.destroy()

def cancel_cal():
    calendar_frame.destroy()

def cancelbooking():
    booking_menu.destroy()
    selected_province_sp.set("")
    selected_province_dp.set("")
    tickets.set(0)
    spin_value.set(0)
    check_date.set("")

def Cancel_edit():
    print("cancel edit")
    main.title("Vus Booking : Profile Menu")
    edit_profile.destroy()

def Exit_menu():
    print("Exit menu")
    main.title("Vus Booking")
    profile_menu.destroy()
    pwd_ent.delete(0,END)
    pwd_ent.focus_force()

w = 600
h = 750
createconnection()
main = mainwindow()

# all variables
test_date = ""
regis_list = ["Name", "Lastname", "Gender", "Phone num",
              "Email", "Password", "Confirm Password"]
gender_list = ["-", "Male", "Female", "Other"]
tickets_list = {0: 'Buy Ticket', 1: 'Booking Ticket'}
tickets = IntVar()
tickets.set(0)
tk_spin = IntVar()
tk_spin.set(0)
check_date = StringVar()
check_date.set("")
spin_value = StringVar()
mail_info = StringVar()
pwd_info = StringVar()
fname_info = StringVar()
lname_info = StringVar()
gender_info = StringVar()
phone_info = StringVar()
newmail_info = StringVar()
newpwd_info = StringVar()
newcfpwd_info = StringVar()
selected_province_sp = StringVar()
selected_province_dp = StringVar()
logo_img = PhotoImage(
    file="image/logo.png").subsample(3, 3)
regis_img = PhotoImage(file="image/register.png").subsample(3, 3)

profi_fnameINFO = StringVar()
profi_lnameINFO = StringVar()
profi_phonenumINFO = StringVar()
profi_birthdateINFO = StringVar()
profi_provinceINFO = StringVar()
profi_genderINFO = StringVar()

startmenu(main)
main.mainloop()
cursor.close()  # close cursor
conn.close()  # close database connection
