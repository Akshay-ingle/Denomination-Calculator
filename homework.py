import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calculate_age():
    try:
        name = name_entry.get()
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())

        birth_date = datetime(year, month, day)
        today = datetime.now()
        age = today.year - birth_date.year

        # Adjust age if the birthday hasn't occurred yet this year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1

        result = f"Hello {name}! You are {age} years old."
        messagebox.showinfo("Age Result", result)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for date, month, and year.")

# Create the main window
root = tk.Tk()
root.title("Age Calculator App")
root.geometry("400x400")
root.configure(bg="#f0f8ff")  # Light blue background

# Title label
title_label = tk.Label(root, text="Age Calculator", font=("Helvetica", 18, "bold"), bg="#f0f8ff", fg="#333366")
title_label.pack(pady=10)

# Frame for form inputs
form_frame = tk.Frame(root, bg="#f0f8ff")
form_frame.pack(pady=20)

# Name
tk.Label(form_frame, text="Name:", font=("Arial", 12), bg="#f0f8ff").grid(row=0, column=0, padx=10, pady=5, sticky="e")
name_entry = tk.Entry(form_frame, width=25)
name_entry.grid(row=0, column=1, padx=10, pady=5)

# Day
tk.Label(form_frame, text="Day:", font=("Arial", 12), bg="#f0f8ff").grid(row=1, column=0, padx=10, pady=5, sticky="e")
day_entry = tk.Entry(form_frame, width=25)
day_entry.grid(row=1, column=1, padx=10, pady=5)

# Month
tk.Label(form_frame, text="Month:", font=("Arial", 12), bg="#f0f8ff").grid(row=2, column=0, padx=10, pady=5, sticky="e")
month_entry = tk.Entry(form_frame, width=25)
month_entry.grid(row=2, column=1, padx=10, pady=5)

# Year
tk.Label(form_frame, text="Year:", font=("Arial", 12), bg="#f0f8ff").grid(row=3, column=0, padx=10, pady=5, sticky="e")
year_entry = tk.Entry(form_frame, width=25)
year_entry.grid(row=3, column=1, padx=10, pady=5)

# Calculate Button
calc_btn = tk.Button(root, text="Calculate Age", command=calculate_age, font=("Arial", 12, "bold"),
                     bg="#3399ff", fg="white", padx=10, pady=5)
calc_btn.pack(pady=20)

# Run the application
root.mainloop()
