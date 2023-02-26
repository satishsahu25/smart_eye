from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import  messagebox
import mysql.connector
import cv2
import os
import numpy as np



class Train:
    def __init__(self, rootwindow):
        self.rootwindow = rootwindow
        self.rootwindow.geometry("1920x1080+0+0")
        self.rootwindow.title("Training Model")
        
        # labelling on the bg image
        titlelabel=Label(self.rootwindow,text="Training dataset",font=("Calibiri",35,"bold"),bg="white",fg="red")
        titlelabel.place(x=0,y=0,width=1550,height=50)

        top_img = Image.open(r"images\topimg.jpg")
        top_img = top_img.resize((1550, 250), Image.ANTIALIAS)
        self.photo_top = ImageTk.PhotoImage(top_img)
        top_img_label = Label(self.rootwindow, image=self.photo_top)
        top_img_label.place(x=0, y=55, width=1550, height=250)

        train_start_btn=Button(self.rootwindow,text="Training Start",command=self.train_classifier,font=("Calibiri",15,"bold"),bg="blue",fg="white",width=14,bd=1)
        train_start_btn.place(x=700, y=330, width=150, height=50)

        bottom_img = Image.open(r"images\manypeople.jpg")
        bottom_img = bottom_img.resize((1550, 500), Image.ANTIALIAS)
        self.photo_bottom = ImageTk.PhotoImage(bottom_img)
        bottom_img_label = Label(self.rootwindow, image=self.photo_bottom)
        bottom_img_label.place(x=0, y=400, width=1550, height=500)

    # =====================================train classifier=======================================
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        faces=[]
        ids=[]

        # exctracting the details from path whihch has all images
        for image in path:
            # converting into grayscale
            img=Image.open(image).convert("L")   
            imagenp=np.array(img,'uint8')   #uint8 is the type of data of image
            id=int(os.path.split(image)[1].split('.')[1])

            # C:\Users\User\Desktop\AttendencePy\data\user.4.1.jpg
            # 0                                        1 
            # 0                                        0   1 2 3 
            faces.append(imagenp)
            ids.append(id)
            cv2.imshow("Training",imagenp)
            cv2.waitKey(1)==13   # press enter key to continue

        # converting ids into numpy array    
        ids=np.array(ids)




        # ========================training the claasier and saving======================
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("trainer.xml")   #saving the trainer.xml file
        cv2.destroyAllWindows()
        messagebox.showinfo('Result','Training complete!!')




if __name__ == "__main__":
    root = Tk()
    object = Train(root)
    root.mainloop()