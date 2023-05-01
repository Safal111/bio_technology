from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from db import get_connection


class Students:
    def open_add_student_popup(self):
        self.bg_color = "white"
        global popup_window
        popup_window = tk.Toplevel()
        popup_window.title("Add Student")
        popup_window.config(bg=self.bg_color)
        bg_color = "#F9F9F9"
        popup_window_width = 500
        popup_window_height = 600
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = int((screen_width / 2) - (popup_window_width / 2))
        y = int((screen_height / 2) - (popup_window_height / 2))
        popup_window.geometry(f"{popup_window_width}x{popup_window_height}+{x}+{y}")

        # course
        ttk.Label(
            popup_window,
            text="Select course:",
            font=("Open Sans", 13, "bold"),
            foreground="#333",
            background="#fff",
        ).grid(row=1, column=0, padx=20, pady=10, sticky="w")

        course_combo = ttk.Combobox(
            popup_window,
            textvariable=self.var_course,
            values=[
                "Select Course",
                "Information Technology",
                "Business Administration",
                "Hotel Management",
            ],
            font=("Open Sans", 12),
            width=30,
            state="readonly",
        )
        course_combo.grid(row=1, column=1, padx=20, pady=10, sticky="w")
        course_combo.current(0)

        # year
        ttk.Label(
            popup_window, text="Year", font=("Arial", 12, "bold"), background="white"
        ).grid(row=2, column=0, padx=20, pady=10, sticky="w")

        year_combo = ttk.Combobox(
            popup_window,
            textvariable=self.var_year,
            values=["Select Year", "1", "2", "3", "4"],
            font=("Arial", 12),
            width=30,
            state="readonly",
        )
        year_combo.grid(row=2, column=1, padx=20, pady=10, sticky="w")
        year_combo.current(0)

        # semester
        ttk.Label(
            popup_window,
            text="Semester",
            font=("Arial", 12, "bold"),
            background="white",
        ).grid(row=3, column=0, padx=20, pady=10, sticky="w")

        semester_combo = ttk.Combobox(
            popup_window,
            textvariable=self.var_semester,
            values=[
                "Select Semester",
                "1st",
                "2nd",
                "3rd",
                "4th",
                "5th",
                "6th",
                "7th",
                "8th",
            ],
            font=("Arial", 12),
            width=30,
            state="readonly",
        )
        semester_combo.grid(row=3, column=1, padx=20, pady=10, sticky="w")
        semester_combo.current(0)

        # student id
        tk.Label(
            popup_window,
            text="Student ID",
            font=("Arial", 12, "bold"),
            background="white",
        ).grid(row=4, column=0, padx=20, pady=10, sticky="w")
        id_entry = ttk.Entry(
            popup_window, textvariable=self.var_id, font=("Arial", 12), width=32
        )
        id_entry.grid(row=4, column=1, padx=20, pady=10, sticky="w")

        # students name
        tk.Label(
            popup_window,
            text="Student Name",
            font=("Arial", 12, "bold"),
            background="white",
        ).grid(row=5, column=0, padx=20, pady=10, sticky="w")
        id_entry = ttk.Entry(
            popup_window, textvariable=self.var_name, font=("Arial", 12), width=32
        )
        id_entry.grid(row=5, column=1, padx=20, pady=10, sticky="w")

        # students dob
        tk.Label(
            popup_window,
            text="Date of Birth",
            font=("Arial", 12, "bold"),
            background="white",
        ).grid(row=6, column=0, padx=20, pady=10, sticky="w")
        id_entry = ttk.Entry(
            popup_window, textvariable=self.var_dob, font=("Arial", 12), width=32
        )
        id_entry.grid(row=6, column=1, padx=20, pady=10, sticky="w")

        # students email
        tk.Label(
            popup_window,
            text="Email",
            font=("Arial", 12, "bold"),
            background="white",
        ).grid(row=7, column=0, padx=20, pady=10, sticky="w")
        id_entry = ttk.Entry(
            popup_window, textvariable=self.var_email, font=("Arial", 12), width=32
        )
        id_entry.grid(row=7, column=1, padx=20, pady=10, sticky="w")

        # students phone
        tk.Label(
            popup_window,
            text="Phone",
            font=("Arial", 12, "bold"),
            background="white",
        ).grid(row=8, column=0, padx=20, pady=10, sticky="w")
        id_entry = ttk.Entry(
            popup_window, textvariable=self.var_phone, font=("Arial", 12), width=32
        )
        id_entry.grid(row=8, column=1, padx=20, pady=10, sticky="w")

        # students address
        tk.Label(
            popup_window,
            text="Address",
            font=("Arial", 12, "bold"),
            background="white",
        ).grid(row=9, column=0, padx=20, pady=10, sticky="w")
        id_entry = ttk.Entry(
            popup_window, textvariable=self.var_address, font=("Arial", 12), width=32
        )
        id_entry.grid(row=9, column=1, padx=20, pady=10, sticky="w")

        radiobtn1 = ttk.Radiobutton(
            popup_window, variable=self.var_radio, text="take photo sample", value="Yes"
        )
        radiobtn1.grid(row=10, column=0, padx=20, pady=10, sticky="w")

        radiobtn2 = ttk.Radiobutton(
            popup_window, variable=self.var_radio, text="No photo sample", value="No"
        )
        radiobtn2.grid(row=10, column=1, padx=20, pady=10, sticky="w")

        # create a button to add the student
        add_button = tk.Button(
            popup_window,
            text="Add Student",
            font=("Arial", 12),
            bg="#4A4A4A",
            fg="#FFFFFF",
            command=self.add_students,
        )
        add_button.grid(row=11, column=0, columnspan=2, padx=10, pady=10)

        popup_window.mainloop()

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

        # students detail frame
        students_detail_frame = LabelFrame(
            body_frame,
            bd=2,
            relief=RIDGE,
            text="Students Details",
            font=("Arial", 12, "bold"),
            bg=bg_color,
            fg="#4A4A4A",
        )
        students_detail_frame.place(x=30, y=10, width=1340, height=555)

        # Add Students Button
        add_students_btn = Button(
            students_detail_frame,
            text="Add Students",
            width=15,
            font=("Arial", 12, "bold"),
            bg="#0d6efd",
            fg="white",
            bd=0,
            cursor="hand2",
            padx=8,
            pady=6,
            highlightthickness=0,
            command=self.open_add_student_popup,
        )
        add_students_btn.grid(row=7, column=1, padx=5)
        add_students_btn.place(x=1100, y=20)

        # table frame
        table_frame = Frame(students_detail_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=10, y=80, width=1315, height=445)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        style = ttk.Style()
        style.configure("myStyle.Treeview", rowheight=30)

        self.student_table = ttk.Treeview(
            table_frame,
            style="myStyle.Treeview",
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
                "action",
            ),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("id", text="Students ID")
        self.student_table.column("id", width=60)

        self.student_table.heading("course", text="Course")
        self.student_table.column("course", width=120)

        self.student_table.heading("year", text="Year")
        self.student_table.column("year", width=50)

        self.student_table.heading("sem", text="Semester")
        self.student_table.column("sem", width=50)

        self.student_table.heading("name", text="Name")
        self.student_table.column("name", width=120)

        self.student_table.heading("dob", text="D.O.B")
        self.student_table.column("dob", width=60)

        self.student_table.heading("email", text="Email")
        self.student_table.column("email", width=160)

        self.student_table.heading("phone", text="Phone")
        self.student_table.column("phone", width=60)

        self.student_table.heading("address", text="Address")
        self.student_table.column("address", width=100)

        self.student_table.heading("photo sample", text="Photo Sample")
        self.student_table.column("photo sample", width=60)

        self.student_table.heading("action", text="Action")
        self.student_table.column("action", width=40)

        self.student_table["show"] = "headings"
        self.student_table.pack(fill=BOTH, expand=1)

        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    # Function Declaration to add students
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
                # print(self.var_name),
                print(self.var_name.get()),
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success", "Student has been added successfully", parent=self.root
                )
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

            popup_window.destroy()

    # fetch data from database
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
    def get_cursor(self, event):
        # Get the selected row
        selected_item = self.student_table.focus()

        # Get the values of the selected row
        values = self.student_table.item(selected_item)["values"]

        # Create a new popup window
        popup_window = tk.Toplevel()
        popup_window.title("Selected Row")
        screen_width = popup_window.winfo_screenwidth()
        screen_height = popup_window.winfo_screenheight()
        popup_width = 350
        popup_height = 450
        x = int((screen_width - popup_width) / 2)
        y = int((screen_height - popup_height) / 2) - 100
        popup_window.geometry(f"{popup_width}x{popup_height}+{x}+{y}")

        # Create labels to display the values
        entries = []
        for i, value in enumerate(values):
            entry = tk.Entry(popup_window, width=40)
            entry.grid(row=i, column=1, padx=10, pady=5, sticky="w")
            entry.insert(0, value)
            entries.append(entry)

        # self.var_id.set(entries[0].get())
        self.var_id.set(values[0])

        # Add headers to the popup window
        headers = [
            "ID",
            "Course",
            "Year",
            "Semester",
            "Name",
            "DOB",
            "Email",
            "Phone",
            "Address",
            "Gender",
        ]
        for i, header in enumerate(headers):
            header_label = tk.Label(popup_window, text=header, font=("bold", 10))
            header_label.grid(row=i, column=0, padx=10, pady=5, sticky="w")

        # Add a button to close the popup window

        update_button = tk.Button(
            popup_window,
            text="Update",
            font=("Arial", 10, "bold"),
            bg="#0d6efd",
            fg="white",
            bd=0,
            cursor="hand2",
            padx=16,
            pady=6,
            highlightthickness=0,
            command=lambda: self.update_data(popup_window),
        )
        update_button.grid(row=len(headers), column=0, padx=10, pady=10)
        update_button.place(x=20, y=340)

        delete_button = tk.Button(
            popup_window,
            text="Delete",
            font=("Arial", 10, "bold"),
            bg="#d9534f",
            fg="white",
            bd=0,
            cursor="hand2",
            padx=16,
            pady=6,
            highlightthickness=0,
            command=lambda: self.delete_data(popup_window),
        )
        delete_button.grid(row=len(headers), column=0, padx=10, pady=10)
        delete_button.place(x=120, y=340)

    # update data
    def update_data(self, popup_window):
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

                    selected_item = self.student_table.focus()
                    print("selected_item:", selected_item)
                    values = self.student_table.item(selected_item)["values"]
                    print(values)
                    student_id = values[0]
                    print("Selected student ID:", student_id)

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
                    print("name:", self.var_name.get())
                else:
                    if not update:
                        return
                messagebox.showinfo(
                    "Success", "Student has been updated successfully", parent=self.root
                )
                conn.commit()
                self.fetch_data()
                conn.close()
                my_cursor.close()

            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

            popup_window.destroy()

    # delete students function
    def delete_data(self, popup_window):
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

            popup_window.destroy()


if __name__ == "__main__":
    root = Tk()
    obj = Students(root)
    root.mainloop()
