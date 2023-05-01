import mysql.connector


def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        username="root",
        password="",
        database="bio_technology",
    )
    return conn


# face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#     def take_photo(self):
#         if self.var_course.get() == "Select":
#             messagebox.showerror("Error", "All fields are required", parent=self.root)
#         else:
#             try:
#                 conn = mysql.connector.connect(
#                     host="localhost",
#                     username="root",
#                     password="",
#                     database="bio_technology",
#                 )
#                 my_cursor = conn.cursor()
#                 my_cursor.execute("select max(id) from student")
#                 myresult = my_cursor.fetchone()
#                 if myresult[0] is not None:
#                     id = myresult[0] + 1
#                 else:
#                     id = 1
#                 my_cursor.execute(
#                     "insert into student (id, course, year, semester, name, dob, email, phone, address, photo) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
#                     (
#                         id,
#                         self.var_course.get(),
#                         self.var_year.get(),
#                         self.var_semester.get(),
#                         self.var_name.get(),
#                         self.var_dob.get(),
#                         self.var_email.get(),
#                         self.var_phone.get(),
#                         self.var_address.get(),
#                         self.var_radio.get(),
#                     ),
#                 )
#                 conn.commit()
#                 self.fetch_data()
#                 self.reset_data()
#                 conn.close()

#                 # load data from opencv
#                 face_classifier = cv2.CascadeClassifier(
#                     "haarcascade_frontalface_default.xml"
#                 )

#                 # crop face
#                 def face_cropped(img):
#                     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#                     faces = face_classifier.detectMultiScale(gray, 1.3, 5)
#                     for x, y, w, h in faces:
#                         face_cropped = img[y : y + h, x : x + w]
#                         return face_cropped

#                 cap = cv2.VideoCapture(0)
#                 img_id = 0
#                 while True:
#                     ret, my_frame = cap.read()
#                     if not ret:
#                         print("Could not open camera")
#                     if my_frame is None:
#                         print("Frame is None")

#                     if face_cropped(my_frame) is not None:
#                         img_id += 1
#                         face = cv2.resize(face_cropped(my_frame), (450, 450))
#                         face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
#                         file_name_path = (
#                             "data/user." + str(id) + "." + str(img_id) + ".jpg"
#                         )
#                         cv2.imwrite(file_name_path, face)
#                         cv2.putText(
#                             face,
#                             str(img_id),
#                             (50, 50),
#                             cv2.FONT_HERSHEY_COMPLEX,
#                             2,
#                             (0, 255, 0),
#                             2,
#                         )
#                         cv2.imshow("Cropped Face", face)

#                     if cv2.waitKey(1) == 13 or int(img_id) == 100:
#                         break

#                 cap.release()
#                 cv2.destroyAllWindows()
#                 messagebox.showinfo("Result", "Generating data set completed!!!")
#             except Exception as es:
#                 messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
