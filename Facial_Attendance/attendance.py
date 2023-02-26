from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import  messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog 
import numpy as np
from time import strftime
from datetime import datetime

mydata=[]

class Attendance:
    def __init__(self, rootwindow):
        self.rootwindow = rootwindow
        self.rootwindow.geometry("1920x1080+0+0")
        self.rootwindow.title("Attendance") 


        # =================variables======================
        self.var_attend_id = StringVar()
        self.var_attend_roll = StringVar()
        self.var_attend_name = StringVar()
        self.var_attend_dep = StringVar()
        self.var_attend_time = StringVar()
        self.var_attend_date = StringVar()
        self.var_attend_attendance = StringVar()


        # labelling on the bg image
        titlelabel=Label(self.rootwindow,text="Face Recognition",font=("Calibiri",35,"bold"),bg="white",fg="red")
        titlelabel.place(x=0,y=0,width=1550,height=50) 


                # //for images
        img = Image.open(r"images\students.jpg")
        img = img.resize((800, 250), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        flbl = Label(self.rootwindow, image=self.photoimg)
        flbl.place(x=0, y=0, width=800, height=250)

        # *********Image-2********
        img1 = Image.open(r"images\attend.jpg")
        img1 = img1.resize((800, 250), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        flbl2 = Label(self.rootwindow, image=self.photoimg1)
        flbl2.place(x=800, y=0, width=800, height=250)


        # labelling on the bg image
        titlelabel=Label(text="Attendance",font=("Calibiri",35,"bold"),bg="white",fg="red")
        titlelabel.place(x=0,y=250,width=1550,height=50)

                # //making frame
        main_frame=Frame(self.rootwindow,bd=2,bg="white")
        main_frame.place(x=0,y=300,width=1550,height=580)

                # //dividing  left frame/////Student details frame
        leftframe=LabelFrame(main_frame,bd=3,bg="white",relief=RIDGE,text="Attendance Details",font="Calibiri")
        leftframe.place(x=10,y=0,width=690,height=470)

        left_frame_img = Image.open(r"images\students3.jpg")
        left_frame_img = left_frame_img.resize((550, 130), Image.ANTIALIAS)
        self.left_img = ImageTk.PhotoImage(left_frame_img)
        left_img_label = Label(leftframe, image=self.left_img)
        left_img_label.place(x=10, y=5, width=100, height=100)

        

        left_inside_frame=Frame(leftframe,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=10,y=110,width=670,height=330)



        # attenadnce ID
        attendanceid_label = Label(left_inside_frame, text="Attendance ID :", font=("Calibiri", 12, "bold"), bg="white")
        attendanceid_label.grid(row=0, column=0, padx=2, pady=5)

        attendanceID_entry=ttk.Entry(left_inside_frame,textvariable=self.var_attend_id,width=20,font=("Calibiri",12,"bold"))
        attendanceID_entry.grid(row=0,column=1,padx=2,pady=5,sticky=W)

        # name
        name_label = Label(left_inside_frame, text="Name :", font=("Calibiri", 12, "bold"), bg="white")
        name_label.grid(row=1, column=0, padx=2, pady=5)

        name_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_name,font=("Calibiri",12,"bold"))
        name_entry.grid(row=1,column=1,padx=2,pady=5,sticky=W)

        # date
        date_label = Label(left_inside_frame, text="Date :", font=("Calibiri", 12, "bold"), bg="white")
        date_label.grid(row=0, column=2, padx=2, pady=5)

        date_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_date,font=("Calibiri",12,"bold"))
        date_entry.grid(row=0,column=3,padx=2,pady=5,sticky=W)

        # time
        time_label = Label(left_inside_frame, text="Time :", font=("Calibiri", 12, "bold"), bg="white")
        time_label.grid(row=1, column=2, padx=2, pady=5)

        time_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_time,font=("Calibiri",12,"bold"))
        time_entry.grid(row=1,column=3,padx=2,pady=5,sticky=W)

        # attendance
        attendance_label = Label(left_inside_frame, text="Attendance :", font=("Calibiri", 12, "bold"), bg="white")
        attendance_label.grid(row=2, column=0)

        attendance_combo=ttk.Combobox(left_inside_frame,font=("Calibiri",12,"bold"),textvariable=self.var_attend_attendance,width=18,state="readonly")
        attendance_combo['values']=('Status',"Present",'Absent')
        attendance_combo.current(0)
        attendance_combo.grid(row=2,column=1,padx=2,pady=5,sticky=W)

        # roll
        date_label = Label(left_inside_frame, text="Roll :", font=("Calibiri", 12, "bold"), bg="white")
        date_label.grid(row=2, column=2, padx=2, pady=5)

        date_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_roll,font=("Calibiri",12,"bold"))
        date_entry.grid(row=2,column=3,padx=2,pady=5,sticky=W)

        # department
        dep_label = Label(left_inside_frame, text="Department:", font=("Calibiri", 12, "bold"), bg="white")
        dep_label.grid(row=3, column=0, padx=2, pady=5)

        dep_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_attend_dep,font=("Calibiri",12,"bold"))
        dep_entry.grid(row=3,column=1,padx=2,pady=5,sticky=W)


   # button frames
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=10,y=150,width=650,height=40)

        # inside buttons of btn frame in student class

        # save btn
        importcsv_btn=Button(btn_frame,text="Import CSV",command=self.importcsv,font=("Calibiri",13,"bold"),bg="blue",fg="white",width=14,bd=1)
        importcsv_btn.grid(row=0,column=0,padx=10,pady=2)

        exportcsv_btn=Button(btn_frame,text="Export CSV",command=self.exportcsv,font=("Calibiri",13,"bold"),bg="blue",fg="white",width=14,bd=1)
        exportcsv_btn.grid(row=0,column=1,padx=5,pady=2)

        update_btn=Button(btn_frame,text="Update",font=("Calibiri",13,"bold"),bg="blue",fg="white",width=14,bd=1)
        update_btn.grid(row=0,column=2,padx=5,pady=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset,font=("Calibiri",13,"bold"),bg="blue",fg="white",width=14,bd=1)
        reset_btn.grid(row=0,column=3,padx=5,pady=2)


                # //dividing label  rights frame
        rightframe=LabelFrame(main_frame,bd=3,bg="white",relief=RIDGE,text="Attendance",font="Calibiri")
        rightframe.place(x=750,y=0,width=690,height=470)

        # ===================Table frame=====================
        table_frame= LabelFrame(rightframe, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=5, width=670, height=420)

        #================ Scrollbar and table=============
        scroll_x=ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.Attendancereporttable=ttk.Treeview(table_frame,column=("id","name","roll","department","date","time","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Attendancereporttable.xview)
        scroll_y.config(command=self.Attendancereporttable.yview)
        self.Attendancereporttable.heading("id",text="Attendance ID")
        self.Attendancereporttable.heading("roll",text="Roll")
        self.Attendancereporttable.heading("name",text="Name")
        self.Attendancereporttable.heading("department",text="Deaprtment")
        self.Attendancereporttable.heading("time",text="Time")
        self.Attendancereporttable.heading("date",text="Date")
        self.Attendancereporttable.heading("attendance",text="Attendance")

        self.Attendancereporttable["show"]="headings"
        self.Attendancereporttable.column("id",width=100)
        self.Attendancereporttable.column("roll",width=100)
        self.Attendancereporttable.column("name",width=100)
        self.Attendancereporttable.column("department",width=100)
        self.Attendancereporttable.column("time",width=100)
        self.Attendancereporttable.column("date",width=100)
        self.Attendancereporttable.column("attendance",width=100)
        

        self.Attendancereporttable.pack(fill=BOTH,expand=1)

        # //binding the getcursor function with table
        self.Attendancereporttable.bind("<ButtonRelease>",self.getcursordata)


    def fetchdata(self,rows):
        self.Attendancereporttable.delete(*self.Attendancereporttable.get_children())
        for i in rows:
            self.Attendancereporttable.insert('',END,values=i)
    
    # ==================import  csv======================
    def importcsv(self):
        global mydata
        mydata.clear()
        filename=filedialog.askopenfilename(initialdir=os.getcwd(),title="Select CSV File",
        filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.rootwindow)

        with open(filename) as csv_file:
            csvread=csv.reader(csv_file,delimiter=',')
            for i in csvread:
                mydata.append(i)
            
            self.fetchdata(mydata)
    

    # ==================export  csv======================
    def exportcsv(self):
        # check data is there or not
        try:
            if len(mydata) <1:
                messagebox.showerror("No Data","No data to export",parent=self.rootwindow)
                return False
            exportfilename=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Select CSV File",
            filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.rootwindow)

            with open(exportfilename,mode="w",newline='\n') as myfile:
                exportwrite=csv.writer(myfile,delimiter=',')
                for i in mydata:
                    exportwrite.writerow(i)
                messagebox.showinfo("Data Export","Data has been exported to "+os.path.basename(exportfilename)+"successfully",parent=self.rootwindow)
        except Exception as e:
            messagebox.showerror("Error",f"Due to:{str(e)} ",parent=self.rootwindow)


    # ==================get cursor data=========================  
    def getcursordata(self,event=""):
        cursor_row=self.Attendancereporttable.focus()
        content=self.Attendancereporttable.item(cursor_row)
        data=content["values"]


        # now setting the values
        self.var_attend_id.set(data[0]),
        self.var_attend_roll.set(data[1]),
        self.var_attend_name.set(data[2]),
        self.var_attend_dep.set(data[3]),
        self.var_attend_time.set(data[4]),
        self.var_attend_date.set(data[5]),
        self.var_attend_attendance.set(data[6])
    
    def reset(self):
        self.var_attend_id.set(""),
        self.var_attend_roll.set(""),
        self.var_attend_name.set(""),
        self.var_attend_dep.set(""),
        self.var_attend_time.set(""),
        self.var_attend_date.set(""),
        self.var_attend_attendance.set("")
    


        




if __name__ == "__main__":
    root = Tk()
    object = Attendance(root)
    root.mainloop()