import requests
import tkinter as tk
from tkinter import messagebox

def get_advise():
    try:
        response=requests.get("https://api.adviceslip.com/advice")
        response.raise_for_status()
        data=response.json()
        advice_message.set(data["slip"]["advice"])
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Unable to fetch advice:{e}")

app=tk.Tk()
app.title("Advice Generator")

advice_message=tk.StringVar()
message_label=tk.Label(app, textvariable=advice_message, wraplength=400, font=("Arial", 14))
fetch_button=tk.Button(app, text="Get Advice", command=get_advise)


message_label.pack(pady=20)
fetch_button.pack(pady=10)

get_advise()
app.mainloop()