from datetime import date
from tkinter import *
import time
import ttkthemes 
from tkinter import ttk
import mysql.connector
from tkinter import messagebox,filedialog
import pymysql
import pandas

#functionality part
def iexit():
    result=messagebox.askyesno('Confirm','Do you want to exit?')
    if result:
        root.destroy()
    else:
        pass
def exportstudent():
    url=filedialog.asksaveasfilename(defaultextension='.csv')
    indexing=stdnttable.get_children()
    newlist=[]
    for index in indexing:
        content=stdnttable.item(index)
        datalist=content['values']
        newlist.append(datalist)

    table=pandas.DataFrame(newlist,columns=['Id','Name','MobileNo','Email','Address','Gender','DOB','Addeddate','Addedtime'])
    table.to_csv(url,index=False)
    messagebox.showinfo('Success','Data is saved successfully')

def updatestudent():
    def update_data():
        try:
            query='update students set name=%s, MobileNo=%s, Email=%s, Address=%s, Gender=%s, DOB=%s, Addeddate=%s, Addedtime=%s where id=%s'
            mycursor.execute(query,(nameEntry.get(),mobilenoEntry.get(),emailEntry.get(),addressEntry.get(),genderEntry.get(),dobEntry.get(),date,currenttime,idEntry.get()))
            con.commit()
            messagebox.showinfo('Success',f'Id {idEntry.get()} is modified successfully',parent=update_window)
            showstudent()

        except Exception as e:
            messagebox.showerror('Error',str(e),parent=update_window)
            

    update_window=Toplevel()
    update_window.title('Update Student')
    update_window.grab_set()
    update_window.resizable(False,False)

    idLabel=Label(update_window,text='Id',font=('times new roman',15,'bold'))
    idLabel.grid(row=0,column=0,padx=30,pady=10,sticky=W)
    idEntry=Entry(update_window,font=('roman',15,'bold'))
    idEntry.grid(row=0,column=1,padx=20,pady=10)
            
    nameLabel=Label(update_window,text='Name',font=('times new roman',15,'bold'))
    nameLabel.grid(row=1,column=0,padx=30,pady=10,sticky=W)
    nameEntry=Entry(update_window,font=('roman',15,'bold'))
    nameEntry.grid(row=1,column=1,padx=20,pady=10)
    
    mobilenoLabel=Label(update_window,text='Mobile No',font=('times new roman',15,'bold'))
    mobilenoLabel.grid(row=2,column=0,padx=30,pady=10,sticky=W)
    mobilenoEntry=Entry(update_window,font=('roman',15,'bold'))
    mobilenoEntry.grid(row=2,column=1,padx=20,pady=10)
        
    emailLabel=Label(update_window,text='Email',font=('times new roman',15,'bold'))
    emailLabel.grid(row=3,column=0,padx=30,pady=10,sticky=W)
    emailEntry=Entry(update_window,font=('roman',15,'bold'))
    emailEntry.grid(row=3,column=1,padx=20,pady=10)
        
    addressLabel=Label(update_window,text='Address',font=('times new roman',15,'bold'))
    addressLabel.grid(row=4,column=0,padx=30,pady=10,sticky=W)
    addressEntry=Entry(update_window,font=('roman',15,'bold'))
    addressEntry.grid(row=4,column=1,padx=20,pady=10)
    
    genderLabel=Label(update_window,text='Gender',font=('times new roman',15,'bold'))
    genderLabel.grid(row=5,column=0,padx=30,pady=10,sticky=W)
    genderEntry=Entry(update_window,font=('roman',15,'bold'))
    genderEntry.grid(row=5,column=1,padx=20,pady=10)
        
    dobLabel=Label(update_window,text='DOB',font=('times new roman',15,'bold'))
    dobLabel.grid(row=6,column=0,padx=30,pady=10,sticky=W)
    dobEntry=Entry(update_window,font=('roman',15,'bold'))
    dobEntry.grid(row=6,column=1,padx=20,pady=10)
        
    updatestudentbutton=ttk.Button(update_window,text='Update',command=update_data)
    updatestudentbutton.grid(row=7,columnspan=2,pady=20)

    indexing=stdnttable.focus()
    print(indexing)
    content=stdnttable.item(indexing)
    listdata=content['values']
    idEntry.insert(0,listdata[0])
    nameEntry.insert(0,listdata[1])
    mobilenoEntry.insert(0,listdata[2])
    emailEntry.insert(0,listdata[3])
    addressEntry.insert(0,listdata[4])
    genderEntry.insert(0,listdata[5])
    dobEntry.insert(0,listdata[6])




def showstudent():
    query='select * from students'
    mycursor.execute(query)
    records=mycursor.fetchall()
    stdnttable.delete(*stdnttable.get_children())
    for data in records:
        stdnttable.insert('',END,values=data)


def deletestudent():
    indexing=stdnttable.focus()
    print(indexing)
    content=stdnttable.item(indexing)
    content_id=content['values'][0]
    query='delete from students where id=%s'
    mycursor.execute(query,(content_id))
    con.commit()
    messagebox.showinfo('Deleted',f'Id {content_id} is deleted successfully')
    query='select * from students'
    mycursor.execute(query)
    records=mycursor.fetchall()
    stdnttable.delete(*stdnttable.get_children())
    for data in records:
        datalist=list(data)
        stdnttable.insert('',END,values=datalist)


def searchstudent():
    def search_data():
        query='select * from students where id=%s or name=%s or MobileNo=%s or Email=%s or Address=%s or Gender=%s or DOB=%s'
        mycursor.execute(query,(idEntry.get(),nameEntry.get(),mobilenoEntry.get(),emailEntry.get(),addressEntry.get(),genderEntry.get(),dobEntry.get()))
        fetchdata=mycursor.fetchall()
        stdnttable.delete(*stdnttable.get_children())

        for data in fetchdata:
            datalist=list(data)
            stdnttable.insert('',END,values=data)

    search_window=Toplevel()
    search_window.title('Search Student')
    search_window.grab_set()
    search_window.resizable(False,False)
    
    idLabel=Label(search_window,text='Id',font=('times new roman',15,'bold'))
    idLabel.grid(row=0,column=0,padx=30,pady=10,sticky=W)
    idEntry=Entry(search_window,font=('roman',15,'bold'))
    idEntry.grid(row=0,column=1,padx=20,pady=10)
        
    nameLabel=Label(search_window,text='Name',font=('times new roman',15,'bold'))
    nameLabel.grid(row=1,column=0,padx=30,pady=10,sticky=W)
    nameEntry=Entry(search_window,font=('roman',15,'bold'))
    nameEntry.grid(row=1,column=1,padx=20,pady=10)

    mobilenoLabel=Label(search_window,text='Mobile No',font=('times new roman',15,'bold'))
    mobilenoLabel.grid(row=2,column=0,padx=30,pady=10,sticky=W)
    mobilenoEntry=Entry(search_window,font=('roman',15,'bold'))
    mobilenoEntry.grid(row=2,column=1,padx=20,pady=10)
    
    emailLabel=Label(search_window,text='Email',font=('times new roman',15,'bold'))
    emailLabel.grid(row=3,column=0,padx=30,pady=10,sticky=W)
    emailEntry=Entry(search_window,font=('roman',15,'bold'))
    emailEntry.grid(row=3,column=1,padx=20,pady=10)
    
    addressLabel=Label(search_window,text='Address',font=('times new roman',15,'bold'))
    addressLabel.grid(row=4,column=0,padx=30,pady=10,sticky=W)
    addressEntry=Entry(search_window,font=('roman',15,'bold'))
    addressEntry.grid(row=4,column=1,padx=20,pady=10)

    genderLabel=Label(search_window,text='Gender',font=('times new roman',15,'bold'))
    genderLabel.grid(row=5,column=0,padx=30,pady=10,sticky=W)
    genderEntry=Entry(search_window,font=('roman',15,'bold'))
    genderEntry.grid(row=5,column=1,padx=20,pady=10)
    
    dobLabel=Label(search_window,text='DOB',font=('times new roman',15,'bold'))
    dobLabel.grid(row=6,column=0,padx=30,pady=10,sticky=W)
    dobEntry=Entry(search_window,font=('roman',15,'bold'))
    dobEntry.grid(row=6,column=1,padx=20,pady=10)
    
    searchstudentbutton=ttk.Button(search_window,text='Search',command=search_data)
    searchstudentbutton.grid(row=7,columnspan=2,pady=20)


def addstudent():
    def add_data():
        if idEntry.get()=='' or nameEntry.get()=='' or mobilenoEntry.get()=='' or emailEntry.get()=='' or addressEntry.get()=='' or genderEntry.get()=='' or dobEntry.get()=='':
            messagebox.showerror('Error','All fields are required',parent=add_window)

        else:
             date=time.strftime('%d/%m/%y')
             currenttime=time.strftime('%H:%M:%S')
        try:
            query='insert into students values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(query,(idEntry.get(),nameEntry.get(),mobilenoEntry.get(),emailEntry.get(),addressEntry.get(),genderEntry.get(),dobEntry.get(),date,currenttime))
            con.commit()
            result=messagebox.askyesno('Confirm','Data added successfully. Do you want to clean the form?',parent=add_window)
            if result:
                idEntry.delete(0,END)
                nameEntry.delete(0,END)
                mobilenoEntry.delete(0,END)
                emailEntry.delete(0,END)
                addressEntry.delete(0,END)
                genderEntry.delete(0,END)
                dobEntry.delete(0,END)
            else:
                pass
        except:
            messagebox.showerror('Error','Id cannot be repeated',parent=add_window)
            return
            

        query='select * from students'
        mycursor.execute(query)
        records=mycursor.fetchall()
        stdnttable.delete(*stdnttable.get_children())
        for data in records:
                datalist=list(data)
                stdnttable.insert('',END,values=datalist)

    add_window=Toplevel()
    add_window.grab_set()
    add_window.resizable(False,False)

    idLabel=Label(add_window,text='Id',font=('times new roman',15,'bold'))
    idLabel.grid(row=0,column=0,padx=30,pady=10,sticky=W)
    idEntry=Entry(add_window,font=('roman',15,'bold'))
    idEntry.grid(row=0,column=1,padx=20,pady=10)

    nameLabel=Label(add_window,text='Name',font=('times new roman',15,'bold'))
    nameLabel.grid(row=1,column=0,padx=30,pady=10,sticky=W)
    nameEntry=Entry(add_window,font=('roman',15,'bold'))
    nameEntry.grid(row=1,column=1,padx=20,pady=10)

    mobilenoLabel=Label(add_window,text='Mobile No',font=('times new roman',15,'bold'))
    mobilenoLabel.grid(row=2,column=0,padx=30,pady=10,sticky=W)
    mobilenoEntry=Entry(add_window,font=('roman',15,'bold'))
    mobilenoEntry.grid(row=2,column=1,padx=20,pady=10)

    emailLabel=Label(add_window,text='Email',font=('times new roman',15,'bold'))
    emailLabel.grid(row=3,column=0,padx=30,pady=10,sticky=W)
    emailEntry=Entry(add_window,font=('roman',15,'bold'))
    emailEntry.grid(row=3,column=1,padx=20,pady=10)

    addressLabel=Label(add_window,text='Address',font=('times new roman',15,'bold'))
    addressLabel.grid(row=4,column=0,padx=30,pady=10,sticky=W)
    addressEntry=Entry(add_window,font=('roman',15,'bold'))
    addressEntry.grid(row=4,column=1,padx=20,pady=10)

    genderLabel=Label(add_window,text='Gender',font=('times new roman',15,'bold'))
    genderLabel.grid(row=5,column=0,padx=30,pady=10,sticky=W)
    genderEntry=Entry(add_window,font=('roman',15,'bold'))
    genderEntry.grid(row=5,column=1,padx=20,pady=10)

    dobLabel=Label(add_window,text='DOB',font=('times new roman',15,'bold'))
    dobLabel.grid(row=6,column=0,padx=30,pady=10,sticky=W)
    dobEntry=Entry(add_window,font=('roman',15,'bold'))
    dobEntry.grid(row=6,column=1,padx=20,pady=10)

    addstudentbutton=ttk.Button(add_window,text='Add Student',command=add_data)
    addstudentbutton.grid(row=7,columnspan=2,pady=20)

def connect():
    global mycursor,con
    try:
        con = pymysql.connect(
            host=hostEntry.get(),
            user=usernameEntry.get(),
            password=passwordEntry.get(),
            database='vishali'
        )
        mycursor=con.cursor()

        connectwindow.destroy()

    except Exception as e:
        messagebox.showerror(
            'Error',
            str(e)
        )
        return
    try:
        query='create database studentmanagementsystem'
        mycursor = con.cursor()
        mycursor.execute(query)
        query='use studentmanagementsystem'
        mycursor = con.cursor()
        mycursor.execute(query)
        query='create table students(id int primary key, name varchar(30), MobileNo VARCHAR(30), Email VARCHAR(40), Address VARCHAR(100), Gender VARCHAR(40), DOB VARCHAR(40),Addeddate VARCHAR(40), Addedtime VARCHAR(40))'
        mycursor = con.cursor()
        mycursor.execute(query)

    except:
          query='use studentmanagementsystem'
          mycursor.execute(query)
    messagebox.showinfo(
                      'Success',
                      'Database Connected Successfully',parent=connectwindow
                  )
    addstdntbutton.config(state=NORMAL)
    searchstdntbutton.config(state=NORMAL)
    updatestdntbutton.config(state=NORMAL)
    showstdntbutton.config(state=NORMAL)
    exportstdntbutton.config(state=NORMAL)
    deletestdntbutton.config(state=NORMAL)

def connect_database():

    global connectwindow
    global hostEntry
    global usernameEntry
    global passwordEntry

    connectwindow=Toplevel()
    connectwindow.geometry('470x250+730+230')
    connectwindow.title('Database Connection')
    connectwindow.resizable(0,0)

    hostnameLabel=Label(connectwindow,text='Host Name',font=('arial',15,'bold'))
    hostnameLabel.grid(row=0,column=0,padx=20)
    
    hostEntry=Entry(connectwindow,text='Host Enrty',font=('arial',15,'bold'),bd=2)
    hostEntry.grid(row=0,column=1,padx=30,pady=15)

    
    usernameLabel=Label(connectwindow,text='User Name',font=('arial',15,'bold'))
    usernameLabel.grid(row=1,column=0,padx=20)
    
    usernameEntry=Entry(connectwindow,text='Username Enrty',font=('arial',15,'bold'),bd=2)
    usernameEntry.grid(row=1,column=1,padx=30,pady=15)
    
    passwordLabel=Label(connectwindow,text='Password',font=('arial',15,'bold'))
    passwordLabel.grid(row=2,column=0,padx=20)
        
    passwordEntry=Entry(connectwindow,text='Password Entry',font=('arial',15,'bold'),bd=2, show='*')
    passwordEntry.grid(row=2,column=1,padx=30,pady=15)

    connectButton=ttk.Button(connectwindow,text='CONNECT', command=connect)
    connectButton.grid(row=3,columnspan=2,pady=20)


count=0
text=''
def slider():
    global text,count 
    if count==len(s):
        count=0
        text=''
    text=text+s[count]
    sliderlabel.config(text=text)
    count+=1
    sliderlabel.after(300,slider)





def clock():
    global date,currenttime
    date=time.strftime('%d/%m/%y')
    currenttime=time.strftime('%H:%M:%S')
    dtlabel.config(text=f'Date: {date}\nTime:{currenttime}')
    dtlabel.after(1000,clock)

#GUI Part
root=ttkthemes.ThemedTk()

root.get_themes()

root.set_theme('radiance')

root.geometry('1174x680')
root.resizable(0,0)
root.title('Student Management System')

dtlabel=Label(root,text='hello',font=('times new roman',18,'bold'))
dtlabel.place(x=5,y=5)
clock()

s='Student Management System'
sliderlabel=Label(root,font=('arial',28,'italic bold'),width=30)
sliderlabel.place(x=200,y=0)
slider()


button=ttk.Button(root,text='Connect database',command=connect_database)
button.place(x=900,y=0)


leftframe=Frame(root)
leftframe.place(x=50,y=80,width=300,height=600)

logo_image=PhotoImage(file='student.png')
logo_label=Label(leftframe,image=logo_image,bg='red')
logo_label.grid(row=0,column=0,pady=10)


addstdntbutton=ttk.Button(leftframe,text='Add Student',width=20,command=addstudent)
addstdntbutton.grid(row=1,column=0,pady=10)

searchstdntbutton=ttk.Button(leftframe,text='Search Student',width=20,command=searchstudent)
searchstdntbutton.grid(row=2,column=0,pady=10)

deletestdntbutton=ttk.Button(leftframe,text='Delete Student',width=20,command=deletestudent)
deletestdntbutton.grid(row=3,column=0,pady=10)

updatestdntbutton=ttk.Button(leftframe,text='Update Student',width=20,command=updatestudent)
updatestdntbutton.grid(row=4,column=0,pady=10)

showstdntbutton=ttk.Button(leftframe,text='Show Student',width=20,command=showstudent)
showstdntbutton.grid(row=5,column=0,pady=10)

exportstdntbutton=ttk.Button(leftframe,text='Export Student',width=20,command=exportstudent)
exportstdntbutton.grid(row=6,column=0,pady=10)

exitbutton=ttk.Button(leftframe,text='Exit',width=20,command=iexit)
exitbutton.grid(row=7,column=0,pady=10)



rightframe=Frame(root)
rightframe.place(x=350,y=80,width=820,height=600)

ScrollBarX=Scrollbar(rightframe,orient=HORIZONTAL)
ScrollBarY=Scrollbar(rightframe,orient=VERTICAL)

stdnttable=ttk.Treeview(rightframe,columns=('Id','Name','MobileNo','Email','Address','Gender','DOB'
                                            ,'Added date','Added time'),
                                            xscrollcommand=ScrollBarX.set,yscrollcommand=ScrollBarY.set)

ScrollBarX.config(command=stdnttable.xview)
ScrollBarY.config(command=stdnttable.yview)

ScrollBarX.pack(side=BOTTOM,fill=X)
ScrollBarY.pack(side=RIGHT,fill=Y)
stdnttable.pack(fill=BOTH,expand=1)


stdnttable.heading('Id',text='Id')
stdnttable.heading('Name',text='Name')
stdnttable.heading('MobileNo',text='MobileNo')
stdnttable.heading('Email',text='Email')
stdnttable.heading('Address',text='Address')
stdnttable.heading('Gender',text='Gender')
stdnttable.heading('DOB',text='DOB')
stdnttable.heading('Added date',text='Added date')
stdnttable.heading('Added time',text='Added time')

stdnttable.column('Id',width=50,anchor=CENTER)
stdnttable.column('Name',width=400,anchor=CENTER)
stdnttable.column('Email',width=300,anchor=CENTER)
stdnttable.column('MobileNo',width=290,anchor=CENTER)
stdnttable.column('Address',width=400,anchor=CENTER)
stdnttable.column('Gender',width=200,anchor=CENTER)
stdnttable.column('DOB',width=300,anchor=CENTER)
stdnttable.column('Added date',width=200,anchor=CENTER)
stdnttable.column('Added time',width=200,anchor=CENTER)

style=ttk.Style()
style.configure('Treeview',rowheight=40,font=('arial',15,'bold'))


stdnttable.config(show='headings')




root.mainloop()    