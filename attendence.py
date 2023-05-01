from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import csv
from tkinter import filedialog
import os

mydata = []


class Attendence:
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
            text="Attendance Sheet",
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
            text="Attendance Details",
            font=("Arial", 12, "bold"),
            bg=bg_color,
            fg="#4A4A4A",
        )
        students_detail_frame.place(x=30, y=10, width=1340, height=555)

        # import csv Button
        import_csv_btn = Button(
            students_detail_frame,
            text="Import CSV",
            width=12,
            font=("Arial", 11, "bold"),
            bg="#0d6efd",
            fg="white",
            bd=0,
            cursor="hand2",
            padx=8,
            pady=6,
            highlightthickness=0,
            command=self.importCsv,
        )
        import_csv_btn.grid(row=7, column=1, padx=5)
        import_csv_btn.place(x=1000, y=20)

        # Export csv Button
        export_csv_btn = Button(
            students_detail_frame,
            text="Export CSV",
            width=12,
            font=("Arial", 11, "bold"),
            bg="#0d6efd",
            fg="white",
            bd=0,
            cursor="hand2",
            padx=8,
            pady=6,
            highlightthickness=0,
            command=self.exportCsv,
        )
        export_csv_btn.grid(row=7, column=1, padx=5)
        export_csv_btn.place(x=1150, y=20)

        # table frame
        table_frame = Frame(students_detail_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=10, y=80, width=1315, height=445)

        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        style = ttk.Style()
        style.configure("myStyle.Treeview", rowheight=30)

        self.student_table = ttk.Treeview(
            table_frame,
            style="myStyle.Treeview",
            column=(
                "id",
                "name",
                "course",
                "sem",
                "email",
                "time",
                "date",
                "attendance status",
            ),
            yscrollcommand=scroll_y.set,
        )

        # Configure column widths
        self.student_table.column("id", width=100, anchor="center")
        self.student_table.column("name", width=200, anchor="center")
        self.student_table.column("course", width=100, anchor="center")
        self.student_table.column("sem", width=100, anchor="w")
        self.student_table.column("email", width=200, anchor="w")
        self.student_table.column("time", width=100, anchor="center")
        self.student_table.column("date", width=100, anchor="center")
        self.student_table.column("attendance status", width=200, anchor="w")

        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("id", text="Students ID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("time", text="Time")
        self.student_table.heading("date", text="Date")
        self.student_table.heading("attendance status", text="Attendance status")

        self.student_table["show"] = "headings"
        self.student_table.pack(fill=BOTH, expand=1)

    # Function to fetch data
    def fetchData(self, rows):
        self.student_table.delete(*self.student_table.get_children())
        for i in rows:
            self.student_table.insert("", END, values=i)

    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Open CSV",
            filetypes=(("CSV File", "*.csv"), ("All File", "*.*")),
            parent=self.root,
        )
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
        self.fetchData(mydata)

    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror(
                    "No Data", "No Data Found to Export", parent=self.root
                )
                return False
            fln = filedialog.asksaveasfilename(
                initialdir=os.getcwd(),
                title="Save CSV",
                filetypes=(("CSV File", "*.csv"), ("All File", "*.*")),
                parent=self.root,
            )
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo(
                    "Data Exported",
                    "Your Data Exported to " + os.path.basename(fln) + " successfully",
                    parent=self.root,
                )
        except Exception as es:
            messagebox.showerror("Error", f"Due To : {str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Attendence(root)
    root.mainloop()
