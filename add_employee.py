import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import DateEntry
from db import get_connection
from style import apply_global_styles, center_window

def open_add_employee_window():
    add_win = tk.Toplevel()
    add_win.title("Add Employee")
    center_window(add_win, 400, 600)
    apply_global_styles(add_win)

    def field(label):
        ttk.Label(add_win, text=label).pack(pady=3)
        entry = ttk.Entry(add_win)
        entry.pack(padx=10, fill="x")
        return entry

    fullname_entry = field("Full Name")
    address_entry = field("Address")

    ttk.Label(add_win, text="Birthdate").pack(pady=3)
    birthdate_entry = DateEntry(add_win, date_pattern='yyyy-mm-dd')
    birthdate_entry.pack(padx=10, fill="x")

    age_entry = field("Age")

    ttk.Label(add_win, text="Gender").pack()
    gender_var = tk.StringVar()
    gender_frame = ttk.Frame(add_win)
    gender_frame.pack()
    for g in ["Male", "Female", "Other"]:
        ttk.Radiobutton(gender_frame, text=g, variable=gender_var, value=g).pack(side="left", padx=5)

    ttk.Label(add_win, text="Civil Status").pack()
    civilstat_combo = ttk.Combobox(add_win, values=["Single", "Married", "Separated", "Widowed"])
    civilstat_combo.pack(padx=10, fill="x")

    contact_entry = field("Contact No.")
    salary_entry = field("Salary")

    isactive_var = tk.IntVar()
    ttk.Checkbutton(add_win, text="Active", variable=isactive_var).pack(pady=5)

    def save_employee():
        try:
            conn = get_connection()
            cursor = conn.cursor()

            # Step 1: Insert employee without empcode
            cursor.execute('''
                INSERT INTO employeefile (
                    fullname, address, birthdate, age, gender,
                    civilstat, contactnum, salary, isactive
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            ''', (
                fullname_entry.get(),
                address_entry.get(),
                birthdate_entry.get_date(),
                int(age_entry.get()),
                gender_var.get(),
                civilstat_combo.get(),
                contact_entry.get(),
                float(salary_entry.get()),
                isactive_var.get()
            ))

            # Step 2: Generate empcode from last inserted recid
            recid = cursor.lastrowid
            empcode = f"EMP-{recid:03}"

            # Step 3: Update empcode for the same record
            cursor.execute("UPDATE employeefile SET empcode = %s WHERE recid = %s", (empcode, recid))

            conn.commit()
            conn.close()

            messagebox.showinfo("Success", f"Employee added.\nEmployee Code: {empcode}")
            add_win.destroy()

        except Exception as e:
            messagebox.showerror("Error", f"Failed to add employee:\n{e}")

    ttk.Button(add_win, text="Save", command=save_employee).pack(pady=10)
