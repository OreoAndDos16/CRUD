import tkinter as tk
from tkinter import ttk, messagebox
from add_employee import open_add_employee_window
from view_employees import open_view_employees_window
from style import apply_global_styles, center_window
from login import show_login_screen

def show_main_menu():
    root = tk.Tk()
    root.title("Employee Management System")
    center_window(root, 800, 500)
    apply_global_styles(root)
    root.configure(bg="#f2f2f2")

    # Menu Bar
    menubar = tk.Menu(root)
    root.config(menu=menubar)

    file_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Add Employee", command=open_add_employee_window)
    file_menu.add_command(label="View Employees", command=open_view_employees_window)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)

    help_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label="About", command=lambda: messagebox.showinfo("About", "Employee Management System\nBy You."))

    # Header
    ttk.Label(root, text="Welcome to the Employee Management System", font=("Segoe UI", 18, "bold")).pack(pady=20)

    # Navigation Buttons
    button_frame = ttk.Frame(root)
    button_frame.pack(pady=30)

    ttk.Button(button_frame, text="➕ Add Employee", width=30, command=open_add_employee_window).pack(pady=10)
    ttk.Button(button_frame, text="📄 View / Update / Delete Employees", width=30, command=open_view_employees_window).pack(pady=10)
    ttk.Button(button_frame, text="🚪 Logout / Exit", width=30, command=lambda: logout(root)).pack(pady=10)

    ttk.Label(root, text="Tip: You can also use the menu bar in the top-left corner.", font=("Segoe UI", 9, "italic")).pack(side="bottom", pady=10)

    root.mainloop()

def logout(window):
    window.destroy()
    from login import show_login_screen  # Moved here to avoid circular import
    show_login_screen()
