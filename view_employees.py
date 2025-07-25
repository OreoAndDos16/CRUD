import tkinter as tk
from tkinter import ttk, messagebox
from db import get_connection
from style import apply_global_styles, center_window

def open_view_employees_window():
    win = tk.Toplevel()
    win.title("View Employees")
    center_window(win, 900, 500)
    apply_global_styles(win)
    win.configure(bg="#f2f2f2")

    search_var = tk.StringVar()

    # Treeview
    tree = ttk.Treeview(win, columns=("RecID", "EmpCode", "Name", "Contact", "Salary"), show="headings")
    for col in tree["columns"]:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=160)
    tree.pack(fill="both", expand=True, pady=10)

    def search():
        keyword = search_var.get().lower()
        for row in tree.get_children():
            tree.delete(row)

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT recid, fullname, contactnum, salary FROM employeefile")
        for row in cursor.fetchall():
            recid = row[0]
            empcode = f"{recid:03}"  # Format recid to 3-digit empcode
            fullname = row[1]
            contact = row[2]
            salary = row[3]
            if keyword in fullname.lower():
                tree.insert("", "end", values=(recid, empcode, fullname, contact, salary))
        conn.close()

    def load_data():
        for row in tree.get_children():
            tree.delete(row)
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT recid, fullname, contactnum, salary FROM employeefile")
        for row in cursor.fetchall():
            recid = row[0]
            empcode = f"{recid:03}"  # Format recid to 3-digit empcode
            fullname = row[1]
            contact = row[2]
            salary = row[3]
            tree.insert("", "end", values=(recid, empcode, fullname, contact, salary))
        conn.close()

    def delete_selected():
        selected = tree.selection()
        if not selected:
            messagebox.showwarning("No selection", "Select a record to delete.")
            return
        item = tree.item(selected[0])
        recid = item["values"][0]
        if messagebox.askyesno("Confirm", "Delete this employee?"):
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM employeefile WHERE recid = %s", (recid,))
            conn.commit()
            conn.close()
            load_data()
            messagebox.showinfo("Deleted", "Employee deleted.")

    def update_selected():
        selected = tree.selection()
        if not selected:
            messagebox.showwarning("No selection", "Select a record to update.")
            return
        item = tree.item(selected[0])
        recid = item["values"][0]

        update_win = tk.Toplevel()
        update_win.title("Update Employee")
        center_window(update_win, 400, 300)
        apply_global_styles(update_win)
        update_win.configure(bg="#f2f2f2")

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT fullname, contactnum, salary FROM employeefile WHERE recid = %s", (recid,))
        row = cursor.fetchone()
        conn.close()

        def field(label, value):
            ttk.Label(update_win, text=label).pack(pady=3)
            e = ttk.Entry(update_win)
            e.insert(0, value)
            e.pack(padx=10, fill="x")
            return e

        fullname_entry = field("Full Name", row[0])
        contact_entry = field("Contact No", row[1])
        salary_entry = field("Salary", row[2])

        def save_update():
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE employeefile
                SET fullname = %s, contactnum = %s, salary = %s
                WHERE recid = %s
            """, (
                fullname_entry.get(),
                contact_entry.get(),
                float(salary_entry.get()),
                recid
            ))
            conn.commit()
            conn.close()
            update_win.destroy()
            load_data()
            messagebox.showinfo("Updated", "Employee updated.")

        ttk.Button(update_win, text="Save Changes", command=save_update).pack(pady=10)

    # Search bar
    search_frame = ttk.Frame(win)
    search_frame.pack(pady=10)
    ttk.Entry(search_frame, textvariable=search_var, width=40).grid(row=0, column=0, padx=5)
    ttk.Button(search_frame, text="🔍 Search", command=search).grid(row=0, column=1)

    # Action Buttons
    btn_frame = ttk.Frame(win)
    btn_frame.pack(pady=5)
    ttk.Button(btn_frame, text="Update Selected", command=update_selected).grid(row=0, column=0, padx=5)
    ttk.Button(btn_frame, text="Delete Selected", command=delete_selected).grid(row=0, column=1, padx=5)
    ttk.Button(btn_frame, text="Refresh", command=load_data).grid(row=0, column=2, padx=5)

    load_data()
