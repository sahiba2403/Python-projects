import tkinter as t
from tkinter import font

root=t.Tk()
root.title("calculator")
root.geometry("800x500")
root.configure(bg="light pink")

def calculate(event):
    text=event.widget.cget('text')
    if text== '=':
        try:
            result=str(eval(entry.get()))
            entry.set(result)

        except:
            entry.set('Error')
        return
    if text=='C':
        entry.set(' ')
        return

    entry.set(entry.get() + text)
    

entry=t.StringVar()
entry.set( '  ')
entry1=t.Entry(root,textvar=entry,font="arial",bd=4,insertwidth=3,bg="light blue")
entry1.pack(ipadx=20,padx=10,pady=30)

buttonframe=t.Frame(root)
buttonframe.pack()

buttonlist=[
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '.','0','=','+',
    '00','000','C'
    ]
i=0
for a in buttonlist:
    button=t.Button(buttonframe,text=a,font="arial",bg="skyblue",padx=10,pady=10,width=5)
    button.grid(row=int(i/4),column=i%4,padx=3,pady=3)
    i=i+1
    button.bind('<Button-1>',calculate)
    
root.mainloop()

    


