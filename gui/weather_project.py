import tkinter as tk
from tkinter import messagebox

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "" or password == "":
        messagebox.showerror("Login Error", "Please enter a username and password.")
    else:
        messagebox.showinfo("Login", "Login successful.")

def create_account():
    messagebox.showinfo("Create Account", "Account creation will open here.")

def cancel():
    window.destroy()

window = tk.Tk()
window.title("Weather Data Login")
window.geometry("400x300")

title_label = tk.Label(window, text="Weather Data", font=("Arial", 20, "bold"))
title_label.pack(pady=20)

username_label = tk.Label(window, text="Username:")
username_label.pack()

username_entry = tk.Entry(window, width=30)
username_entry.pack(pady=5)

password_label = tk.Label(window, text="Password:")
password_label.pack()

password_entry = tk.Entry(window, width=30, show="*")
password_entry.pack(pady=5)

login_button = tk.Button(window, text="Login", width=15, command=login)
login_button.pack(pady=5)

create_button = tk.Button(window, text="Create Account", width=15, command=create_account)
create_button.pack(pady=5)

cancel_button = tk.Button(window, text="Cancel", width=15, command=cancel)
cancel_button.pack(pady=5)

window.mainloop()
