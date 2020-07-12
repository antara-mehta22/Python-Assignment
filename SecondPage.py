#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 18:15:02 2020

@author: antara
"""


#importing all necessary modules
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showinfo
import os
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from PIL import ImageTk,Image

#creating a a database connection 
conn = create_engine('mysql+pymysql://antara:pass@127.0.0.1/python_gui').connect()

#Checking if the connection is established
if(conn):
        print("Database Opened And Created Successfully")
else:
        print("Database Not Found")



#Custom function to enter employee details into the system
        
def register():
    global register_screen
    register_screen = Tk()
    #Toplevel(main_screen)
    register_screen.title("Enter Details")
    register_screen.geometry("500x500")#window size for the application

    global Fullname
    global Email
    global var
    global c
    global var1
    global depart

    #defining variables to enter details
    Fullname=StringVar()  #full name of the employee
    Email=StringVar()     #email address of the employee
    depart=StringVar()    #department of the employee
    var1 = StringVar()    #gender
    c=StringVar()         #country

       
  #form details   


    label_0 = Label(register_screen, text="Basic Details form",width=20,bg="orange",font=("TumesNewRoman", 30))
    label_0.place(x=90,y=53)


    label_1 = Label(register_screen, text="Full Name",width=20,bg="orange",font=("TumesNewRoman", 10))
    label_1.place(x=70,y=130)

    entry_1 = Entry(register_screen,textvar=Fullname)
    entry_1.place(x=240,y=130)

    label_2 = Label(register_screen, text="Email",width=20,bg="orange",font=("TumesNewRoman", 10))
    label_2.place(x=70,y=180)

    entry_2 = Entry(register_screen,textvar=Email)
    entry_2.place(x=240,y=180)

    label_3 = Label(register_screen, text="Gender",width=20,bg="orange",font=("TumesNewRoman", 10))
    label_3.place(x=70,y=230)

    Radiobutton(register_screen, text="Male",padx = 5, variable=var1, value=1).place(x=235,y=230)
    Radiobutton(register_screen, text="Female",padx = 20, variable=var1, value=2).place(x=290,y=230)
    
    label_5 = Label(register_screen, text="Department",bg="orange",width=20,font=("TumesNewRoman", 10))
    label_5.place(x=70,y=250)
    entry_5 = Entry(register_screen,textvar=depart)
    entry_5.place(x=240,y=250)

    label_4 = Label(register_screen, text="Select Country",bg="orange",width=20,font=("TumesNewRoman", 10))
    label_4.place(x=70,y=280)

    list1 = ['Canada','India','UK','Nepal','Iceland','South Africa'];

    droplist=OptionMenu(register_screen,c, *list1)
    droplist.config(width=15)
    c.set('select your country') 
    droplist.place(x=240,y=280)


    
#custom methods to insert into the mysql table
    def database():
       name1=Fullname.get()
       email=Email.get()
       var = var1.get()
       department=depart.get()
       country=c.get()

       t  = [name1, email, var,department,country]

       with conn:
           #Ret = connection.execute(sq.select([persons]))
           #conn.execute('CREATE TABLE IF NOT EXISTS Employees (Fullname varchar(50),Email varchar(50),Gender varchar(50),DEPARTMENT varchar(50),country varchar(50))')
           conn.execute("INSERT INTO Employees (FullName,Email,Gender,Department,country) VALUES(%s,%s,%s,%s,%s)",t)
           showinfo( title = "New employee Added", message = "Data inserted To table")
           #df = pd.DataFrame(ret.fetchall)
           #conn.commit()
    Button(register_screen, text="Register", width=10, height=2, bg="Orange", command = database).pack(side="bottom")




# Designing window for login

def search():
    global login_screen
    login_screen = Tk()
    #Toplevel(main_screen)
    login_screen.title("Search Employees here")
    login_screen.geometry("500x500")
    
    Label(login_screen, text="Search employees", bg="orange", width="300", height="2", font=("TimesNewRoman", 20)).pack()
    Label(text="").pack()

    entry=Entry(login_screen,width="500")
    entry.pack(side=TOP, expand=True)
    tree= ttk.Treeview(login_screen, column=("EMPLOYEE NAME", "EMAIL","BOX NUMBER", "GENDER", "DEPARTMENT","COUNTRY"), show='headings')
    def get_name():
        global person_name
        person_name = entry.get()
        variable=str(person_name)
        data = conn.execute("SELECT * FROM Employees WHERE Fullname =%s",(variable,))
        # create Treeview with 3 columns

        for row in data:
            Libcontect_label = Label(login_screen, text= row,fg="black",font=("Monaco",20))
            Libcontect_label.pack(pady=10,padx=10)
            showinfo( title = "Find results", message = "Search Successful")




    #Click to display results
    button = Button(login_screen, text="Display results", bg="orange",  height="3", width="20",font=("TimesNewRoman", 20),command=get_name)
    button.pack()


