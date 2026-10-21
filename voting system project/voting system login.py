import tkinter as t
from tkinter import font
from tkinter import messagebox
import sqlite3
from sqlite3 import *
def submitbutton():
    adhaarno=adhaare.get()
    password=epass.get()
    db=sqlite3.connect("voting system.sql")
    curr=db.cursor()
    curr.execute("select  * from registration where adhaarno=(?) and password= (?)",(adhaarno,password))
    cursorr=curr.fetchall()
    count=1
    for x in cursorr:
        print(x)
        count=count+1
    if count==2:
        messagebox.showinfo("login success")
    else:
        messagebox.showinfo("login failed you are not registerd")
        
    
root=t.Tk()
root.title("login form")
root.configure(bg="brown")
root.geometry("800x500")

# define label
adhaarl=t.Label(root,text="adhaarno",font=18,fg="black")
adhaarl.grid(row=1,column=0,padx=10,pady=10)

passwordl=t.Label(root,text="password",font=18,fg="black")
passwordl.grid(row=2,column=0,padx=10,pady=10)

# definre entry box
adhaare=t.Entry(root,width=50,font=18,fg="black")
adhaare.grid(row=1,column=1,padx=10,pady=10)

epass=t.Entry(root,width=50,font=18,fg="black")
epass.grid(row=2,column=1,padx=10,pady=10)

#define button
submit=t.Button(root,text="login",font=18,fg="black",bg="pink",command=submitbutton)
submit.grid(row=4,column=1,padx=10,pady=10)
root.mainloop()
