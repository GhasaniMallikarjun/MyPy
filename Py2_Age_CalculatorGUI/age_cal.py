import tkinter as tk
from  tkinter import ttk
from datetime import datetime

def calculate_age():
    try:
        birthdate=datetime.strptime(birthdate_entry.get(), "%Y-%m-%d")
        future_date=datetime.strptime(future_date_entry.get(), "%Y-%m-%d")
        age=future_date-birthdate
        result_label.config(text=f"Age: {age.days//365} years, {age.days%365} days")
    except ValueError:
        result_label.config(text="Please enter valid dates in YYYY-MM-DD format.")

root=tk.Tk()

root.title("Age Calculator")

ttk.Label(root,text="Date of Birth (YYYY-MM-DD):").grid(column=0, row=0, padx=10, pady=5)
birthdate_entry=ttk.Entry(root)
birthdate_entry.grid(column=1, row=0, padx=10, pady=5)


current_date=datetime.now().strftime("%Y-%m-%d")


ttk.Label(root, text="Age at the Date of (YYYY-MM-DD):").grid(column=0, row=1, padx=10, pady=5)
future_date_entry=ttk.Entry(root)
future_date_entry.grid(column=1, row=1, padx=10, pady=5)
future_date_entry.insert(0, current_date)


calculate_button=ttk.Button(root, text="Calculate", command=calculate_age)
calculate_button.grid(column=0, row=3, columnspan=2, pady=10)

result_label=ttk.Label(root, text="")
result_label.grid(column=0, row=3, columnspan=2, pady=5)

root.mainloop()



