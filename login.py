import tkinter as tk
from tkinter import messagebox, ttk
from auth import validate_login
from style import apply_global_styles, center_window

def show_login_screen():
    login_window = tk.Tk()
    login_window.title("Login")
    center_window(login_window, 300, 200)
    apply_global_styles(login_window)

    ttk.Label(login_window, text="Username").pack(pady=5)
    username_entry = ttk.Entry(login_window)
    username_entry.pack(padx=10, fill="x")

    ttk.Label(login_window, text="Password").pack(pady=5)
    password_entry = ttk.Entry(login_window, show='*')
    password_entry.pack(padx=10, fill="x")

    def login():
        from menu import show_main_menu  # 👈 Moved here to break circular import
        username = username_entry.get()
        password = password_entry.get()
        if validate_login(username, password):
            login_window.destroy()
            show_main_menu()
        else:
            messagebox.showerror("Login Failed", "Invalid credentials")

    ttk.Button(login_window, text="Login", command=login).pack(pady=10)
    login_window.mainloop()
