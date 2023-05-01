from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import cv2

from db import get_connection


class Students:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x720+10+30")
        self.root.title("Use of Bio Technology in Face Recognition Attendance System")

        # Variables
        self.var_id = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_name = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_radio = StringVar()

        # Background color
        bg_color = "#F9F9F9"

        # Heading Frame
        heading_frame = Frame(self.root, bg=bg_color, bd=5)
        heading_frame.place(x=0, y=0, relwidth=1)

        # Heading Label
        heading_label = Label(
            heading_frame,
            text="Students Mangement",
            font=("Arial", 28, "bold"),
            bg=bg_color,
            fg="#4A4A4A",
        )
        heading_label.pack(side="left", padx=50, pady=10)

        # Body Frame
        body_frame = Frame(self.root, bg=bg_color)
        body_frame.place(x=50, y=100, width=1400, height=600)

        # left label frame
        left_frame = LabelFrame(
            body_frame,
            bd=2,
            relief=RIDGE,
            text="Add Students",
            font=("Arial", 12, "bold"),
            bg=bg_color,
            fg="#4A4A4A",
        )
        left_frame.place(x=10, y=10, width=600, height=575)

        # current course
        current_course_label = Label(
            left_frame,
            text="Current Course",
            font=("Arial", 12, "bold"),
            bg=bg_color,
            fg="#4A4A4A",
        )
        current_course_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        current_course_combo = ttk.Combobox(
            left_frame,
            textvariable=self.var_course,
            font=("Arial", 12),
            width=28,
            state="readonly",
        )
        current_course_combo["values"] = ("Select", "Computing", "BBA", "BCA", "HM")
        current_course_combo.current(0)
        current_course_combo.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        # year
        year_label = Label(
            left_frame,
            text="Year",
            font=("Arial", 12, "bold"),
            bg=bg_color,
            fg="#4A4A4A",
        )
        year_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        year_combo = ttk.Combobox(
            left_frame,
            textvariable=self.var_year,
            font=("Arial", 12),
            width=28,
            state="readonly",
        )
        year_combo["values"] = ("Select", "1st", "2nd", "3rd", "4th")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        # semester
        semester_label = Label(
            left_frame,
            text="Semester",
            font=("Arial", 12, "bold"),
            bg=bg_color,
            fg="#4A4A4A",
        )
        semester_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        semester_combo = ttk.Combobox(
            left_frame,
            textvariable=self.var_semester,
            font=("Arial", 12),
            width=28,
            state="readonly",
        )
        semester_combo["values"] = (
            "Select",
            "1st",
            "2nd",
            "3rd",
            "4th",
            "5th",
            "6th",
            "7th",
            "8th",
        )
        semester_combo.current(0)
        semester_combo.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        # student id
        student_id_label = Label(
            left_frame,
            text="Student ID",
            font=("Arial", 12, "bold"),
            bg=bg_color,
            fg="#4A4A4A",
        )
        student_id_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        student_id_entry = ttk.Entry(
            left_frame, textvariable=self.var_id, font=("Arial", 12), width=30
        )
        student_id_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        # student name
        student_name_label = Label(
            left_frame,
            text="Student Name",
            font=("Arial", 12, "bold"),
            bg=bg_color,
            fg="#4A4A4A",
        )
        student_name_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        student_name_entry = ttk.Entry(
            left_frame, textvariable=self.var_name, font=("Arial", 12), width=30
        )
        student_name_entry.grid(row=4, column=1, padx=10, pady=10, sticky="w")

        # students DOB
        student_dob_label = Label(
            left_frame,
            text="Student DOB",
            font=("Arial", 12, "bold"),
            bg=bg_color,
            fg="#4A4A4A",
        )
        student_dob_label.grid(row=5, column=0, padx=10, pady=10, sticky="w")

        student_dob_entry = ttk.Entry(
            left_frame, textvariable=self.var_dob, font=("Arial", 12), width=30
        )
        student_dob_entry.grid(row=5, column=1, padx=10, pady=10, sticky="w")

        # students email
        student_email_label = Label(
            left_frame,
            text="Student Email",
            font=("Arial", 12, "bold"),
            bg=bg_color,
            fg="#4A4A4A",
        )
        student_email_label.grid(row=6, column=0, padx=10, pady=10, sticky="w")

        student_email_entry = ttk.Entry(
            left_frame, textvariable=self.var_email, font=("Arial", 12), width=30
        )
        student_email_entry.grid(row=6, column=1, padx=10, pady=10, sticky="w")

        # students phone
        student_phone_label = Label(
            left_frame,
            text="Student Phone",
            font=("Arial", 12, "bold"),
            bg=bg_color,
            fg="#4A4A4A",
        )
        student_phone_label.grid(row=7, column=0, padx=10, pady=10, sticky="w")

        student_phone_entry = ttk.Entry(
            left_frame, textvariable=self.var_phone, font=("Arial", 12), width=30
        )
        student_phone_entry.grid(row=7, column=1, padx=10, pady=10, sticky="w")

        # students address
        student_address_label = Label(
            left_frame,
            text="Student Address",
            font=("Arial", 12, "bold"),
            bg=bg_color,
            fg="#4A4A4A",
        )
        student_address_label.grid(row=8, column=0, padx=10, pady=10, sticky="w")

        student_address_entry = ttk.Entry(
            left_frame, textvariable=self.var_address, font=("Arial", 12), width=30
        )
        student_address_entry.grid(row=8, column=1, padx=10, pady=10, sticky="w")

        # radio button
        radiobtn1 = ttk.Radiobutton(
            left_frame, variable=self.var_radio, text="take photo sample", value="Yes"
        )
        radiobtn1.grid(
            row=9,
            column=0,
            padx=10,
            pady=10,
        )

        radiobtn2 = ttk.Radiobutton(
            left_frame, variable=self.var_radio, text="No photo sample", value="No"
        )
        radiobtn2.grid(
            row=9,
            column=1,
            padx=10,
            pady=10,
        )

        # button
        save_btn = Button(
            left_frame,
            command=self.add_students,
            text="Save",
            width=10,
            font=("Arial", 12, "bold"),
            bg="#2196F3",
            fg="#FFFFFF",
            bd=0,
            cursor="hand2",
            padx=8,
            pady=6,
            highlightthickness=0,
        )
        save_btn.grid(row=10, column=0, padx=0, pady=10)

        update_btn = Button(
            left_frame,
            command=self.update_data,
            text="Update",
            width=10,
            font=("Arial", 12, "bold"),
            bg="#2196F3",
            fg="#FFFFFF",
            bd=0,
            cursor="hand2",
            padx=8,
            pady=6,
            highlightthickness=0,
        )
        update_btn.grid(row=10, column=0, padx=0, pady=10)
        update_btn.place(x=150, y=456)

        delete_btn = Button(
            left_frame,
            command=self.delete_data,
            text="Delete",
            width=10,
            font=("Arial", 12, "bold"),
            bg="#2196F3",
            fg="#FFFFFF",
            bd=0,
            cursor="hand2",
            padx=8,
            pady=6,
            highlightthickness=0,
        )
        delete_btn.grid(row=10, column=0, padx=0, pady=10)
        delete_btn.place(x=282, y=456)

        reset_btn = Button(
            left_frame,
            command=self.take_photo,
            text="Reset",
            width=10,
            font=("Arial", 12, "bold"),
            bg="#2196F3",
            fg="#FFFFFF",
            bd=0,
            cursor="hand2",
            padx=8,
            pady=6,
            highlightthickness=0,
        )
        reset_btn.grid(row=10, column=0, padx=0, pady=10)
        reset_btn.place(x=416, y=456)

        # right label frame
        right_frame = LabelFrame(
            body_frame,
            bd=2,
            relief=RIDGE,
            text="Students Details",
            font=("Arial", 12, "bold"),
            bg=bg_color,
            fg="#4A4A4A",
        )
        right_frame.place(x=630, y=10, width=750, height=575)

        # search by
        style = ttk.Style()
        style.configure(
            "Custom.TEntry",
            bordercolor="blue",
            borderwidth=2,
            relief="groove",
            padding=6,
            borderradius=12,
        )

        search_entry = ttk.Entry(
            right_frame, style="Custom.TEntry", font=("Arial", 12), width=40
        )
        search_entry.grid(row=7, column=1, padx=10, pady=10, sticky="w")
        search_entry.place(x=50, y=15)

        search_button = ttk.Button(
            right_frame, text="Search", style="Custom.TButton", cursor="hand2"
        )
        search_button.grid(row=7, column=1, padx=5)
        search_button.place(x=342, y=20)

        # sort by
        sort_by_combo = ttk.Combobox(
            right_frame, font=("Arial", 10), width=10, state="readonly"
        )
        sort_by_combo["values"] = ("Sort By:", "Name", "ID", "Course", "Year")
        sort_by_combo.current(0)
        sort_by_combo.grid(row=2, column=1, padx=10, pady=10, sticky="w")
        sort_by_combo.place(x=620, y=22)

        # table frame
        table_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=8, y=80, width=730, height=465)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(
            table_frame,
            column=(
                "id",
                "course",
                "year",
                "sem",
                "name",
                "dob",
                "email",
                "phone",
                "address",
                "photo sample",
            ),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("id", text="Students ID")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("dob", text="D.O.B")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("photo sample", text="Photo Sample")

        self.student_table["show"] = "headings"
        self.student_table.pack(fill=BOTH, expand=1)

        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    # Function to add student
    def add_students(self):
        if self.var_course.get() == "Select":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = get_connection()
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                        self.var_id.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_name.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_radio.get(),
                    ),
                )
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success", "Student has been added successfully", parent=self.root
                )
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    # fetch data
    def fetch_data(self):
        conn = get_connection()
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # get cursor
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        if len(data) >= 10:
            self.var_id.set(data[0])
            self.var_course.set(data[1])
            self.var_year.set(data[2])
            self.var_semester.set(data[3])
            self.var_name.set(data[4])
            self.var_dob.set(data[5])
            self.var_email.set(data[6])
            self.var_phone.set(data[7])
            self.var_address.set(data[8])
            self.var_radio.set(data[9])

    # update data
    def update_data(self):
        if self.var_course.get() == "Select":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                update = messagebox.askyesno(
                    "Update", "Do you want to update this student", parent=self.root
                )
                if update > 0:
                    conn = get_connection()
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "update student set course=%s, year=%s, semester=%s, name=%s, dob=%s, email=%s, phone=%s, address=%s, photo=%s where id=%s",
                        (
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_name.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_address.get(),
                            self.var_radio.get(),
                            self.var_id.get(),
                        ),
                    )
                else:
                    if not update:
                        return
                messagebox.showinfo(
                    "Success", "Student has been updated successfully", parent=self.root
                )
                conn.commit()
                self.fetch_data()
                conn.close()

            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    # delete data
    def delete_data(self):
        if self.var_id.get() == "":
            messagebox.showerror(
                "Error", "Student ID must be required", parent=self.root
            )
        else:
            try:
                delete = messagebox.askyesno(
                    "Student Delete",
                    "Do you want to delete this student",
                    parent=self.root,
                )
                if delete > 0:
                    conn = get_connection()
                    my_cursor = conn.cursor()
                    sql = "delete from student where id=%s"
                    val = (self.var_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return

                messagebox.showinfo(
                    "Success", "Student has been deleted successfully", parent=self.root
                )
                conn.commit()
                self.fetch_data()
                conn.close()

            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    # reset data
    def reset_data(self):
        self.var_id.set("")
        self.var_course.set("Select")
        self.var_year.set("Select")
        self.var_semester.set("Select")
        self.var_name.set("")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_radio.set("")

    # take photo
    face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    def take_photo(self):
        if self.var_course.get() == "Select":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = get_connection()
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = len(myresult)
                # id = 0  # added now
                for x in myresult:
                    if x[0] == id:
                        id += 1
                    # id += 1
                    my_cursor.execute(
                        "update student set course=%s, year=%s, semester=%s, name=%s, dob=%s, email=%s, phone=%s, address=%s, photo=%s where id=%s",
                        (
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_name.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_address.get(),
                            self.var_radio.get(),
                            self.var_id.set(id + 1),
                        ),
                    )
                    conn.commit()
                    self.fetch_data()
                    self.reset_data()
                    conn.close()

                    # load data from opencv
                    face_classifier = cv2.CascadeClassifier(
                        "haarcascade_frontalface_default.xml"
                    )

                    def face_cropped(img):
                        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                        faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                        for x, y, w, h in faces:
                            face_cropped = img[y : y + h, x : x + w]
                            return face_cropped

                    cap = cv2.VideoCapture(0)
                    img_id = 0
                    while True:
                        ret, my_frame = cap.read()
                        if face_cropped(my_frame) is not None:
                            img_id += 1
                            face = cv2.resize(face_cropped(my_frame), (450, 450))
                            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                            file_name_path = (
                                "data/user." + str(id) + "." + str(img_id) + ".jpg"
                            )
                            cv2.imwrite(file_name_path, face)
                            cv2.putText(
                                face,
                                str(img_id),
                                (50, 50),
                                cv2.FONT_HERSHEY_COMPLEX,
                                2,
                                (0, 255, 0),
                                2,
                            )
                            cv2.imshow("Cropped Face", face)

                        if cv2.waitKey(1) == 13 or int(img_id) == 100:
                            break

                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Result", "Generating data set completed!!!")
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Students(root)
    root.mainloop()
