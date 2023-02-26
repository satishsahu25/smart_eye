from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import  messagebox
import mysql.connector
import cv2



class Student:
    def __init__(self, rootwindow):
        self.rootwindow = rootwindow
        self.rootwindow.geometry("1920x1080+0+0")
        self.rootwindow.title("Student Details")

        # ============varaibales===========
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_id=IntVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_name=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_teacher=StringVar()
        self.var_address=StringVar()
        self.var_radio1=StringVar()


        # //for images
        img = Image.open(r"images\students.jpg")
        img = img.resize((500, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        flbl = Label(self.rootwindow, image=self.photoimg)
        flbl.place(x=0, y=0, width=500, height=130)

        # *********Image-2********
        img1 = Image.open(r"images\students2.jfif")
        img1 = img1.resize((500, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        flbl2 = Label(self.rootwindow, image=self.photoimg1)
        flbl2.place(x=500, y=0, width=500, height=130)

        # *********Image-3********
        img2 = Image.open(r"images\students3.jpg")
        img2 = img2.resize((550, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        flbl3= Label(self.rootwindow, image=self.photoimg2)
        flbl3.place(x=1000, y=0, width=550, height=130)

        img3 = Image.open(r"images\mlbgimg.jpg")
        img3 = img3.resize((1800, 890), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.rootwindow, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1800, height=890)

        # labelling on the bg image
        titlelabel=Label(text="STUDENT DETAILS",font=("Calibiri",35,"bold"),bg="white",fg="red")
        titlelabel.place(x=0,y=130,width=1550,height=50)

        # //making frame
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=50,y=60,width=1420,height=580)

        # //dividing  left frame/////Student details frame
        leftframe=LabelFrame(main_frame,bd=3,bg="white",relief=RIDGE,text="Student Details",font="Calibiri")
        leftframe.place(x=10,y=10,width=690,height=565)

        left_frame_img = Image.open(r"images\students3.jpg")
        left_frame_img = left_frame_img.resize((550, 130), Image.ANTIALIAS)
        self.left_img = ImageTk.PhotoImage(left_frame_img)
        left_img_label = Label(leftframe, image=self.left_img)
        left_img_label.place(x=10, y=5, width=100, height=100)

        # ***current course****
        curr_course_frame= LabelFrame(leftframe, bd=2, bg="white", relief=RIDGE, text="Current Course Information", font="Calibiri")
        curr_course_frame.place(x=5, y=130, width=670, height=100)

        # department Combobox
        dep_label=Label(curr_course_frame,text="Department :",font=("Calibiri",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=2,pady=5)

        dep_combo=ttk.Combobox(curr_course_frame,textvariable=self.var_dep,font=("Calibiri",12,"bold"),width=17,state="readonly")
        dep_combo['values']=('Select Department','Computer',"Mechanical","Civil","Biotech","Chemical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=5,sticky=W)

        # Course Combobox
        dep_label=Label(curr_course_frame,text="Course :",font=("Calibiri",12,"bold"),bg="white")
        dep_label.grid(row=0,column=2,padx=2,pady=5)

        dep_combo=ttk.Combobox(curr_course_frame,textvariable=self.var_course,font=("Calibiri",12,"bold"),width=17,state="readonly")
        dep_combo['values']=('Select Course','B.Tech',"M.Tech","P.hd")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=3,padx=2,pady=5,sticky=W)

        # Year Combobox
        dep_label=Label(curr_course_frame,text="Year :",font=("Calibiri",12,"bold"),bg="white")
        dep_label.grid(row=1,column=0,padx=2,pady=5)

        dep_combo=ttk.Combobox(curr_course_frame,textvariable=self.var_year,font=("Calibiri",12,"bold"),width=17,state="readonly")
        dep_combo['values']=('Select Year','2020-2021',"2021-2022","2022-2023")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=1,padx=2,pady=5,sticky=W)

        # Semester Combobox
        dep_label=Label(curr_course_frame,text="Semester :",font=("Calibiri",12,"bold"),bg="white")
        dep_label.grid(row=1,column=2,padx=2,pady=5)

        dep_combo=ttk.Combobox(curr_course_frame,textvariable=self.var_semester,font=("Calibiri",12,"bold"),width=17,state="readonly")
        dep_combo['values']=('Select Semester','1st',"2nd")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=3,padx=2,pady=5,sticky=W)

        # ***Student Class Information****
        student_class_frame= LabelFrame(leftframe, bd=2, bg="white", relief=RIDGE, text="Student Class Information", font="Calibiri")
        student_class_frame.place(x=5, y=230, width=670, height=305)

        # Student ID
        studentid_label = Label(student_class_frame, text="Student ID :", font=("Calibiri", 12, "bold"), bg="white")
        studentid_label.grid(row=0, column=0, padx=2, pady=5)

        studentID_entry=ttk.Entry(student_class_frame,textvariable=self.var_id,width=20,font=("Calibiri",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=2,pady=5,sticky=W)

        # Student Name
        studentname_label = Label(student_class_frame,text="Student Name :", font=("Calibiri", 12, "bold"), bg="white")
        studentname_label.grid(row=0, column=2, padx=2, pady=5)

        studentname_entry=ttk.Entry(student_class_frame, textvariable=self.var_name,width=20,font=("Calibiri",12,"bold"))
        studentname_entry.grid(row=0,column=3,padx=2,pady=5,sticky=W)

        # Class Division
        class_div_label = Label(student_class_frame, text="Class Division :", font=("Calibiri", 12, "bold"), bg="white")
        class_div_label.grid(row=1, column=0, padx=2, pady=5)

        div_combo=ttk.Combobox(student_class_frame,textvariable=self.var_div,font=("Calibiri",12,"bold"),width=18,state="readonly")
        div_combo['values']=('A',"B",'C','D')
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=2,pady=5,sticky=W)

        # Roll No.
        roll_num_label = Label(student_class_frame, text="Roll No :", font=("Calibiri", 12, "bold"), bg="white")
        roll_num_label.grid(row=1, column=2, padx=2, pady=5)

        roll_num_entry=ttk.Entry(student_class_frame,width=20, textvariable=self.var_roll,font=("Calibiri",12,"bold"))
        roll_num_entry.grid(row=1,column=3,padx=2,pady=5,sticky=W)

        # DOB.
        dob_label = Label(student_class_frame, text="DOB :", font=("Calibiri", 12, "bold"), bg="white")
        dob_label.grid(row=2, column=0, padx=2, pady=5)

        dob_entry=ttk.Entry(student_class_frame, textvariable=self.var_dob,width=20,font=("Calibiri",12,"bold"))
        dob_entry.grid(row=2,column=1,padx=2,pady=5,sticky=W)

        # Gender
        gender_label = Label(student_class_frame, text="Gender :", font=("Calibiri", 12, "bold"), bg="white")
        gender_label.grid(row=2, column=2, padx=2, pady=5)

        gender_combo=ttk.Combobox(student_class_frame,textvariable=self.var_gender,font=("Calibiri",12,"bold"),width=18,state="readonly")
        gender_combo['values']=('Male',"Female",'Other')
        gender_combo.current(0)
        gender_combo.grid(row=2,column=3,padx=2,pady=5,sticky=W)


        # Email
        email_label = Label(student_class_frame, text="Email :", font=("Calibiri", 12, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx=2, pady=5)

        email_entry=ttk.Entry(student_class_frame,width=20, textvariable=self.var_email,font=("Calibiri",12,"bold"))
        email_entry.grid(row=3,column=1,padx=2,pady=5,sticky=W)


        # Phone num
        phone_label = Label(student_class_frame, text="Phone no :", font=("Calibiri", 12, "bold"), bg="white")
        phone_label.grid(row=3, column=2, padx=2, pady=5)

        phone_entry=ttk.Entry(student_class_frame,width=20, textvariable=self.var_phone,font=("Calibiri",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=2,pady=5,sticky=W)


        # Address
        address_label = Label(student_class_frame, text="Address :", font=("Calibiri", 12, "bold"), bg="white")
        address_label.grid(row=4, column=0, padx=2, pady=5)

        address_entry=ttk.Entry(student_class_frame,width=20, textvariable=self.var_address,font=("Calibiri",12,"bold"))
        address_entry.grid(row=4,column=1,padx=2,pady=5,sticky=W)


        # Email
        teacher_label = Label(student_class_frame, text="Teacher :", font=("Calibiri", 12, "bold"), bg="white")
        teacher_label.grid(row=4, column=2, padx=2, pady=5)

        teacher_entry=ttk.Entry(student_class_frame,width=20, textvariable=self.var_teacher,font=("Calibiri",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=2,pady=5,sticky=W)


        # //radio buttons

        radiobtn1=ttk.Radiobutton(student_class_frame, variable=self.var_radio1,text="Take Photo Sample", value="Yes")
        radiobtn1.grid(row=5,column=0,padx=5)
        radiobtn2=ttk.Radiobutton(student_class_frame, variable=self.var_radio1,text="No Photo Sample", value="No")
        radiobtn2.grid(row=5,column=1)

        # button frames
        btn_frame=Frame(student_class_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=10,y=200,width=650,height=40)

        # inside buttons of btn frame in student class

        # save btn
        save_btn=Button(btn_frame,text="Save",command=self.save_data,font=("Calibiri",13,"bold"),bg="blue",fg="white",width=14,bd=1)
        save_btn.grid(row=0,column=0,padx=10,pady=2)

        update_btn=Button(btn_frame,text="Update",command=self.updatedata,font=("Calibiri",13,"bold"),bg="blue",fg="white",width=14,bd=1)
        update_btn.grid(row=0,column=1,padx=5,pady=2)

        delete_btn=Button(btn_frame,text="Delete",command=self.del_data,font=("Calibiri",13,"bold"),bg="blue",fg="white",width=14,bd=1)
        delete_btn.grid(row=0,column=2,padx=5,pady=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,font=("Calibiri",13,"bold"),bg="blue",fg="white",width=14,bd=1)
        reset_btn.grid(row=0,column=3,padx=5,pady=2)


        take_update_frame=Frame(student_class_frame,bd=2,relief=RIDGE,bg="white")
        take_update_frame.place(x=10, y=240, width=650, height=37)

        take_photosample_btn = Button(take_update_frame,command=self.generate_data, text="Take Photo Sample", font=("Calibiri", 13, "bold"), bg="blue", fg="white", width=25,
                            bd=1)
        take_photosample_btn.grid(row=0, column=1, padx=180, pady=2)

        # update_photosample_btn = Button(take_update_frame, text="Update Photo Sample", font=("Calibiri", 13, "bold"), bg="blue", fg="white", width=30,
        #                    bd=1)
        # update_photosample_btn.grid(row=0, column=1, padx=5, pady=2)




        # //dividing label  rights frame
        rightframe=LabelFrame(main_frame,bd=3,bg="white",relief=RIDGE,text="Student Details",font="Calibiri")
        rightframe.place(x=710,y=10,width=690,height=560)

        right_frame_img = Image.open(r"images\students3.jpg")
        right_frame_img = right_frame_img.resize((550, 130), Image.ANTIALIAS)
        self.right_img = ImageTk.PhotoImage(right_frame_img)
        right_img_label = Label(rightframe, image=self.right_img)
        right_img_label.place(x=10, y=5, width=100, height=100)


        # ************** Search System***************
        search_frame= LabelFrame(rightframe, bd=2, bg="white", relief=RIDGE, text="Search System", font="Calibiri")
        search_frame.place(x=5, y=110, width=670, height=70)

        search_label = Label(search_frame, text="Search by:", font=("Calibiri", 12, "bold"), bg="white")
        search_label.grid(row=0, column=0, padx=2, pady=5)

        search_combo=ttk.Combobox(search_frame,font=("Calibiri",12,"bold"),width=17,state="readonly")
        search_combo['values']=('Select','Roll no',"Phone no")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=5,sticky=W)

        search_entry=ttk.Entry(search_frame,width=20,font=("Calibiri",12,"bold"))
        search_entry.grid(row=0,column=2,padx=2,pady=5,sticky=W)

        search_btn=Button(search_frame,text="Search",font=("Calibiri",10,"bold"),bg="blue",fg="white",width=8,bd=1)
        search_btn.grid(row=0,column=3,padx=5,pady=2)

        show_all_btn=Button(search_frame,text="Show All",font=("Calibiri",10,"bold"),bg="blue",fg="white",width=8,bd=1)
        show_all_btn.grid(row=0,column=4,padx=5,pady=2)

        # ===================Table frame=====================
        table_frame= LabelFrame(rightframe, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=190, width=670, height=300)

        x_scroll=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        y_scroll=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=('dep','course','year','semester','id','name','div','roll','gender','dob','phone','address','teacher','photo','email'),xscrollcommand=x_scroll.set,yscrollcommand=y_scroll.set)
        x_scroll.pack(side=BOTTOM,fill=X)
        y_scroll.pack(side=RIGHT,fill=Y)
        x_scroll.config(command=self.student_table.xview)
        y_scroll.config(command=self.student_table.yview)

        # //to show headers
        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("semester", text="Semester")
        self.student_table.heading("id",text="ID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll no")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo", text="Photo")
        self.student_table.heading("email", text="Email")
        self.student_table["show"]="headings"

        self.student_table.pack(fill=BOTH,expand=1)
        # //setting the width of every column
        self.student_table.column("id",width=100)
        self.student_table.column("photo",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("semester",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.bind("<ButtonRelease>",self.get_cursor_data)
        self.fetch_data()

        # ===============Function Declaration==================
    def save_data(self):
        # by get method we take values from varaibles
        if self.var_dep.get() == "Select Department" or self.var_name == "" or self.var_id == "":
            # self.rootwindow means show message box here itself only
            messagebox.showerror("Error","All fields are required",parent=self.rootwindow)
        else:
            # messagebox.showinfo("Info","Data added successfully")
            try:
                conn=mysql.connector.connect(username="root",password="satman73#",host="localhost",database="facial_attendance")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_semester.get(),
                                                                                                            self.var_id.get(),
                                                                                                            self.var_name.get(),
                                                                                                            self.var_div.get(),
                                                                                                            self.var_roll.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_teacher.get(),
                                                                                                            self.var_radio1.get(),
                                                                                                            self.var_email.get()
                                                                                                        ))
                conn.commit()
                # so that data automatically changes
                self.fetch_data()
                conn.close()
                messagebox.showwarning("Success","Student details has been added successfully",parent=self.rootwindow)
            except Exception as err:
                messagebox.showerror("Error",f"Due to :{str(err)}",parent=self.rootwindow)


    # =======================fetch data=========================
    def fetch_data(self):
        conn = mysql.connector.connect(username="root", password="satman73#", host="localhost",
                                        database="facial_attendance")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        student_data=my_cursor.fetchall()

        if len(student_data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in student_data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    # =======================get cursor data=========================
    def get_cursor_data(self,event=""):
        # focussing the varaible
        cursor_focus=self.student_table.focus()
        # getting content
        content=self.student_table.item(cursor_focus)
        data=content["values"]


        # now setting the values
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_phone.set(data[10]),
        self.var_address.set(data[11]),
        self.var_teacher.set(data[12]),
        self.var_radio1.set(data[13]),
        self.var_email.set(data[14])

    # ==========update function===============
    def updatedata(self):
        if self.var_dep.get() == "Select Department" or self.var_name == "" or self.var_id == "":
            # self.rootwindow means show message box here itself only
            messagebox.showerror("Error","All fields are required",parent=self.rootwindow)
        else:
            try:
                updatestudent=messagebox.askyesno("Update","Are you sure to update ?",parent=self.rootwindow)
                if updatestudent>0:
                    conn = mysql.connector.connect(username="root", password="satman73#", host="localhost",database="facial_attendance")
                    my_cursor = conn.cursor()
                    my_cursor.execute(f"UPDATE student SET dep=%s,course=%s,`year`=%s,semester=%s,`name`=%s,`div`=%s,roll=%s,gender=%s,dob=%s,phone=%s,address=%s,teacher=%s,photo=%s,email=%s WHERE id=%s",(
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_email.get(),
                        self.var_id.get()

                    ))
                else:
                    if not updatestudent:
                        return
                messagebox.showinfo("Success","Student details updated successfully",parent=self.rootwindow)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.rootwindow)


    # ==================deleting the data==================
    def del_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Student is must be required",parent=self.rootwindow)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to delete this student",parent=self.rootwindow)
                if delete>0:
                    conn = mysql.connector.connect(username="root", password="satman73#", host="localhost", database="facial_attendance")
                    my_cursor = conn.cursor()
                    sql="delete from student where id=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student deleted successfully",parent=self.rootwindow)
            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.rootwindow)


    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_id.set("")
        self.var_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")



# =====================Generate dataset or take photo sample======================
    def generate_data(self):
        if self.var_dep.get() == "Select Department" or self.var_name == "" or self.var_id == "":
            messagebox.showerror("Error","All fields are required",parent=self.rootwindow)
        else:
            try:
                conn = mysql.connector.connect(username="root", password="satman73#", host="localhost",database="facial_attendance")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                my_result=my_cursor.fetchall()
                ids=0
                idd=self.var_id.get()
                for x in my_result:
                    ids+=1
                sqlcommand = f"UPDATE student SET dep=%s,course=%s,`year`=%s,semester=%s,`name`=%s,`div`=%s,roll=%s,gender=%s,dob=%s,phone=%s,address=%s,teacher=%s,photo=%s,email=%s WHERE id=%s"
                my_cursor.execute(sqlcommand, (
                                                                                          self.var_dep.get(),
                                                                                          self.var_course.get(),
                                                                                          self.var_year.get(),
                                                                                          self.var_semester.get(),
                                                                                          self.var_name.get(),
                                                                                          self.var_div.get(),
                                                                                          self.var_roll.get(),
                                                                                          self.var_gender.get(),
                                                                                          self.var_dob.get(),
                                                                                          self.var_phone.get(),
                                                                                          self.var_address.get(),
                                                                                          self.var_teacher.get(),
                                                                                          self.var_radio1.get(),
                                                                                          self.var_email.get(),
                                                                                          self.var_id.get()==ids+1
                                                                                      ))
                conn.commit()
                self.fetch_data()
                # self.reset_data()
                conn.close()
            

                # ===================load predefined data on face frontal openncv================
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
                

                def face_cropped(img):
                    # converting bgr images in gray scale
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(img,1.3,5)
                    # scaling factor=1.3
                    # minimum neighborus=5

                    for (x,y,w,h) in faces:
                        # storing the images in folder
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                # opening camera
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    # reading the images
                    ret,myframe=cap.read()
                    if face_cropped(myframe) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(myframe),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(idd)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data set completed")

            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.rootwindow)








if __name__ == "__main__":
    root = Tk()
    object = Student(root)
    root.mainloop()
