#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 19:06:49 2020

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
from SecondPage import *
from PIL import ImageTk,Image

#creating a a database connection 
conn = create_engine('mysql+pymysql://antara:pass@127.0.0.1/python_gui').connect()

#Checking if the connection is established
if(conn):
        print("Database Opened And Created Successfully")
else:
        print("Database Not Found")


# Designing Main(first) window

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("500x500")
    main_screen.title("Welcome to SpaceZ")
 
    Label(text="SpaceZ Phonebook", bg="orange", width="300", height="2", font=("TimesNewRoman", 20)).pack()
    Label(text="").pack()
    Button(text="Search", height="5", width="30",font=("TimesNewRoman", 20), command = search).pack()
    Label(text="").pack()
    Button(text="Register", height="5", width="30",font=("TimesNewRoman", 20), command=register).pack()

    main_screen.mainloop()


main_account_screen()