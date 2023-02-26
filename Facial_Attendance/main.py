from tkinter import *
from tkinter import ttk
# //for images managing
from PIL import ImageTk, Image
from student import Student
import os
import tkinter
from train import Train
from face_detect import FaceRecognition
from attendance import Attendance
from developer import Developer
from time import strftime
from datetime import datetime

class Face_Recog_Sys:
    # constructor call
    def __init__(self, rootwindow):
        self.rootwindow = rootwindow
        # x-axis and y-axis from 0,0
        self.rootwindow.geometry("1920x1080+0+0")
        self.rootwindow.title("Face Recognition System")

        # //for imagespy
        img = Image.open(r"images\face1.png")
        # width, height, converting high level image into low level
        img = img.resize((500, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        # //making label for image
        flbl = Label(self.rootwindow, image=self.photoimg)
        # //to show in window
        flbl.place(x=0, y=0, width=500, height=130)

        # *********Image-2********
        img1 = Image.open(r"images\face2.jpg")
        img1 = img1.resize((500, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        flbl = Label(self.rootwindow, image=self.photoimg1)
        flbl.place(x=500, y=0, width=500, height=130)

        # *********Image-3********
        img2 = Image.open(r"images\face3.jpg")
        img2 = img2.resize((550, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        flbl = Label(self.rootwindow, image=self.photoimg2)
        flbl.place(x=1000, y=0, width=550, height=130)


        # *********Image-3********
        img3 = Image.open(r"images\bgimage.jpg")
        img3 = img3.resize((1800, 890), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img= Label(self.rootwindow, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1800, height=890)

        # labelling on the bg image
        titlelabel=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SOFTWARE",font=("Calibiri",35,"bold"),bg="white",fg="red")
        titlelabel.place(x=0,y=0,width=1550,height=50)


# //************************buttons*********************************

        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
        
        lbl=Label(titlelabel,font=("Calibiri",13,"bold"),bg="white",fg="blue")
        lbl.place(x=0,y=0,width=110,height=50)
        time()


        # *******Student Details btn**
        btnimg = Image.open(r"images\stud_details.jpg")
        btnimg = btnimg.resize((220, 220), Image.ANTIALIAS)
        self.photobutton = ImageTk.PhotoImage(btnimg)

        b1=Button(bg_img,image=self.photobutton,cursor="hand2",command=self.studentdetails)
        b1.place(x=200+100,y=100,width=220,height=200)

        b1_1=Button(bg_img,text="Student Details",command=self.studentdetails,cursor="hand2",font=("Calibiri",15,"bold"),bg="white",fg="red")
        b1_1.place(x=200+100,y=260,width=220,height=40)


        # ****Detect Face btn*****
        btnimg1 = Image.open(r"images\face_detect.png")
        btnimg1 = btnimg1.resize((220, 220), Image.ANTIALIAS)
        self.photobutton1 = ImageTk.PhotoImage(btnimg1)

        detectface_btn=Button(bg_img,image=self.photobutton1,command=self.facerecognition,cursor="hand2")
        detectface_btn.place(x=450+100,y=100,width=220,height=200)

        detectface_txt_btn=Button(bg_img,text="Detect Face",command=self.facerecognition,cursor="hand2",font=("Calibiri",15,"bold"),bg="white",fg="red")
        detectface_txt_btn.place(x=450+100,y=260,width=220,height=40)

        # ***Attendance btn*****
        btnimg2 = Image.open(r"images\attend.jpg")
        btnimg2 = btnimg2.resize((220, 220), Image.ANTIALIAS)
        self.photobutton2 = ImageTk.PhotoImage(btnimg2)

        attend_btn=Button(bg_img,image=self.photobutton2,command=self.attendancereport,cursor="hand2")
        attend_btn.place(x=700+100,y=100,width=220,height=200)

        attend_txt_btn=Button(bg_img,text="Attendance",command=self.attendancereport,cursor="hand2",font=("Calibiri",15,"bold"),bg="white",fg="red")
        attend_txt_btn.place(x=700+100,y=260,width=220,height=40)


        # ****Training Model btn*****
        btnimg4 = Image.open(r"images\train.jfif")
        btnimg4 = btnimg4.resize((220, 220), Image.ANTIALIAS)
        self.photobutton4 = ImageTk.PhotoImage(btnimg4)

        train_btn=Button(bg_img,image=self.photobutton4,command=self.trainmodel,cursor="hand2")
        train_btn.place(x=950+100,y=100,width=220,height=200)

        train_txt_btn=Button(bg_img,text="Train Model",command=self.trainmodel,cursor="hand2",font=("Calibiri",15,"bold"),bg="white",fg="red")
        train_txt_btn.place(x=950+100,y=260,width=220,height=40)

        # ****Photos btn*****
        btnimg5 = Image.open(r"images\photos.jfif")
        btnimg5 = btnimg5.resize((220, 220), Image.ANTIALIAS)
        self.photobutton5 = ImageTk.PhotoImage(btnimg5)

        face_btn = Button(bg_img, image=self.photobutton5,command=self.openimg, cursor="hand2")
        face_btn.place(x=300+100, y=340, width=220, height=200)

        face_txt_btn = Button(bg_img, text="Photos",command=self.openimg, cursor="hand2", font=("Calibiri", 15, "bold"), bg="white",
                               fg="red")
        face_txt_btn.place(x=300+100, y=500, width=220, height=40)

        # ****Developer btn*****
        btnimg6 = Image.open(r"images\dev.png")
        btnimg6 = btnimg6.resize((220, 220), Image.ANTIALIAS)
        self.photobutton6 = ImageTk.PhotoImage(btnimg6)

        Dev_btn = Button(bg_img, image=self.photobutton6,command=self.developerpage, cursor="hand2")
        Dev_btn.place(x=550+100, y=340, width=220, height=200)

        Dev_txt_btn = Button(bg_img, text="Developer", command=self.developerpage,cursor="hand2", font=("Calibiri", 15, "bold"), bg="white",
                               fg="red")
        Dev_txt_btn.place(x=550+100, y=500, width=220, height=40)

        # ****Exit btn*****
        btnimg7 = Image.open(r"images\exit.png")
        btnimg7 = btnimg7.resize((220, 220), Image.ANTIALIAS)
        self.photobutton7 = ImageTk.PhotoImage(btnimg7)

        exit=Button(bg_img,image=self.photobutton7,command=self.iExit,cursor="hand2")
        exit.place(x=800+100,y=340,width=220,height=200)

        exit_txt_btn=Button(bg_img,text="Exit",command=self.iExit,cursor="hand2",font=("Calibiri",15,"bold"),bg="white",fg="red")
        exit_txt_btn.place(x=800+100,y=500,width=220,height=40)

    def openimg(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Exit","Do you want to exit?",parent=self.rootwindow)
        if self.iExit>0:
            self.rootwindow.destroy()
        else:
            return

        # ================FUNCTIONS BUTTON==================

    def studentdetails(self):
        self.new_window=Toplevel(self.rootwindow)
        self.app=Student(self.new_window)   

    def trainmodel(self):
        self.new_window=Toplevel(self.rootwindow)
        self.app=Train(self.new_window)
    
    def facerecognition(self):
        self.new_window=Toplevel(self.rootwindow)
        self.app=FaceRecognition(self.new_window)
    
    def attendancereport(self):
        self.new_window=Toplevel(self.rootwindow)
        self.app=Attendance(self.new_window)

    def developerpage(self):
        self.new_window=Toplevel(self.rootwindow)
        self.app=Developer(self.new_window)
    


if __name__ == "__main__":
    root = Tk()
    object = Face_Recog_Sys(root)
    # //closing the loop
    root.mainloop()
