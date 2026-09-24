import tkinter as tk
from tkinter import messagebox

accounts = {}

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "" or password == "":
        messagebox.showerror("Login Error", "Please enter a username and password.")
    elif username in accounts and accounts[username] == password:
        messagebox.showinfo("Login", "Login successful!")
    else:
        messagebox.showerror("Login Error", "Incorrect username or password.")

def create_account():
    account_window = tk.Toplevel(window)
    account_window.title("Create Account")
    account_window.geometry("400x300")

    title = tk.Label(account_window, text="Create Account", font=("Arial", 18, "bold"))
    title.pack(pady=20)

    new_username_label = tk.Label(account_window, text="Username:")
    new_username_label.pack()

    new_username_entry = tk.Entry(account_window, width=30)
    new_username_entry.pack(pady=5)

    new_password_label = tk.Label(account_window, text="Password:")
    new_password_label.pack()

    new_password_entry = tk.Entry(account_window, width=30, show="*")
    new_password_entry.pack(pady=5)
    
    def save_account():
        username = new_username_entry.get()
        password = new_password_entry.get()

        if username == "" or password == "":
            messagebox.showerror("Error", "Please enter a username and password.")

        else:
             accounts[username] = password
             messagebox.showinfo("Account Created", "Your account was created successfully.")

    create_button = tk.Button(account_window, text="Create", width=15, command=save_account)
    create_button.pack(pady=10)

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
