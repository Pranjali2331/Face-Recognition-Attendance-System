import tkinter as tk
import subprocess
from tkinter import*
from PIL import ImageTk, Image

class Face_Registration_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry =("1530x790+0+0")
        self.root.title("Face Registration System")
        
        #background image
        img=Image.open(r"Images\Background.jpg")
        img=img.resize((1920,1080), Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        background_img=Label(self.root, image=self.photoimg)
        background_img.place(x=0, y=0, width=1920, height=1080)
        
        #Title
        title_label=Label(background_img, text="FACE RECOGNITION ATTENDANCE SYSTEM", font=("times new roman",35,"bold"),bg="white",fg="red")
        title_label.place(x=0, y=0, width=1550, height=45)
        
        #Student Button
        img1=Image.open(r"Images\Student.jpg")
        img1=img1.resize((300,300), Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        b1=Label(background_img, image=self.photoimg1)
        b1.place(x=50, y=100, width=300, height=300)
        
        b1_1=Button(background_img, command=self.register_student,text="Student Registration", cursor="hand2", font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=50, y=400, width=300, height=30)
        
        #Attendance Taker
        img2=Image.open(r"Images\face_detection.png")
        img2=img2.resize((300,300), Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        b1=Label(background_img, image=self.photoimg2)
        b1.place(x=400, y=100, width=300, height=300)

        b1_1=Button(background_img,command=self.take_attendance, text="Take Attendance", cursor="hand2", font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=400, y=400, width=300, height=30)
        
        #Train Button
        img5=Image.open(r"Images\face.jpg")
        img5=img5.resize((300,300), Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Label(background_img, image=self.photoimg5)
        b1.place(x=50, y=500, width=300, height=300)

        b1_1=Button(background_img, text="Train Image", cursor="hand2",command=self.train_image, font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=50, y=800, width=300, height=30)
        
        #See Attendance
        img6=Image.open(r"Images\face.jpg")
        img6=img6.resize((300,300), Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Label(background_img, image=self.photoimg6)
        b1.place(x=400, y=500, width=300, height=300)

        b1_1=Button(background_img, text="See Attendance", cursor="hand2",command=self.see_attendance, font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=400, y=800, width=300, height=30)


    def register_student(self):
        print("Student Registration button clicked")
        subprocess.run(["python", "get_faces_from_camera_tkinter.py"])

    def take_attendance(self):
        print("Attendance Taker button clicked")
        subprocess.run(["python", "attendance_taker.py"])

    def train_image(self):
        print("Train Image button clicked")
        subprocess.run(["python", "features_extraction_to_csv.py"])

    def see_attendance(self):
        print("See Attendance button clicked")
        subprocess.run(["python", "app.py"])

def main():
    root = tk.Tk()
    my_window = Face_Registration_System(root)
    root.mainloop()

if __name__ == "__main__":
    main()
