from tkinter import *
import ali1
from tkinter import messagebox
win=Tk()
db1=ali1.database("C:/Users/PC42/Desktop/ali/myfile.db")
def delete():
    ent_name.delete(0,END)
    ent_lname.delete(0,END)
    ent_cname.delete(0,END)
    ent_oname.delete(0,END)
def signup():
    name=ent_name.get()
    lname=ent_lname.get()
    cname=ent_cname.get()
    kname=ent_oname.get()
    if cname==" "or kname=="":
        messagebox.showinfo("error")
    db1.insert_record(name,lname,cname,kname)
    delete()
def signin():
    record=db1.search_record(ent_cname.get(),ent_oname.get())
    if len(record)==0:
        messagebox.showinfo("erorr")
    else:
        messagebox.showinfo("yes")    




win.geometry("400x300")
lbl_name=Label(win,text="fname")
lbl_name.place(x=20,y=20)
ent_name=Entry(win)
ent_name.place(x=120,y=20)
lbl_lname=Label(win,text="lname")
lbl_lname.place(x=20,y=50)
ent_lname=Entry(win)
ent_lname.place(x=120,y=50)
lbl_cname=Label(win,text="email")
lbl_cname.place(x=20,y=80)
ent_cname=Entry(win)
ent_cname.place(x=120,y=80)
lbl_oname=Label(win,text="password")
lbl_oname.place(x=20,y=110)
ent_oname=Entry(win)
ent_oname.place(x=120,y=110)
btn_name=Button(win,text="sign up",command=signup)
btn_name.place(x=40,y=140)
btn_lname=Button(win,text="sign in",command=signin)
btn_lname.place(x=100,y=140)





win.mainloop()


