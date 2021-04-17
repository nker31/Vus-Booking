import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

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
    mail_ent = Entry(start_frm, width=18, textvariable=mail_spy)
    mail_ent.grid(row=1, column=1, ipady=5)
    mail_spy.set("email")
    pwd_ent = Entry(start_frm, width=18, textvariable=pwd_spy)
    pwd_ent.grid(row=2, column=1, ipady=5)

    # Check Box
    Checkbutton(start_frm, text="Remember me", bg="#F6E71D").grid(
        row=2, column=0, columnspan=2, sticky=S)
    # Button
    Button(start_frm, text="Register", width=12, command=regisframe).grid(
        row=3, column=0, ipady=13, sticky=E)
    Button(start_frm, text="Login", width=12, command=mainMenu).grid(
        row=3, column=1, ipady=13, sticky=W, padx=30)
    start_frm.grid(row=1, column=1, rowspan=3, columnspan=3, sticky=NSEW)


def regisframe():
    start_frm.destroy()
    main.title("VUS B : Registration")
    regis_frm = Frame(main, bg="#F6E71D")
    regis_frm.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)
    regis_frm.columnconfigure((0, 1), weight=1)
    # Header
    Label(regis_frm, image=regis_img, compound=LEFT,
          text="Register", font="helvetica 30 bold", bg="#F6E71D").grid(row=0, columnspan=2)
    # Body
    for i, data in enumerate(regis_list):
        Label(regis_frm, text=regis_list[i]+" :",
              font="helvetica 18 bold", bg="#F6E71D").grid(row=i+1, column=0, sticky=E)
    # Insert data part
    fname_ent = Entry(regis_frm, width=15)
    fname_ent.grid(row=1, column=1)
    lname_ent = Entry(regis_frm, width=15)
    lname_ent.grid(row=2, column=1)
    gender_spin = Spinbox(regis_frm,)
    regis_frm.grid(row=1, column=1, rowspan=3, columnspan=3, sticky=NSEW)

def mainMenu():
    print("This main menu")
    main.title("Vus Booking : MainMenu")
    main_menu = Frame(main, bg="#F6E71D")
    main_menu.rowconfigure((0,1,2,3,4,5,6,7,8,9,10),weight=1)
    main_menu.columnconfigure((0,1),weight=1)

    #Text
    Label(main_menu, image=logo_img, compound=LEFT, text="Vus Booking", font="helvetica 30 bold", fg="black",
          bg="#F6E71D").grid(row=0, column=0, columnspan=2)
    Label(main_menu, text='Select starting point', font="helvetica 16 bold", fg="black",
          bg="#F6E71D").grid(row=1, column=0, columnspan=2)
    Label(main_menu, text='Select destination point', font="helvetica 16 bold", fg="black",
          bg="#F6E71D").grid(row=3, column=0, columnspan=2)
    #Value Combobox      
    province = ('Pathum Thani','Nakhon Nayok','Chachoengsao','Samut Songkhram','Nakhon Pathom',
                'Chon Buri','Rayong','Phetchaburi','Saraburi','Ayutthaya','Ratchaburi')
    #use Combobox starting point
    province_select_sp = ttk.Combobox(main_menu, textvariable=selected_province)
    province_select_sp['values'] = province
    province_select_sp['state'] = 'readonly'
    province_select_sp.grid(row=2, column=0, columnspan=2, sticky='n', ipady=5, ipadx=5)
    
    #use Combobox destination point
    province_select_dp = ttk.Combobox(main_menu, textvariable=province)
    province_select_dp['values'] = province
    province_select_dp['state'] = 'readonly'
    province_select_dp.grid(row=4, column=0, columnspan=2, sticky='n', ipady=5, ipadx=5)

    main_menu.grid(row=1, column=1, rowspan=3, columnspan=3, sticky='news')
w = 600
h = 750
main = mainwindow()
# all variables
regis_list = ["Name", "Lastname", "Gender", "Phone num",
              "Email", "Password", "Confirm Password"]
mail_spy = StringVar()
pwd_spy = StringVar()
fname_info = StringVar()
lname_info = StringVar()
gender_info = StringVar()
phone_info = StringVar()
newmail_info = StringVar()
newpwd_info = StringVar()
newcfpwd_info = StringVar()
selected_province = StringVar()
logo_img = PhotoImage(file="image/logo.png").subsample(3, 3)
regis_img = PhotoImage(file="image/register.png").subsample(3, 3)

startmenu(main)
main.mainloop()
