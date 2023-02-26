from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import  messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime
# from main import Face_Recog_Sys



class FaceRecognition:
    def __init__(self, rootwindow):
        self.rootwindow = rootwindow
        self.rootwindow.geometry("1920x1080+0+0")
        self.rootwindow.title("Face Recognition") 

        # labelling on the bg image
        titlelabel=Label(self.rootwindow,text="Face Recognition",font=("Calibiri",35,"bold"),bg="white",fg="red")
        titlelabel.place(x=0,y=0,width=1550,height=50) 


        # left image

        left_img = Image.open(r"images\facedetect.jpg")
        left_img = left_img.resize((800, 800), Image.ANTIALIAS)
        self.photo_left = ImageTk.PhotoImage(left_img)
        left_img_label = Label(self.rootwindow, image=self.photo_left)
        left_img_label.place(x=0, y=50, width=800, height=800) 


        # right image
        right_img = Image.open(r"images\face_detect.png")
        right_img = right_img.resize((800, 800), Image.ANTIALIAS)
        self.photo_right = ImageTk.PhotoImage(right_img)
        right_img_label = Label(self.rootwindow, image=self.photo_right)
        right_img_label.place(x=800, y=50, width=800, height=800) 

        # recognize button
        recognize_start_btn=Button(self.rootwindow,text="Start My Recognition",command=self.recognizemyface,font=("Calibiri",15,"bold"),bg="blue",fg="white",width=20,bd=1)
        recognize_start_btn.place(x=700, y=400, width=200, height=100)



# ===================Attendance=======================================

    def mark_attendance(self,i,r,n,d):
        with open("attendance.csv","r+",newline="\n") as f:
            mydatalist=f.readlines()
            namelist=[]
            for line in mydatalist:
                entry=line.split(',')
                namelist.append(entry[0])
                # not repeating the attendance
            if((i not in namelist) and (r not in namelist) and (n not in namelist) and (d not in namelist)):
                # print(i,r,n,d)

                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtstring=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtstring},{d1},Present")
            
                    

    def mainback(self):
        # self.new_window=Toplevel(self.rootwindow)
        # self.app=Face_Recog_Sys(self.new_window)
        self.rootwindow.destroy()

# ====================================FaceRecognition==================================================================
    def recognizemyface(self):
        def draw_boundary(img, classifier,scaleFactor,MinNeighbors,color,text,clf):
            grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(grayimg,scaleFactor,MinNeighbors)
            
            coord=[]
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                # predicitng from model
                id,predict=clf.predict(grayimg[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn = mysql.connector.connect(username="root", password="satman73#", host="localhost",database="facial_attendance")
                my_cursor = conn.cursor()


                my_cursor.execute("select name from student where id="+str(id))
                person_name=my_cursor.fetchone()
                person_name='+'.join(person_name)

                my_cursor.execute("select roll from student where id="+str(id))
                person_roll=my_cursor.fetchone()
                person_roll='+'.join(person_roll)
                
                my_cursor.execute("select dep from student where id="+str(id))
                person_dep=my_cursor.fetchone()
                person_dep='+'.join(person_dep)

                my_cursor.execute("select id from student where id="+str(id))
                person_id=my_cursor.fetchone()
                person_id='+'.join(person_id)

                if confidence>77:
                    # showing the name and id
                    cv2.putText(img,f"ID:{person_id}",(x,y-75),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
                    cv2.putText(img,f"Roll:{person_roll}",(x,y-55),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
                    cv2.putText(img,f"Name:{person_name}",(x,y-30),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
                    cv2.putText(img,f"Dep:{person_dep}",(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
                    self.mark_attendance(person_id,person_roll,person_name,person_dep)
                    
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)

                coord=[x,y,w,h]

            return coord


        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        # jo apna trainer model hai aur frontface alog both are required
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("trainer.xml")

        # opening camera to detect

        video_Cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)

        while True:
            ret,img=video_Cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Your Face is being recognized",img)

            if cv2.waitKey(1)==13:
                break
        
        video_Cap.release()
        cv2.destroyAllWindows()

            


if __name__ == "__main__":
    root = Tk()
    object = FaceRecognition(root)
    root.mainloop()