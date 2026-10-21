import tkinter as t
from tkinter import messagebox


def addtask():
    task=entry.get()
    if task:
        listbox.insert(t.END,task)
        entry.delete(0,t.END)
    else:
        messagebox.showwarning("Input error,please enter a task")

def deletetask():
    try:
        selected=listbox.curselection()
        listbox.delete(selected)
    except:
        messagebox.showwarning("selection error")
def clearall():
   if messagebox.askyesno("confirm are you sure"):
       listbox.delete(0,t.END)


       
root=t.Tk()
root.title("To do list")
root.geometry("900x800")

root.configure(bg="light grey")

l=t.Label(root,text="To do list",font=("arial",22,"bold"),bg="light blue")
l.pack(pady=10)
s=t.Label(root,text="One text at a time!",font=("arial",15))
s.pack(pady=20)

entry=t.Entry(root,font="arial")
entry.pack(pady=10,padx=20,fil=t.X)

btnframe=t.Frame(root,bg="light blue")
btnframe.pack(pady=5)

add=t.Button(btnframe,text="add task",font=("arial",14,"bold"),fg="green",width=12,command=addtask)
add.grid(row=0,column=0,padx=5)

delete=t.Button(btnframe,text="delete",font=("arial",14,"bold"),fg="red",width=12,command=deletetask)
delete.grid(row=0,column=1,padx=5)

clear=t.Button(btnframe,text="clear all",font=("arial",14,"bold"),fg="orange",width=12,command=clearall)
clear.grid(row=0,column=2,padx=5)

listbox=t.Listbox(root,width=40,height=20,font="arial",selectbackground="light blue")
listbox.pack(pady=10,padx=10,fill=t.X)
root.mainloop()


