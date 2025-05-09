import tkinter as tk
from tkinter import messagebox

def check_strength():
    password = entry.get()
    length = len(password)
    
    if length == 0:
        result_label.config(text="Please enter a password.", fg="red")
    elif length < 6:
        result_label.config(text="Password Strength: Weak", fg="red")
    elif 6 <= length <= 10:
        result_label.config(text="Password Strength: Medium", fg="orange")
    else:
        result_label.config(text="Password Strength: Strong", fg="green")

# Create the main application window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x200")
root.resizable(False, False)

# Create and place the widgets
title_label = tk.Label(root, text="Enter Your Password", font=("Arial", 14))
title_label.pack(pady=10)

entry = tk.Entry(root, show="*", width=30, font=("Arial", 12))
entry.pack(pady=5)

check_button = tk.Button(root, text="Check Strength", command=check_strength, font=("Arial", 12))
check_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=5)

# Run the application
root.mainloop()
