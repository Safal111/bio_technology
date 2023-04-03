import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class StudentManagementSystem:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Student Management System")
        self.bg_color = "#FFFFFF"
        self.root.config(bg=self.bg_color)
        self.var_name = tk.StringVar()

        # create a button to open the popup
        add_button = tk.Button(
            self.root,
            text="Add Student",
            command=self.popup,
            font=("Arial", 12),
            bg="#4A4A4A",
            fg="#FFFFFF",
        )
        add_button.place(x=50, y=80)

        self.root.mainloop()

    def add_student(self):
        # code to add student to your database or list
        messagebox.showinfo("Success", "Student added successfully!")
        popup_window.destroy()

    def popup(self):
        global popup_window
        popup_window = tk.Toplevel()
        popup_window.title("Add Student")
        popup_window.config(bg=self.bg_color)
        bg_color = "#F9F9F9"
        popup_window_width = 500
        popup_window_height = 500
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
            values=[
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
            values=["1", "2", "3", "4"],
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
            values=["1", "2"],
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
            popup_window, textvariable=self.var_name, font=("Arial", 12), width=32
        )
        id_entry.grid(row=4, column=1, padx=20, pady=10, sticky="w")

        # student name
        tk.Label(
            popup_window,
            text="Student Name",
            font=("Arial", 12, "bold"),
            background="white",
        ).grid(row=5, column=0, padx=20, pady=10, sticky="w")
        name_entry = ttk.Entry(
            popup_window, textvariable=self.var_name, font=("Arial", 12), width=32
        )
        name_entry.grid(row=5, column=1, padx=20, pady=10, sticky="w")

        # date of birth
        tk.Label(
            popup_window,
            text="Date of Birth",
            font=("Arial", 12, "bold"),
            background="white",
        ).grid(row=6, column=0, padx=20, pady=10, sticky="w")
        dob_entry = ttk.Entry(
            popup_window, textvariable=self.var_name, font=("Arial", 12), width=32
        )
        dob_entry.grid(row=6, column=1, padx=20, pady=10, sticky="w")

        # email
        tk.label(
            popup_window,
            text="Student Email",
            font=("Arial", 12, "bold"),
            background="white",
        ).grid(row=7, column=0, padx=20, pady=10, sticky="w")
        email_entry = ttk.Entry(
            popup_window, textvariable=self.var_name, font=("Arial", 12), width=32
        )
        email_entry.grid(row=7, column=1, padx=20, pady=10, sticky="w")

        # phone
        tk.label(
            popup_window,
            text="Student Phone",
            font=("Arial", 12, "bold"),
            background="white",
        ).grid(row=8, column=0, padx=20, pady=10, sticky="w")
        phone_entry = ttk.Entry(
            popup_window, textvariable=self.var_name, font=("Arial", 12), width=32
        )
        phone_entry.grid(row=8, column=1, padx=20, pady=10, sticky="w")

        # address
        tk.Label(
            popup_window,
            text="Address",
            font=("Arial", 12, "bold"),
            background="white",
        ).grid(row=9, column=0, padx=20, pady=10, sticky="w")
        address_entry = ttk.Entry(
            popup_window, textvariable=self.var_name, font=("Arial", 12), width=32
        )
        address_entry.grid(row=9, column=1, padx=20, pady=10, sticky="w")

        # create a button to add the student
        add_button = tk.Button(
            popup_window,
            text="Add Student",
            command=self.add_student,
            font=("Arial", 12),
            bg="#4A4A4A",
            fg="#FFFFFF",
        )
        add_button.grid(row=11, column=0, columnspan=2, padx=10, pady=10)

        popup_window.mainloop()


if __name__ == "__main__":
    StudentManagementSystem()
