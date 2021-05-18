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
    main.config(bg="#98ddca")
    main.rowconfigure((0, 1, 2, 3, 5), weight=1)
    main.columnconfigure((0, 1, 2, 3, 4), weight=1)
    img_icon = PhotoImage(file="image/bus.png").subsample(6, 6)
    main.iconphoto(False, img_icon)
    return main


def startmenu(main):  # login or register
    global mail_ent, pwd_ent, start_frm
    start_frm = Frame(main, bg="#ffd3b4")
    start_frm.rowconfigure((0, 1, 2, 3, 4), weight=1)
    start_frm.columnconfigure((0, 1), weight=1)
    # text

    Label(start_frm, image=logo_img, compound=LEFT, text="Vus Booking", font="helvetica 30 bold", fg="black", bg="#ffd3b4"
          ).grid(row=0, column=0, columnspan=2)
    Label(start_frm, text="Email", font="helvetica 23 bold", fg="black",
          bg="#ffd3b4").grid(row=1, column=0, sticky=E)
    Label(start_frm, text="Password", font="helvetica 23 bold", fg="black",
          bg="#ffd3b4").grid(row=2, column=0, sticky=E)

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
                    messagebox.showinfo("Admin", "Login Succesfully")
                    # Booking_seat()
                    Profile_Menu(mail_info.get())
                    mail_gb = mail_info.get()
                else:
                    messagebox.showwarning(
                        "Admin", "Username or Password\nInvalid")
                    pwd_ent.delete(0, END)
                    pwd_ent.focus_force()


def regisframe():
    global fname_ent, lname_ent, gender_spin, phone_ent, newmail_ent, newpwd_ent, cfpwd_ent, regis_frm
    main.title("VUS B : Registration")
    regis_frm = Frame(main, bg="#ffd3b4")

    regis_frm.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8), weight=1)
    regis_frm.columnconfigure((0, 1, 2), weight=1)
    # Header
    Label(regis_frm, image=regis_img, compound=LEFT,
          text="Register", font="helvetica 30 bold", bg="#ffd3b4").grid(row=0, columnspan=3)
    # Body
    for i, data in enumerate(regis_list):
        Label(regis_frm, text=regis_list[i]+" :",
              font="helvetica 18 bold", bg="#ffd3b4").grid(row=i+1, column=0, sticky=E)
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

    Button(regis_frm, width=10, text="Cancel",
           command=cancel_regis).grid(row=8, column=0)
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
                sql_insert = "insert into my_ticket (email) values (?)"
                cursor.execute(sql_insert, [newmail_info.get()])
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
    profile_menu = Frame(main, bg="#ffd3b4")
    profile_menu.columnconfigure((0, 1, 2), weight=1)
    profile_menu.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)

    # sql
    sql = "SELECT fname,lname,phonenum,birthdate,province FROM customer WHERE email=?"
    cursor.execute(sql, [mail_info.get()])
    result = cursor.fetchone()

    email = mail_info.get()
    print(email)

    # text
    Label(profile_menu, image=logo_img, compound=LEFT, text="Vus Booking", font="helvetica 30 bold", fg="black",
          bg="#ffd3b4").grid(row=0, column=0, columnspan=3)
    Label(profile_menu, text="Welcome : "+result[0]+" "+result[1], font="helvetica 16 bold",
          bg="#ffd3b4").grid(row=1, column=0, columnspan=2)

    # set real time

    # button
    Button(profile_menu, text="Booking Tickets", width=20,
           command=Booking_Menu).grid(row=2, column=0, columnspan=2, ipady=10)
    Button(profile_menu, text="Your Ticket", width=20,
           command=history).grid(row=3, column=0, columnspan=2, ipady=10)
    Button(profile_menu, text="Edit Profile", width=20,
           command=Edit_profile).grid(row=4, column=0, columnspan=2, ipady=10)
    Button(profile_menu, text='Exit', width=20,
           command=Exit_menu).grid(row=5, column=0, columnspan=2, ipady=10)

    profile_menu.grid(row=1, column=1, rowspan=3, columnspan=3, sticky=NSEW)


def Edit_profile():
    print("edit profile")
    global edit_profile, profi_fname, profi_lname, profi_phonenum, profi_birthdate, profi_province, profi_gender
    sql = "SELECT fname,lname,phonenum,birthdate,province,gender FROM customer WHERE email=?"
    cursor.execute(sql, [mail_info.get()])
    result_edt = cursor.fetchone()

    main.title("Vus Booking : Edit Profile")
    edit_profile = Frame(main, bg='#ffd3b4')
    edit_profile.columnconfigure((0, 1), weight=1)
    edit_profile.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), weight=1)

    # text & entry
    Label(edit_profile, image=logo_img, compound=LEFT, text="Vus Booking", font="helvetica 30 bold", fg="black",
          bg="#ffd3b4").grid(row=0, column=0, columnspan=2)
    Label(edit_profile, text='First Name', bg="#ffd3b4",
          font="helvetica 16 bold").grid(row=1, column=0)
    profi_fname = Entry(edit_profile, width=20,
                        textvariable=profi_fnameINFO, state=DISABLED)
    profi_fname.grid(row=1, column=1)

    Label(edit_profile, text='Last Name', bg="#ffd3b4",
          font="helvetica 16 bold").grid(row=2, column=0)
    profi_lname = Entry(edit_profile, width=20,
                        textvariable=profi_lnameINFO, state=DISABLED)
    profi_lname.grid(row=2, column=1)

    Label(edit_profile, text='Phone Number', bg="#ffd3b4",
          font="helvetica 16 bold").grid(row=3, column=0)
    profi_phonenum = Entry(edit_profile, width=20,
                           textvariable=profi_phonenumINFO, state=DISABLED)
    profi_phonenum.grid(row=3, column=1)

    Label(edit_profile, text='Birthdate', bg="#ffd3b4",
          font="helvetica 16 bold").grid(row=4, column=0)
    profi_birthdate = Entry(edit_profile, width=20,
                            textvariable=profi_birthdateINFO, state=DISABLED)
    profi_birthdate.grid(row=4, column=1)

    Label(edit_profile, text='Province', bg="#ffd3b4",
          font="helvetica 16 bold").grid(row=5, column=0)
    profi_province = Entry(edit_profile, width=20,
                           textvariable=profi_provinceINFO, state=DISABLED)
    profi_province.grid(row=5, column=1)

    Label(edit_profile, text='Gender', bg="#ffd3b4",
          font="helvetica 16 bold").grid(row=6, column=0)
    profi_gender = Entry(edit_profile, width=20,
                         textvariable=profi_genderINFO, state=DISABLED)
    profi_gender.grid(row=6, column=1)

    # button
    Button(edit_profile, text='Edit', command=Editable).grid(row=7, column=0)
    Button(edit_profile, text="Cancel",
           command=Cancel_edit).grid(row=7, column=1)

    # set text from sql
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
    Button(edit_profile, text='Update', command=Update_data).grid(
        row=8, column=0, columnspan=2)


def Update_data():
    print("update data")
    sql = """
            UPDATE customer
            SET fname=?, lname=?, phonenum=?, birthdate=?, province=?, gender=?
            WHERE email=?
    """
    cursor.execute(sql, [profi_fname.get(), profi_lname.get(), profi_phonenum.get(
    ), profi_birthdate.get(), profi_province.get(), profi_gender.get(), email])
    conn.commit()
    messagebox.showinfo("Admin", "Update Data Successfully")
    edit_profile.destroy()


def Booking_Menu():
    print("This booking menu")
    global booking_menu, province_select_sp, province_select_dp, date_button, date_text, date_show
    main.title("Vus Booking : Booking Menu")
    booking_menu = Frame(main, bg="#ffd3b4")
    booking_menu.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), weight=1)
    booking_menu.columnconfigure((0, 1), weight=1)

    # Text
    Label(booking_menu, image=logo_img, compound=LEFT, text="Vus Booking", font="helvetica 30 bold", fg="black",
          bg="#ffd3b4").grid(row=0, column=0, columnspan=2)
    Label(booking_menu, text='Select starting point', font="helvetica 16 bold", fg="black",
          bg="#ffd3b4").grid(row=1, column=0, columnspan=2)
    Label(booking_menu, text='Select destination point', font="helvetica 16 bold", fg="black",
          bg="#ffd3b4").grid(row=3, column=0, columnspan=2)

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
    province_select_dp = ttk.Combobox(
        booking_menu, textvariable=selected_province_dp)
    province_select_dp['values'] = province
    province_select_dp['state'] = 'readonly'
    province_select_dp.grid(row=4, column=0, columnspan=2,
                            sticky='n', ipady=5, ipadx=5)

    bkt_button = Radiobutton(booking_menu, text=tickets_list[1],
                             value=1, bg="#ffd3b4", font="helvetica 16 bold", fg="black")
    bkt_button.grid(row=5, column=0, columnspan=2)

    # select how many do you want to buy or booking tickets
    Label(booking_menu, text='Tickets : ', bg="#ffd3b4", font="helvetica 16 bold",
          fg="black").grid(row=6, column=0, sticky='e')
    tk_spin = Spinbox(booking_menu, from_=0, to=20,
                      width=8, textvariable=tickets)
    tk_spin.grid(row=6, column=1, sticky='w')

    # calendar
    date_button = Button(booking_menu, text="Date", width=10, command=calendar)
    date_button.grid(row=7, column=0, sticky=E)
    date_show = Label(booking_menu, text="",
                      textvariable=check_date, bg="#ffd3b4")
    check_date.set("DD/MM/YY")
    date_show.grid(row=7, column=1, sticky=W, padx=20)
    # Button
    Button(booking_menu, width=10, text="Cancel",
           command=cancelbooking).grid(row=8, column=0)
    Button(booking_menu, text='OK', width=10,
           command=checkradiobutton).grid(row=8, column=1)

    booking_menu.grid(row=1, column=1, rowspan=3, columnspan=3, sticky='news')


def Booking_car():
    global booking_car
    print("Booking Car")
    main.title("Vus Booking : Choose a trip")
    booking_car = Frame(main, bg="#ffd3b4")
    booking_car.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), weight=1)
    booking_car.columnconfigure((0, 1), weight=1)
    Label(booking_car, text="Choose a trip", bg="#ffd3b4").grid(
        row=0, column=0, columnspan=2)

    show_info_frame = Frame(booking_car, bg="lightyellow")
    show_info_frame.rowconfigure((0, 1, 2), weight=1)
    show_info_frame.columnconfigure((0, 1), weight=1)
    cal.get_date()
    Label(show_info_frame, image=home_img, text=province_select_sp.get(),
          bg="lightyellow", compound=LEFT).grid(row=0, column=0, sticky='w')
    Label(show_info_frame, image=location_img, text=province_select_dp.get(
    ), bg="lightyellow", compound=LEFT).grid(row=1, column=0, sticky='w', padx=10)
    Label(show_info_frame, image=calendar_img, text=cal.get_date(
    ), bg="lightyellow", compound=LEFT).grid(row=2, column=0, sticky='w', padx=8)
    show_info_frame.grid(row=1, column=0, columnspan=2,
                         sticky="NEWS", padx=15, pady=15)
    space = " " * 125
    space_2 = " " * 70

    button_car_1 = Button(booking_car, text=time_list[0]+" PM" + space + "Price   "+str(price_list[0]) + "   Bath" + "\n      Start :"+province_select_sp.get(
    ) + space_2 + "\nDestination : "+province_select_dp.get() + space_2 + "Seat : 10", anchor=W, relief=GROOVE, bg="lightyellow", command=lambda: trip_select(0))

    button_car_2 = Button(booking_car, text=time_list[1]+" PM" + space + "Price   "+str(price_list[1]) + "   Bath" + "\n      Start :"+province_select_sp.get(
    ) + space_2 + "\nDestination : "+province_select_dp.get() + space_2 + "Seat : 10", anchor=W, relief=GROOVE, bg="lightyellow", command=lambda: trip_select(1))

    button_car_3 = Button(booking_car, text=time_list[2]+" PM" + space + "Price   "+str(price_list[2]) + "   Bath" + "\n      Start :"+province_select_sp.get(
    ) + space_2 + "\nDestination : "+province_select_dp.get() + space_2 + "Seat : 10", anchor=W, relief=GROOVE, bg="lightyellow", command=lambda: trip_select(2))

    button_car_4 = Button(booking_car, text=time_list[3]+" PM" + space + "Price   "+str(price_list[3]) + "   Bath" + "\n      Start :"+province_select_sp.get(
    ) + space_2 + "\nDestination : "+province_select_dp.get() + space_2 + "Seat : 10", anchor=W, relief=GROOVE, bg="lightyellow", command=lambda: trip_select(3))

    button_list = [button_car_1, button_car_2, button_car_3, button_car_4]
    for i in range(number):
        button_list[i]
        button_list[i].grid(row=2+i, column=0, columnspan=2,
                            sticky="NEWS", pady=15, padx=15)

    booking_car.grid(row=1, column=1, rowspan=3, columnspan=3, sticky='news')

    Button(booking_car, text="Cancel", command=cancel_trip).grid(
        row=6, columnspan=2, column=0)


def Booking_seat():
    global booking_seat

    main.title("Vus Booking : Choose a seat")
    booking_seat = Frame(main, bg="#ffd3b4")
    booking_seat.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), weight=1)
    booking_seat.columnconfigure((0, 1, 2, 3, 4), weight=1)

    Label(booking_seat, text="Choose a seat", bg="#ffd3b4",
          font="helvetica 24 bold").grid(row=0, column=0, columnspan=5)
    Label(booking_seat, text="Left", bg="#ffd3b4",
          font="helvetica 10").grid(row=1, column=0, columnspan=2)
    Label(booking_seat, text="Right", bg="#ffd3b4",
          font="helvetica 10").grid(row=1, column=3, columnspan=2)
    for i, des in enumerate(seat_list_left):
        Checkbutton(booking_seat, text=des, compound=LEFT,
                    variable=check_seat[i], command=Check_seat, image=man_seat, bg="#ffd3b4").grid(row=i+2, column=0)
    for i, des in enumerate(seat_list_right):
        Checkbutton(booking_seat, text=des, compound=LEFT,
                    variable=check_seat[i+5], command=Check_seat, image=man_seat, bg="#ffd3b4").grid(row=i+2, column=4)
    # distance covid-19
    for i, des in enumerate(seat_list_left_dis):
        Button(booking_seat, text=des, compound=LEFT, image=man_seat,
               bg="#ffd3b4", command=distance, relief=RIDGE).grid(row=i+2, column=1)
    for i, des in enumerate(seat_list_right_dis):
        Button(booking_seat, text=des, compound=LEFT, image=man_seat,
               bg="#ffd3b4", command=distance, relief=RIDGE).grid(row=i+2, column=3)

    Label(booking_seat, text="Total seat :", textvariable=txt_total,
          bg="#ffd3b4").grid(row=7, columnspan=5, column=0)
    Button(booking_seat, text="Cancel", command=cancel_seat,
           width=8).grid(row=9, column=0, columnspan=5)
    Button(booking_seat, text="Ok", width=8, command=check_total).grid(
        row=8, column=0, columnspan=5)
    booking_seat.grid(row=1, column=1, rowspan=3, columnspan=3, sticky='news')


def Payment():
    global pay_ment, total_price
    main.title("Vus Booking : Payment")
    pay_ment = Frame(main, bg="#ffd3b4")
    pay_ment.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), weight=1)
    pay_ment.columnconfigure((0, 1), weight=1)
    Label(pay_ment, text="   Vus Booking Ticket", bg="#ffd3b4", font="helvetica 20",
          image=img_bus, compound=LEFT).grid(row=0, column=0, columnspan=2, sticky=W, padx=15)
    Label(pay_ment, text=province_select_sp.get() + " → " + province_select_dp.get() + "  "+time_select,
          bg="#ffd3b4", font="helvetica 20").grid(row=1, column=0, columnspan=2, sticky=W, padx=15)
    Label(pay_ment, text="Date : "+cal.get_date(), bg="#ffd3b4",
          font="helvetica 20").grid(row=2, column=0, columnspan=2, sticky=W, padx=15)
    Label(pay_ment, text="   "+province_select_sp.get() + " Station", bg="#ffd3b4",
          font="helvetica 20").grid(row=3, column=0, columnspan=2, sticky=W, padx=15)
    Label(pay_ment, text="   "+province_select_dp.get() + " Station", bg="#ffd3b4",
          font="helvetica 20").grid(row=4, column=0, columnspan=2, sticky=W, padx=15)
    Label(pay_ment, text="Normal economy class", bg="#ffd3b4",
          font="helvetica 20").grid(row=5, column=0, sticky=W, padx=15)
    Label(pay_ment, text="Price", bg="#ffd3b4", font="helvetica 20").grid(
        row=6, column=0, sticky=W, padx=15)
    Label(pay_ment, text=str(price_select) + "x" + str(tickets.get()),
          bg="#ffd3b4", font="helvetica 20").grid(row=6, column=1, sticky=E, padx=15)
    Label(pay_ment, text="Total ", bg="#ffd3b4", font="helvetica 20").grid(
        row=7, column=0, sticky=W, padx=15)
    total_price = tickets.get() * price_select
    Label(pay_ment, text=str(total_price)+" Baht", bg="#ffd3b4",
          font="helvetica 20").grid(row=7, column=1, sticky=E, padx=15)
    Label(pay_ment, image=img_qr, text="(Please scan QRcode with LINE)", bg="#ffd3b4",
          compound=TOP, font="helvetica 20").grid(row=8, column=0, columnspan=2, pady=3)

    Button(pay_ment, text="Ok", command=payment_success).grid(
        row=9, column=0, columnspan=2)
    pay_ment.grid(row=1, column=1, rowspan=3, columnspan=3, sticky='news')


def My_ticket():
    global my_ticket
    my_ticket = Frame(main, bg="#ffd3b4")
    my_ticket.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), weight=1)
    my_ticket.columnconfigure((0, 1), weight=1)

    Button(my_ticket, text="Cancel").grid(row=7, column=0, columnspan=2)
    my_ticket.grid(row=1, column=1, rowspan=3, columnspan=3, sticky='news')


def checkradiobutton():
    if province_select_sp.get() == "":
        messagebox.showinfo("system", 'Please Select starting point.')
    elif province_select_dp.get() == "":
        messagebox.showinfo("system", 'Please Select destination point.')
    elif province_select_sp.get() == province_select_dp.get():
        messagebox.showinfo("system", 'Please Select Different place.')
    elif tickets.get() == 0:
        messagebox.showinfo(
            "system", 'Please Enter the number of your tickets.')
    elif check_date.get() == "":
        messagebox.showinfo("system", 'Please Enter your date.')
    elif check_date.get() != "":
        fake_rng()
        Booking_car()


def Check_seat():
    global total
    total = 0
    for i, des in enumerate(seat_list):
        if check_seat[i].get():
            total = total + 1
    print(total)
    txt_total.set("Total seat :"+str(total))


def check_total():
    print("FUCK")
    print(tickets.get())
    print(total)
    print("YOU")
    if tickets.get() == total:
        Payment()
    else:
        messagebox.showwarning(
            "Peam", "Please choose your seat equal your tickets")


def calendar():
    global calendar_frame, date, cal
    print("calendar")
    calendar_frame = Frame(main, bg="#ffd3b4")
    calendar_frame.rowconfigure((0, 1, 2, 3), weight=1)
    calendar_frame.columnconfigure((0, 1), weight=1)
    # calendar
    cal = Calendar(calendar_frame, selectmode='day',
                   year=2021, month=5, day=16)
    cal.grid(row=0, column=0, columnspan=2, sticky='NEWS', pady=15, padx=15)

    # button
    Button(calendar_frame, text="Get Date", command=grad_date).grid(
        row=2, column=0, columnspan=2)
    Button(calendar_frame, text="Cancel", command=cancel_cal).grid(
        row=3, column=0, columnspan=2)

    calendar_frame.grid(row=1, column=1, rowspan=3,
                        columnspan=3, sticky='news')


def payment_success():
    print("i")
    sql = """UPDATE my_ticket 
            SET start =?,destination=?,time=?,total_price=?
            WHERE email=?
        """
    cursor.execute(sql, [province_select_sp.get(
    ), province_select_dp.get(), time_select, total_price, mail_gb])
    conn.commit()
    messagebox.showinfo(
        "Vus Booking", "Payment Successful✅\nPlease check your ticket in Ticket History")
    Profile_Menu(mail_gb)


def fake_rng():
    global number
    check_date_list = cal.get_date()
    x = check_date_list.split("/")
    if int(x[1]) % 2 == 0:
        print("even")
        number = 2
    else:
        print("odd")
        number = 4


def trip_select(num):

    global time_select, price_select
    print(num)
    time_select = time_list[num]
    price_select = price_list[num]
    print(time_select)
    print(price_select)
    booking_car.destroy()
    Booking_seat()


def distance():
    messagebox.showinfo("Covid-19", "ห่างกันสักพัก")


def history():
    print("i")
    My_ticket()


def grad_date():
    global test_date
    test_date = cal.get_date()
    check_date.set(cal.get_date())
    date_show.config(text=":" + test_date)
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


def cancel_trip():
    booking_car.destroy()


def Cancel_edit():
    print("cancel edit")
    main.title("Vus Booking : Profile Menu")
    edit_profile.destroy()


def cancel_regis():
    regis_frm.destroy()


def cancel_seat():
    booking_seat.destroy()
    check_seat


def Exit_menu():
    print("Exit menu")
    main.title("Vus Booking")
    profile_menu.destroy()
    pwd_ent.delete(0, END)
    pwd_ent.focus_force()


w = 600
h = 750
createconnection()
main = mainwindow()

# all variables
txt_total = StringVar()
txt_total.set("Total Seat : 0")
total = 0
test_date = ""
regis_list = ["Name", "Lastname", "Gender", "Phone num",
              "Email", "Password", "Confirm Password"]
gender_list = ["-", "Male", "Female", "Other"]
tickets_list = {0: 'Buy Ticket', 1: 'Booking Ticket'}

time_list = ["9.00", "12.30", "14.30", "18.30"]
price_list = [470, 530, 570, 600]

seat_list = ["A1", "A2", "A3", "A4", "A5", "C1", "C2", "C3", "C4", "C5"]
seat_list_left = ["A1", "A2", "A3", "A4", "A5"]
seat_list_right = ["C1", "C2", "C3", "C4", "C5"]
seat_list_left_dis = ["B1", "B2", "B3", "B4", "B5"]
seat_list_right_dis = ["D1", "D2", "D3", "D4", "D5"]
check_seat = [BooleanVar() for i in seat_list]


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
logo_img = PhotoImage(file="image/logo.png").subsample(3, 3)
regis_img = PhotoImage(file="image/register.png").subsample(3, 3)
home_img = PhotoImage(file="image/home.png").subsample(6, 6)
location_img = PhotoImage(file="image/location.png").subsample(9, 9)
calendar_img = PhotoImage(file="image/calendar.png").subsample(9, 9)
man_seat = PhotoImage(file="image/man_seat.png").subsample(9, 9)
img_qr = PhotoImage(file="image/qr_code.png")
img_bus = PhotoImage(file="image/bus.png").subsample(6, 6)
profi_fnameINFO = StringVar()
profi_lnameINFO = StringVar()
profi_phonenumINFO = StringVar()
profi_birthdateINFO = StringVar()
profi_provinceINFO = StringVar()
profi_genderINFO = StringVar()
number = 0
startmenu(main)
main.mainloop()
cursor.close()  # close cursor
conn.close()  # close database connection
