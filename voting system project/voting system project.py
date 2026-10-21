import tkinter as t
from tkinter import font
from tkinter import messagebox
import sqlite3
from sqlite3 import *
def submitbutton():
    name=ename.get()
    fname=efname.get()
    adhaarno=eadhaarno.get()
    age=eage.get()
    city=ecity.get()
    password=epass.get()
    mobileno=emobno.get()
    db=sqlite3.connect("final voting.db")
    print('database created')
    curr=db.cursor()
    curr.execute(" CREATE TABLE IF NOT EXISTS registration(name text,fname text,adhaarno integer primarykey,age integer, city Text ,password Text, mobileno integer)")
    print("table created")
    curr.execute("Insert into registration(name,fname,adhaarno,age,city,password,mobileno) values (?,?,?,?,?,?,?) ",(name,fname,adhaarno,age,city,password,mobileno))
    db.commit()
    cursor=curr.execute ("select * from registration")
    for i in cursor.fetchall():
        print(i)
    
    db.close()
    
root=t.Tk()
root.title("Registration login form")
root.geometry("800x600")
root.configure(bg="brown")

#define label
ltitle=t.Label(root,text="voter registration form",font=58,fg="black")
ltitle.grid(row=0,column=1,padx=200,pady=10)

lname=t.Label(root,text="name",font=18,fg="black")
lname.grid(row=1,column=0,padx=50,pady=20)

lfname=t.Label(root,text="father name",font=18,fg="black")
lfname.grid(row=2,column=0,padx=10,pady=10)

ladhaarno=t.Label(root,text="adhaarno",font=18,fg="black")
ladhaarno.grid(row=3,column=0,padx=10,pady=10)

lage=t.Label(root,text="age",font=18,fg="black")
lage.grid(row=4,column=0,padx=50,pady=10)

lcity=t.Label(root,text='city',font=18,fg="black")
lcity.grid(row=5,column=0,padx=10,pady=10)

lpass=t.Label(root,text="password",font=18,fg="black")
lpass.grid(row=6,column=0,padx=10,pady=10)

lmobno=t.Label(root,text="mobileno",font=18,fg="black")
lmobno.grid(row=7,column=0,padx=10,pady=10)

lpincode=t.Label(root,text="pincode",font=18,fg="black")
lpincode.grid(row=8,column=0,padx=10,pady=10)

#define entry box
ename=t.Entry(root,width=50,font=18,fg="black")
ename.grid(row=1,column=1,padx=0,pady=0)

efname=t.Entry(root,width=50,font=18,fg="black")
efname.grid(row=2,column=1,padx=0,pady=0)

eadhaarno=t.Entry(root,width=50,font=18,fg="black")
eadhaarno.grid(row=3,column=1,padx=2,pady=10)

eage=t.Entry(root,width=30,font=18,fg='black')
eage.grid(row=4,column=1,padx=2,pady=10)

ecity=t.Entry(root,width=30,font=18,fg="black")
ecity.grid(row=5,column=1,padx=10,pady=10)

epass=t.Entry(root,width=50,font=18,fg="black")
epass.grid(row=6,column=1,padx=10,pady=10)

emobno=t.Entry(root,width=50,font=18,fg="black")
emobno.grid(row=7,column=1,padx=10,pady=10)

epincode=t.Entry(root,width=30,font=18,fg="black")
epincode.grid(row=8,column=1,padx=10,pady=10)

#button
submit=t.Button(root,text="signup",font=18,fg="black",bg="pink",command=submitbutton )
submit.grid(row=12,column=1,padx=10,pady=10)
root.mainloop()



