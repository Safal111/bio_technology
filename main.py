from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import cv2
import os
import numpy as np
from tkinter import messagebox
import mysql.connector

from students import Students


class Use_of_Bio_Technology:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1400x700+60+30")
        self.root.title("Use of Bio Technology in Face Recognition Attendance System")

        # Background color
        bg_color = "#F9F9F9"

        # Heading Frame
        heading_frame = Frame(self.root, bg=bg_color, bd=5)
        heading_frame.place(x=0, y=0, relwidth=1)

        # Heading Label
        heading_label = Label(
            heading_frame,
            text="Face Recognition Attendance System",
            font=("Arial", 28, "bold"),
            bg=bg_color,
            fg="#4A4A4A",
        )
        heading_label.pack(side="left", padx=50, pady=10)

        # Body Frame
        body_frame = Frame(self.root, bg=bg_color)
        body_frame.place(x=50, y=100, width=1300, height=520)

        # Students Details Button
        # students_img = Image.open("images/abc.png")
        # students_img = students_img.resize((200, 200), Image.ANTIALIAS)
        # students_photo_img = ImageTk.PhotoImage(students_img)
        # students_img.show()

        students_button = Button(
            body_frame,
            # image=students_photo_img,
            text="Students Details",
            compound="top",
            font=("Arial", 16, "bold"),
            bg="#4A4A4A",
            fg="white",
            bd=0,
            padx=10,
            pady=10,
            cursor="hand2",
            command=self.students_detail_button,
        )
        students_button.place(x=100, y=100)

        # Face Detection Button
        # detection_img = Image.open(
        #     r"C:\Users\Safal Karki\Desktop\Production Project\project\images\facedetection.png"
        # )
        # detection_img = detection_img.resize((200, 200), Image.ANTIALIAS)
        # detection_photo_img = ImageTk.PhotoImage(detection_img)

        detection_button = Button(
            body_frame,
            # image=detection_photo_img,
            text="Face Detection",
            compound="top",
            font=("Arial", 16, "bold"),
            bg="#4A4A4A",
            fg="white",
            bd=0,
            padx=10,
            pady=10,
            cursor="hand2",
            command=self.face_recognition,
        )
        detection_button.place(x=400, y=100)

        # Train Data Button
        # train_img = Image.open(
        #     r"C:\Users\Safal Karki\Desktop\Production Project\project\images\training.jpg"
        # )
        # train_img = train_img.resize((200, 200), Image.ANTIALIAS)
        # train_photo_img = ImageTk.PhotoImage(train_img)

        train_button = Button(
            body_frame,
            # image=train_photo_img,
            text="Train Data",
            compound="top",
            font=("Arial", 16, "bold"),
            bg="#4A4A4A",
            fg="white",
            bd=0,
            padx=10,
            pady=10,
            cursor="hand2",
            command=self.train_data,
        )
        train_button.place(x=700, y=100)

        # Attendance Button
        # attendance_img = Image.open(
        #     r"C:\Users\Safal Karki\Desktop\Production Project\project\images\attendance.png"
        # )
        # attendance_img = attendance_img.resize((200, 200), Image.ANTIALIAS)
        # attendance_photo_img = ImageTk.PhotoImage(attendance_img)

        attendance_button = Button(
            body_frame,
            # image=attendance_photo_img,
            text="Attendance",
            compound="top",
            font=("Arial", 16, "bold"),
            bg="#4A4A4A",
            fg="white",
            bd=0,
            padx=10,
            pady=10,
            cursor="hand2",
        )
        attendance_button.place(x=1000, y=100)

        # Footer Frame
        footer_frame = Frame(self.root, bg="#4A4A4A", bd=5)
        footer_frame.place(x=0, y=650, relwidth=1, height=50)

        # Footer Label
        footer_label = Label(
            footer_frame,
            text="© 2023 All rights reserved. Use of Bio Technology in Face Recognition Attendance System",
            font=("Arial", 10),
            bg="#4A4A4A",
            fg="#F9F9F9",
        )
        footer_label.pack(side="bottom", anchor="center", pady=10)

    # function for students button
    def students_detail_button(self):
        self.new_window = Toplevel(self.root)
        self.app = Students(self.new_window)

    # train data
    def train_data(self):
        data_dir = "data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert("L")
            imageNp = np.array(img, "uint8")
            id = int(os.path.split(image)[1].split(".")[1])
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("training", imageNp)
            cv2.waitKey(1) == 13
        ids = np.array(ids)

        print("training classifier...")
        # train and save
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training dataset completed!!")

    # face recognition
    def face_recognition(self):
        def draw_boundry(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(
                gray_image, scaleFactor, minNeighbors
            )

            coords = []

            for x, y, w, h in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y : y + h, x : x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="",
                    database="bio_technology",
                )
                my_cursor = conn.cursor()

                print("ID before conversion:", id)
                my_cursor.execute("select id from student where id=" + str(id))
                i = my_cursor.fetchone()
                if i is not None:
                    i = str(i[0])
                else:
                    i = "unknown"

                print("ID after query:", i)

                # i = str(i)

                my_cursor.execute("select name from student where id=" + str(id))
                n = my_cursor.fetchone()
                if n is not None:
                    n = str(n[0])
                else:
                    n = ""
                # n = str(n)

                if confidence > 77:
                    cv2.putText(
                        img,
                        f"ID: {i}",
                        (x, y - 50),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8,
                        (255, 255, 255),
                        1,
                        cv2.LINE_AA,
                    )
                    cv2.putText(
                        img,
                        f"Name: {n}",
                        (x, y - 15),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8,
                        (255, 255, 255),
                        1,
                        cv2.LINE_AA,
                    )

                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 225), 3)

                    cv2.putText(
                        img,
                        "Unknown Face",
                        (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8,
                        (0, 0, 255),
                        1,
                    )

                coords = [x, y, w, h]

            return coords

        def recognize(img, clf, faceCascade):
            coord = draw_boundry(
                img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf
            )
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)

            key = cv2.waitKey(1) & 0xFF
            if key == ord("q") or key == ord("Q"):
                break

        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Use_of_Bio_Technology(root)
    root.mainloop()
