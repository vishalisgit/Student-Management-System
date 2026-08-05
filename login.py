from tkinter import *
from tkinter import messagebox
from PIL import ImageTk 

def login():
    if usernameEntry.get()==''or passwordEntry.get()=='':
        messagebox.showerror('Error','Fields cannot be empty')
    elif usernameEntry.get()=='Vishali' and passwordEntry.get()=='1234':
        messagebox.showinfo('Success','Login Successful')
        window.destroy()
        import sms
        
    else:
        messagebox.showerror('Error','Please enter correct credentials')

window=Tk()
window.title('Login_Page of Student Management System')

window.geometry('1280x800')

#window.resizable(False,False)#to disable the minimize button

bgImage=ImageTk.PhotoImage(file='bg.jpg')

bglabel=Label(window,image=bgImage)
bglabel.place(x=0,y=0)


loginframe=Frame(window,bg = "#CFDBDC")
loginframe.place(x=400,y=200)

logoImage=PhotoImage(file='logo.png')
logolabel=Label(loginframe,image=logoImage)
logolabel.grid(row=0,column=0,columnspan=4,pady=10)

usernameImage=PhotoImage(file='username.png')
usernamelabel=Label(loginframe,image=usernameImage,text='Username',compound=LEFT,font=('times new roman',20,'bold'),bg = "#CFDBDC")
usernamelabel.grid(row=1,column=0,pady=10,padx=20)

usernameEntry=Entry(loginframe,font=('times new roman',20,'bold'),bd=5)
usernameEntry.grid(row=1,column=1,pady=10,padx=20)


passwordImage=PhotoImage(file='password.png')
passwordlabel=Label(loginframe,image=passwordImage,text='Password',compound=LEFT,font=('times new roman',20,'bold'),bg = "#CFDBDC")
passwordlabel.grid(row=2,column=0,pady=10,padx=20)

passwordEntry=Entry(loginframe,font=('times new roman',20,'bold'),bd=5,show='*')
passwordEntry.grid(row=2,column=1,pady=10,padx=20)


loginbutton=Button(loginframe,text='Login',font=('times new roman',15,'bold'),width=15,bg='#1589FF'
                   ,fg='white',activebackground='#1589FF',cursor='hand2',command=login)
loginbutton.grid(row=3,column=0,columnspan=2,pady=10)

window.mainloop()