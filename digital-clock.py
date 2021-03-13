from tkinter import *
import datetime
import time
from datetime import date
today=date.today()
now=datetime.datetime.now()


root=Tk()
root.title("Digital Clock Created By Harendra Kumar")
root.geometry("1350x700+0+0")
root.config(bg="#081933")

lbl_date=Label(root,text="day",font=("times new roman",20,"bold"),bg="tomato",fg="white")
lbl_date.place(x=400,y=450,width=400,height=50)

lbl_day=Label(root,text="day",font=("times new roman",20,"bold"),bg="tomato",fg="white")
lbl_day.place(x=400,y=520,width=400,height=50)

lbl_name=Label(root,text="Created By HR",font=("times new roman",20,"bold"),bg="blue",fg="white")
lbl_name.place(x=400,y=100,width=400,height=50)



lbl_date.config(text=today)

lbl_day.config(text=now.strftime("%A"))

def clock():
    h=str(time.strftime("%H"))
    m=str(time.strftime("%M"))
    s=str(time.strftime("%S"))
    print(h,m,s)
    lbl_hr.config(text=h)
    lbl_min.config(text=m)
    lbl_sec.config(text=s)

    lbl_hr.after(200,clock)


    
lbl_hr=Label(root,text="12",font=("times new roman",50,"bold"),bg="#087587",fg="white")
lbl_hr.place(x=350,y=200,width=150,height=150)
lbl_hr2=Label(root,text="HOUR",font=("times new roman",20,"bold"),bg="#087587",fg="white")
lbl_hr2.place(x=350,y=360,width=150,height=50)

lbl_min=Label(root,text="12",font=("times new roman",50,"bold"),bg="#087587",fg="white")
lbl_min.place(x=540,y=200,width=150,height=150)
lbl_min2=Label(root,text="MINUTE",font=("times new roman",20,"bold"),bg="#087587",fg="white")
lbl_min2.place(x=540,y=360,width=150,height=50)

lbl_sec=Label(root,text="12",font=("times new roman",50,"bold"),bg="#087587",fg="white")
lbl_sec.place(x=710,y=200,width=150,height=150)
lbl_sec2=Label(root,text="SECOND",font=("times new roman",20,"bold"),bg="#087587",fg="white")
lbl_sec2.place(x=710,y=360,width=150,height=50)




clock()

root.mainloop()

