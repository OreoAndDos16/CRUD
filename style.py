import tkinter as tk
from tkinter import ttk

def apply_global_styles(root):
    style = ttk.Style(root)
    style.theme_use("clam")
    root.configure(bg="#f2f2f2")

    # Treeview styling
    style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"), background="#00aaff", foreground="white")
    style.configure("Treeview", font=("Segoe UI", 10), rowheight=25, background="white", fieldbackground="white")
    style.map("Treeview", background=[("selected", "#dfe6e9")])

    # Button styling
    style.configure("TButton", font=("Segoe UI", 10, "bold"), padding=8, background="#00b894", foreground="white")
    style.map("TButton", background=[("active", "#00cec9")])

    # Label styling
    style.configure("TLabel", background="#f2f2f2", font=("Segoe UI", 10))

    # Entry styling
    style.configure("TEntry", padding=5)

def center_window(win, width=500, height=400):
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))
    win.geometry(f"{width}x{height}+{x}+{y}")
