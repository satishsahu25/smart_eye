from tkinter import *
from tkinter import ttk
# //for images managing
from PIL import ImageTk, Image
import os

class Developer:
    # constructor call
    def __init__(self, rootwindow):
        self.rootwindow = rootwindow
        # x-axis and y-axis from 0,0
        self.rootwindow.geometry("1920x1080+0+0")
        self.rootwindow.title("Developer")

        # labelling on the bg image
        titlelabel=Label(self.rootwindow,text="Developer",font=("Calibiri",35,"bold"),bg="white",fg="red")
        titlelabel.place(x=0,y=0,width=1550,height=50)

        img = Image.open(r"images\mlbgimg.jpg")
        img = img.resize((1550, 800), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        flbl = Label(self.rootwindow, image=self.photoimg)
        flbl.place(x=0, y=50, width=1550, height=800)

        # //making frame
        main_frame=Frame(flbl,bd=2,bg="white")
        main_frame.place(x=1000,y=60,width=500,height=400)

        img_top = Image.open(r"images\satish_profimage.jpg")
        img_top = img_top.resize((200, 200), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img_top)

        flbl = Label(main_frame, image=self.photoimg2)
        flbl.place(x=10, y=10, width=200, height=200)


        # labelling on the profile image
        titlelabel=Label(main_frame,text="Hello, I am Satish Sahu. Aspiring computer programmer with",font=("Calibiri",13,"bold"),bg="white",fg="red")
        titlelabel.place(x=5,y=220)
        titlelabel=Label(main_frame,text="a BTech (Hons.) degree and proven problem-solving and",font=("Calibiri",13,"bold"),bg="white",fg="red")
        titlelabel.place(x=5,y=240)
        titlelabel=Label(main_frame,text="troubleshooting skills. Interned with RUSHTech as a junior",font=("Calibiri",13,"bold"),bg="white",fg="red")
        titlelabel.place(x=5,y=260)
        titlelabel=Label(main_frame,text="database developer for financial programs. Seeking an entry-",font=("Calibiri",13,"bold"),bg="white",fg="red")
        titlelabel.place(x=5,y=280)
        titlelabel=Label(main_frame,text="-level programmer or coder position to continue expanding ",font=("Calibiri",13,"bold"),bg="white",fg="red")
        titlelabel.place(x=5,y=300)
        titlelabel=Label(main_frame,text="my knowledge of different languages and systems.",font=("Calibiri",13,"bold"),bg="white",fg="red")
        titlelabel.place(x=5,y=320)


if __name__ == "__main__":
    root = Tk()
    object = Developer(root)
    # //closing the loop
    root.mainloop()