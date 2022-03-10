from tkinter import *
from tkinter import ttk
window = Tk()
window.title("Welcome to MySite")
window.geometry('400x400')
window.configure(background = "grey");
a=Label(window,text="Full Name").grid(row=0,column=0)
b=Label(window,text="Age").grid(row=1,column=0)
c=Label(window,text="Contact number").grid(row=2,column=0)
d=Label(window,text="Email").grid(row=3,column=0)
a1=Entry(window).grid(row=0,column=1)
b1=Entry(window).grid(row=1,column=1)
c1=Entry(window).grid(row=2,column=1)
d1=Entry(window).grid(row=3,column=1)
def clicked():
    res="Welcome to"+txt.get()
    lbl.configure(text=res)

btn=ttk.Button(window,text="Submit").grid(row=5,column=1)
window.mainloop()
