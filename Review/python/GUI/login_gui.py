#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from tkinter import *
from tkinter import messagebox
import pickle

top = Tk()
top.title('welcome to learn tkinter')
top.geometry('500x300')  # 顶层窗口的大小

Label(top, text='Username:').place(x=50, y=50)
Label(top, text='passworld:').place(x=50, y=90)

var_username = StringVar()
entry_username = Entry(top, textvariable=var_username)
entry_username.place(x=160, y=50)

var_pwd = StringVar()
entry_pad = Entry(top, textvariable=var_pwd, show='*')
entry_pad.place(x=160, y=90)

def usr_login():
    usr_name=var_username.get()
    usr_pwd=var_pwd.get()
    try:
        with open('usrs_info.txt','rb') as usr_file:
            usrs_info=pickle.load(usr_file)
    except FileNotFoundError:
        with open('usrs_info.txt', 'wb') as usr_file:
            usrs_info={'admin':'admin'}
            pickle.dump(usrs_info,usr_file)
    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            messagebox.showinfo(message='Welcome back  '+usr_name)
        else:
            messagebox.showerror(message='password is wrong,try again')
    else:
        is_signup=messagebox.askyesno('you have not sign up yet,sign up?')
        if is_signup:
            usr_signup()

def usr_signup():
    def signup_to():
        nn=new_name.get()
        np=new_pwd.get()
        npf=new_pwd_confirm.get()
        with open('usrs_info.txt', 'rb') as usr_file:
            exist_userinfo=pickle.load(usr_file)
        if np!=npf:
            messagebox.showerror('Error','Password and confirm Password must be same')
        elif nn in exist_userinfo:
            messagebox.showerror('Error','The User has already signed up')
        else:
            exist_userinfo[nn]=np
            with open('usrs_info.txt', 'wb') as usr_file:
                pickle.dump(exist_userinfo,usr_file)
            messagebox.showinfo('Sign up successfully')
            window_signup.destroy()


    window_signup=Toplevel(top)
    window_signup.geometry('500x300')
    window_signup.title('Sign up window')

    new_name=StringVar()
    Label(window_signup,text='Username:').place(x=10,y=10)
    entry_name=Entry(window_signup,textvariable=new_name)
    entry_name.place(x=150,y=10)

    new_pwd=StringVar()
    Label(window_signup, text='password:').place(x=10, y=50)
    entry_name = Entry(window_signup, textvariable=new_pwd,show='*')
    entry_name.place(x=150, y=50)

    new_pwd_confirm=StringVar()
    Label(window_signup, text='Confirm password:').place(x=10, y=90)
    entry_name = Entry(window_signup, textvariable=new_pwd_confirm,show='*')
    entry_name.place(x=150, y=90)

    btn_confirm_signup=Button(window_signup,text='Sign up',command=signup_to)
    btn_confirm_signup.place(x=150,y=130)

# login and sign up button
btn_login=Button(top,text='login',command=usr_login)
btn_login.place(x=170,y=130)

btn_signup=Button(top,text='sign up',command=usr_signup)
btn_signup.place(x=270,y=130)
mainloop()
