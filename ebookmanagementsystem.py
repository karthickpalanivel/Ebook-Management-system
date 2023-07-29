from tkinter import*
from tkinter import ttk
import tkinter as tk
import mysql.connector
from tkinter import messagebox
import datetime
import tkinter 



class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("LibraryManagementSystem")
        self.root.geometry("1200x900+0+0")

       #-----------------------------------Variable-------------------------------------------------------#
        self.Member_var=StringVar()
        self.ID_number_var=StringVar()
        self.Department_var=StringVar()
        self.Year_var=StringVar()
        self.Name_var=StringVar()
        self.Mobile_no_var=StringVar()
        self.Book_ID_var=StringVar()
        self.Book_Name_var=StringVar()
        self.Date_Borrowed_var=StringVar()
        self.Due_Date_var=StringVar()
        self.Late_Return_var=StringVar()
        self.Date_Over_Due_var=StringVar()
        self.ActualPrice_var=StringVar()
        

        def idata():
         conn=mysql.connector.connect(host="localhost",username="root",password="mysql",database="librarymanagementsystem")
         my_cursor=conn.cursor()
         my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
        (
                       self.Member_var.get(),
                       self.ID_number_var.get(),
                       self.Department_var.get(),
                       self.Year_var.get(),
                       self.Name_var.get(),
                       self.Mobile_no_var.get(),
                       self.Book_ID_var.get(),
                       self.Book_Name_var.get(),
                       self.Date_Borrowed_var.get(),
                       self.Due_Date_var.get(),
                       self.Late_Return_var.get(),
                       self.Date_Over_Due_var.get(),
                       self.ActualPrice_var.get()
        ))
         conn.commit()
         self.fatch_data()
         conn.close()   
         messagebox.showinfo("Success","Member has be inserted sucessfully")          

        
       #------------------------------------------------ creating a lable ------------------------------------------------------------------#


        lbltitle=Label(self.root,text="E-book Management System",bg="powder blue",fg="black",bd=15,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6) 
        lbltitle.pack(side=TOP,fill=X)
  
       #-------------------------------------------------- creating a frame -----------------------------------------------------------------#


        frame=Frame(self.root,bd=12,relief=RIDGE,padx=15,bg="powder blue")
        frame.place(x=0,y=120,width=1370,height=400)  


       #------------------------------------------- creating frames inside a frame ----------------------------------------------------------#


      #-------------------------------------------  DataFrameLeft ---------------------------------------------------------------------------#
        DataFrameLeft=LabelFrame(frame,text="E-book member",bg="powder blue",fg="black",bd=10,relief=RIDGE,font=("times new roman",15,"bold"))
        DataFrameLeft.place(x=0,y=5,width=800,height=350)

        lblMember=Label(DataFrameLeft,bg="powder blue",text="Member Type",font=("times new roman",15,"bold"),padx=2,pady=6) 
        lblMember.grid(row=0,column=0,sticky=W)    

        comMember=ttk.Combobox(font=("times new roman",15,"bold"),textvariable=self.Member_var,width=20,state="readonly")
        comMember["value"]=("Admin","Student","Teacher")
        comMember.pack(padx=180,pady=50,anchor=SW)

        lblID_number=Label(DataFrameLeft,bg="powder blue" ,text="ID_number",font=("times new roman",13,"bold")) 
        lblID_number.grid(row=1,column=0,sticky=W) 

        txtID=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.ID_number_var,width=20)
        txtID.grid(row=1,column=1,padx=15)

        lblDepartment=Label(DataFrameLeft,bg="powder blue" ,text="Department",font=("times new roman",13,"bold")) 
        lblDepartment.grid(row=2,column=0,sticky=W) 

        txtDepartment=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.Department_var,width=20)
        txtDepartment.grid(row=2,column=1,padx=16,pady=5)
        

        lblYEAR=Label(DataFrameLeft,bg="powder blue" ,text="YEAR",font=("times new roman",13,"bold")) 
        lblYEAR.grid(row=3,column=0,sticky=W) 

        comYEAR=ttk.Combobox(font=("times new roman",15,"bold"),textvariable=self.Year_var,width=20,state="readonly")
        comYEAR["value"]=("Staff","I","II","III","IV")
        comYEAR.pack(padx=180,pady=20,anchor=SW)

        lblName=Label(DataFrameLeft,bg="powder blue" ,text="Name",font=("times new roman",13,"bold"))
        lblName.grid(row=4,column=0,sticky=W)

        txtName=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.Name_var,width=20)
        txtName.grid(row=4,column=1,padx=16,pady=9)
        
        lblMobile_no=Label(DataFrameLeft,bg="powder blue" ,text="Mobile_no",font=("times new roman",13,"bold"))
        lblMobile_no.grid(row=5,column=0,sticky=W)

        txtMobile_no=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.Mobile_no_var,width=20)
        txtMobile_no.grid(row=5,column=1,padx=20,pady=2)

        lblBook_Id=Label(DataFrameLeft,bg="powder blue" ,text="Book_Id",font=("times new roman",13,"bold"))
        lblBook_Id.grid(row=6,column=0,sticky=W)

        txtBook_Id=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.Book_ID_var,width=20)
        txtBook_Id.grid(row=6,column=1,padx=20,pady=2)
  
        lblBook_Name=Label(DataFrameLeft,bg="powder blue" ,text="Book_Name",font=("times new roman",13,"bold"))
        lblBook_Name.grid(row=7,column=0,sticky=W)

        txtBook_Name=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.Book_Name_var,width=20)
        txtBook_Name.grid(row=7,column=1,padx=20,pady=2)

        lblDateBorrowed=Label(DataFrameLeft,bg="powder blue" ,text="Date_Borrowed",font=("times new roman",13,"bold"))
        lblDateBorrowed.grid(row=8,column=0,sticky=W)
         
        txtDateBorrowed=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.Date_Borrowed_var,width=20)
        txtDateBorrowed.grid(row=8,column=1,padx=20,pady=2) 

        lblDateDue=Label(DataFrameLeft,bg="powder blue" ,text="Date_Due",font=("times new roman",13,"bold"))
        lblDateDue.grid(row=0,column=2,sticky=W)

        txtDateDue=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.Due_Date_var,width=20)
        txtDateDue.grid(row=0,column=2,padx=190,pady=2) 

        lblLate_Return_fine=Label(DataFrameLeft,bg="powder blue" ,text="Late_Return_fine",font=("times new roman",13,"bold"))
        lblLate_Return_fine.grid(row=1,column=2,sticky=W)
          
        txtLate_Return_fine=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.Late_Return_var,width=20)
        txtLate_Return_fine.grid(row=1,column=2,padx=190,pady=2) 
        
        lblDateOverDue=Label(DataFrameLeft,bg="powder blue" ,text="Date_Over_Due",font=("times new roman",13,"bold"))
        lblDateOverDue.grid(row=2,column=2,sticky=W)

        txtDateOverDue=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.Date_Over_Due_var,width=20)
        txtDateOverDue.grid(row=2,column=2,padx=90,pady=2) 
        
        lblActualPrice=Label(DataFrameLeft,bg="powder blue" ,text="ActualPrice",font=("times new roman",13,"bold"))
        lblActualPrice.grid(row=3,column=2,sticky=W)

        txtActualPrice=Entry(DataFrameLeft,font=("times new roman",15,"bold"),textvariable=self.ActualPrice_var,width=20)
        txtActualPrice.grid(row=3,column=2,padx=90,pady=2) 



      #-------------------------------------------  DataFrameRight --------------------------------------------------------------------------#
        DataFrameRight=LabelFrame(frame,text="BOOKS",bg="powder blue",fg="black",bd=10,relief=RIDGE,font=("times new roman",15,"bold"))
        DataFrameRight.place(x=810,y=5,width=500,height=350)

        self.textbox=Text(DataFrameRight,font=("times new roman",15,"bold"),width=23,height=13,padx=5,pady=2)
        self.textbox.grid(row=0,column=2)
        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")
      # ------------------------------------------------list box-------------------------------------------------------------------------------#
        Listbook=("clean code","Data Structure & Algorithm Classes","Big Data","Design thinking","Core programming",
                                                   "Full Stack Development","Complete Data Science Program Trending.",
                                                   "coding with c", "c++ programming","python tkinter",
                                                   "softwer design with uml","programming with c","R programming","SQL database")
        def SelectBook(event=""):
          value=str(listBox.get(listBox.curselection()))
          x=value
          if (x=="clean code"):
            self.Book_ID_var.set("BKID5454")
            self.Book_Name_var.set("clean code")

            d1=datetime.datetime.today()
            d2=datetime.timedelta(days=15)
            d3=d1+d2
            self.Date_Borrowed_var.set(d1)
            self.Due_Date_var.set(d3)
            self.Late_Return_var.set("Rs.50")
            self.Date_Over_Due_var.set("No")
            self.ActualPrice_var.set("Rs.512")

          elif (x=="Data Structure & Algorithm Classes"):
            self.Book_ID_var.set("BKID5485")
            self.Book_Name_var.set("Data Structure & Algorithm")

            d1=datetime.datetime.today()
            d2=datetime.timedelta(days=15)
            d3=d1+d2
            self.Date_Borrowed_var.set(d1)
            self.Due_Date_var.set(d3)
            self.Late_Return_var.set("Rs.50")
            self.Date_Over_Due_var.set("No")
            self.ActualPrice_var.set("Rs.790")

          elif (x=="Big Data"):
            self.Book_ID_var.set("BKID5490")
            self.Book_Name_var.set("Big Data")

            d1=datetime.datetime.today()
            d2=datetime.timedelta(days=15)
            d3=d1+d2
            self.Date_Borrowed_var.set(d1)
            self.Due_Date_var.set(d3)
            self.Late_Return_var.set("Rs.50")
            self.Date_Over_Due_var.set("No")
            self.ActualPrice_var.set("Rs.800")

          elif (x=="Design thinking"):
            self.Book_ID_var.set("BKID5824")
            self.Book_Name_var.set("Design thinking")

            d1=datetime.datetime.today()
            d2=datetime.timedelta(days=15)
            d3=d1+d2
            self.Date_Borrowed_var.set(d1)
            self.Due_Date_var.set(d3)
            self.Late_Return_var.set("Rs.50")
            self.Date_Over_Due_var.set("No")
            self.ActualPrice_var.set("Rs.400")

          elif (x=="Core programming"):
            self.Book_ID_var.set("BKID5047")
            self.Book_Name_var.set("Core programming")

            d1=datetime.datetime.today()
            d2=datetime.timedelta(days=15)
            d3=d1+d2
            self.Date_Borrowed_var.set(d1)
            self.Due_Date_var.set(d3)
            self.Late_Return_var.set("Rs.50")
            self.Date_Over_Due_var.set("No")
            self.ActualPrice_var.set("Rs.700")

          elif (x=="Full Stack Development"):
            self.Book_ID_var.set("BKID6454")
            self.Book_Name_var.set("Full Stack Development")

            d1=datetime.datetime.today()
            d2=datetime.timedelta(days=15)
            d3=d1+d2
            self.Date_Borrowed_var.set(d1)
            self.Due_Date_var.set(d3)
            self.Late_Return_var.set("Rs.50")
            self.Date_Over_Due_var.set("No")
            self.ActualPrice_var.set("Rs.900")

          elif (x=="Complete Data Science Program Trending."):
            self.Book_ID_var.set("BKID4454")
            self.Book_Name_var.set("Data Science Programing")

            d1=datetime.datetime.today()
            d2=datetime.timedelta(days=15)
            d3=d1+d2
            self.Date_Borrowed_var.set(d1)
            self.Due_Date_var.set(d3)
            self.Late_Return_var.set("Rs.50")
            self.Date_Over_Due_var.set("No")
            self.ActualPrice_var.set("Rs.900")

          elif (x=="coding with c"):
            self.Book_ID_var.set("BKID5325")
            self.Book_Name_var.set("coding with c")

            d1=datetime.datetime.today()
            d2=datetime.timedelta(days=15)
            d3=d1+d2
            self.Date_Borrowed_var.set(d1)
            self.Due_Date_var.set(d3)
            self.Late_Return_var.set("Rs.50")
            self.Date_Over_Due_var.set("No")
            self.ActualPrice_var.set("Rs.612")

          elif (x=="c++ programing"):
            self.Book_ID_var.set("BKID5454")
            self.Book_Name_var.set("c++ programming")

            d1=datetime.datetime.today()
            d2=datetime.timedelta(days=15)
            d3=d1+d2
            self.Date_Borrowed_var.set(d1)
            self.Due_Date_var.set(d3)
            self.Late_Return_var.set("Rs.50")
            self.Date_Over_Due_var.set("No")
            self.ActualPrice_var.set("Rs.758")

          elif (x=="python tkinter"):
            self.Book_ID_var.set("BKID2454")
            self.Book_Name_var.set("python tkinter")

            d1=datetime.datetime.today()
            d2=datetime.timedelta(days=15)
            d3=d1+d2
            self.Date_Borrowed_var.set(d1)
            self.Due_Date_var.set(d3)
            self.Late_Return_var.set("Rs.50")
            self.Date_Over_Due_var.set("No")
            self.ActualPrice_var.set("Rs.912")

          elif (x=="softwer design with uml"):
            self.Book_ID_var.set("BKID5698")
            self.Book_Name_var.set("softwer design with uml")

            d1=datetime.datetime.today()
            d2=datetime.timedelta(days=15)
            d3=d1+d2
            self.Date_Borrowed_var.set(d1)
            self.Due_Date_var.set(d3)
            self.Late_Return_var.set("Rs.50")
            self.Date_Over_Due_var.set("No")
            self.ActualPrice_var.set("Rs.812")

          elif (x=="programming with c"):
            self.Book_ID_var.set("BKID8454")
            self.Book_Name_var.set("programming with c")

            d1=datetime.datetime.today()
            d2=datetime.timedelta(days=15)
            d3=d1+d2
            self.Date_Borrowed_var.set(d1)
            self.Due_Date_var.set(d3)
            self.Late_Return_var.set("Rs.50")
            self.Date_Over_Due_var.set("No")
            self.ActualPrice_var.set("Rs.712")

          elif (x=="R programming"):
            self.Book_ID_var.set("BKID7454")
            self.Book_Name_var.set("R programming")

            d1=datetime.datetime.today()
            d2=datetime.timedelta(days=15)
            d3=d1+d2
            self.Date_Borrowed_var.set(d1)
            self.Due_Date_var.set(d3)
            self.Late_Return_var.set("Rs.50")
            self.Date_Over_Due_var.set("No")
            self.ActualPrice_var.set("Rs.1012")  

          elif (x=="SQL database"):
            self.Book_ID_var.set("BKID7454")
            self.Book_Name_var.set("SQL database")

            d1=datetime.datetime.today()
            d2=datetime.timedelta(days=15)
            d3=d1+d2
            self.Date_Borrowed_var.set(d1)
            self.Due_Date_var.set(d3)
            self.Late_Return_var.set("Rs.50")
            self.Date_Over_Due_var.set("No")
            self.ActualPrice_var.set("Rs.712")

          elif (x=="c++ programming"):
            self.Book_ID_var.set("BKID7400")
            self.Book_Name_var.set("c++ programming")

            d1=datetime.datetime.today()
            d2=datetime.timedelta(days=15)
            d3=d1+d2
            self.Date_Borrowed_var.set(d1)
            self.Due_Date_var.set(d3)
            self.Late_Return_var.set("Rs.50")
            self.Date_Over_Due_var.set("No")
            self.ActualPrice_var.set("Rs.912")  
            
            
          
   




        listBox=Listbox(DataFrameRight,font=("times new roman",15,"bold"),width=20,height=13)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in Listbook:
          listBox.insert(END,item)

       #-------------------------------------------- Button frame ------------------------------------------------------------------------ #

        framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        framebutton.place(x=0,y=500,width=1370,height=70) 
         
        btnAddData=Button(framebutton,command=idata,text="add_data",font=("times new roman",15,"bold"),width=15,bg="blue",fg="white")
        btnAddData.grid(row=0,column=0)

        btnShowData=Button(framebutton,command=self.showdata,text="Show Data",font=("times new roman",15,"bold"),width=15,bg="blue",fg="white")
        btnShowData.grid(row=0,column=2)
        
        btnUpdate=Button(framebutton,command=self.update,text="Update",font=("times new roman",15,"bold"),width=15,bg="blue",fg="white")
        btnUpdate.grid(row=0,column=3)

        btnDelete=Button(framebutton,command=self.delete,text="Delete",font=("times new roman",15,"bold"),width=15,bg="blue",fg="white")
        btnDelete.grid(row=0,column=4)
        
        btnReset=Button(framebutton,command=self.reset,text="Reset",font=("times new roman",15,"bold"),width=15,bg="blue",fg="white")
        btnReset.grid(row=0,column=5)

        btnExit=Button(framebutton,command=self.iExit,text="Exit",font=("times new roman",15,"bold"),width=20,bg="blue",fg="white")
        btnExit.grid(row=0,column=6)

       #-------------------------------------------- Information frame ------------------------------------------------------------------- #

        Framedetail=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        Framedetail.place(x=0,y=560,width=1370,height=150)  

        Table_frame=Frame(Framedetail,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1320,height=130)  

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)  
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)


        self.library_table=ttk.Treeview(Table_frame,column=("membertype","idnumber","department","year","name","mobileno","bookid", 
                                                          "bookname","dateborrowed","datedue","latereturn","dateoverdue","actualprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)   
        yscroll.config(command=self.library_table.yview)                                        

        self.library_table.heading("membertype",text="Member type")
        self.library_table.heading("idnumber",text="ID_number")
        self.library_table.heading("department",text="Department")
        self.library_table.heading("year",text="Year")
        self.library_table.heading("name",text="Name")
        self.library_table.heading("mobileno",text="Mobile_no")
        self.library_table.heading("bookid",text="Book_ID")
        self.library_table.heading("bookname",text="Book_Name")
        self.library_table.heading("dateborrowed",text="Date_Borrowed")
        self.library_table.heading("datedue",text="Date_Due")
        self.library_table.heading("latereturn",text="Late_Return")
        self.library_table.heading("dateoverdue",text="Date_Over_Due")
        self.library_table.heading("actualprice",text="Actualprice")


        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)       

        self.library_table.column("membertype",width=100)
        self.library_table.column("idnumber",width=100)
        self.library_table.column("department",width=100)
        self.library_table.column("year",width=100)
        self.library_table.column("name",width=100)
        self.library_table.column("mobileno",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("bookname",width=100)
        self.library_table.column("dateborrowed",width=100)
        self.library_table.column("datedue",width=100)
        self.library_table.column("latereturn",width=100)
        self.library_table.column("dateoverdue",width=100)
        self.library_table.column("actualprice",width=100)
       
        self.fatch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)

    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="mysql",database="librarymanagementsystem")
        my_cursor=conn.cursor()
        my_cursor.execute("select*from library")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
           self.library_table.delete(*self.library_table.get_children())
           for  i in  rows:
                  self.library_table.insert("",END,values=i)
        conn.commit()
        conn.close()    

    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']
        
        self.Member_var.set(row[0])
        self.ID_number_var.set(row[1])
        self.Department_var.set(row[2]) 
        self.Year_var.set(row[3])
        self.Name_var.set(row[4]) 
        self.Mobile_no_var.set(row[5]) 
        self.Book_ID_var.set(row[6])
        self.Book_Name_var.set(row[7])
        self.Date_Borrowed_var.set(row[8])
        self.Due_Date_var.set(row[9])
        self.Late_Return_var.set(row[10])
        self.Date_Over_Due_var.set(row[11])
        self.ActualPrice_var.set(row[12])  

    def showdata(self):
        self.textbox.insert(END,"Member_type\t\t"+self.Member_var.get()+"\n")    
        self.textbox.insert(END,"Id number\t\t"+self.ID_number_var.get()+"\n")
        self.textbox.insert(END,"Department\t\t"+self.Department_var.get()+"\n")
        self.textbox.insert(END,"Year\t\t"+self.Year_var.get()+"\n")
        self.textbox.insert(END,"Name\t\t"+self.Name_var.get()+"\n")
        self.textbox.insert(END,"Mobileno\t\t"+self.Mobile_no_var.get()+"\n")
        self.textbox.insert(END,"BookId\t\t"+self.Book_ID_var.get()+"\n")
        self.textbox.insert(END,"BookName\t\t"+self.Book_Name_var.get()+"\n")
        self.textbox.insert(END,"Datebrrowed\t\t"+self.Date_Borrowed_var.get()+"\n")
        self.textbox.insert(END,"DueDate\t\t"+self.Due_Date_var.get()+"\n")
        self.textbox.insert(END,"Latereturn\t\t"+self.Late_Return_var.get()+"\n")
        self.textbox.insert(END,"DateoverDue\t\t"+self.Date_Over_Due_var.get()+"\n")
        self.textbox.insert(END,"Actualprice\t\t"+self.ActualPrice_var.get()+"\n")

    def reset(self):
        self.Member_var.set(""),
        self.ID_number_var.set(""),
        self.Department_var.set(""),     
        self.Year_var.set(""),        
        self.Name_var.set(""),
        self.Mobile_no_var.set(""),
        self.Book_ID_var.set(""),
        self.Book_Name_var.set(""),
        self.Date_Borrowed_var.set(""),
        self.Due_Date_var.set(""), 
        self.Late_Return_var.set(""),
        self.Date_Over_Due_var.set(""),
        self.ActualPrice_var.set("")
        self.textbox.delete("1.0",END)      
    def iExit(self):
      iExit=tkinter.messagebox.askyesno("Library Management System","Do you want to Exit")
      if iExit>0:
        self.root.destroy()
        return
    
    def update(self):     
        conn=mysql.connector.connect(host="localhost",username="root",password="mysql",database="librarymanagementsystem")
        my_cursor=conn.cursor()
        my_cursor.execute("update library set Membertype=%s,Department=%s,Year=%s,Name=%s,Mobileno=%s,BookId=%s,BookName=%s,DateBorrowed=%s,DateDue=%s,LateReturn=%s,DateOverDue=%s,Actualprice=%s where IDnumber=%s",(
                                                                              self.Member_var.get(),
                                                                              self.Department_var.get(),
                                                                              self.Year_var.get(),
                                                                              self.Name_var.get(),
                                                                              self.Mobile_no_var.get(),
                                                                              self.Book_ID_var.get(),
                                                                              self.Book_Name_var.get(),
                                                                              self.Date_Borrowed_var.get(),
                                                                              self.Due_Date_var.get(),
                                                                              self.Late_Return_var.get(),
                                                                              self.Date_Over_Due_var.get(),
                                                                              self.ActualPrice_var.get(),
                                                                              self.ID_number_var.get()                  
                                                    ))
        conn.commit()
        self.fatch_data()
        self.reset()
        conn.close()
        messagebox.showinfo("Sucess","Member has been updated")                              

    def delete(self):
      if self.ID_number_var.get()=="":
         messagebox.showerror("Error","First select the member")
      else:
          conn=mysql.connector.connect(host="localhost",username="root",password="mysql",database="librarymanagementsystem")
          my_cursor=conn.cursor()
          query="delete from library where IDnumber=%s"
          value=(self.ID_number_var.get())
          my_cursor.execute(query,(value,))
           
          conn.commit()
          self.fatch_data()
          self.reset()
          conn.close
          messagebox.showinfo("Sucess","Member has been Deleted") 





if __name__=="__main__":
  root=Tk()
  obj=LibraryManagementSystem(root)
  root.mainloop()