import tkinter as tk
import time
from tkinter import font as tkfont

def update_time():
    current_time=time.strftime("%I:%M:%S %p")
    time_label.config(text=current_time)
    time_label.after(1000, update_time)

root=tk.Tk()
root.title("Digital clock")
root.geometry("800x200")
root.configure(bg='purple')

custom_font=tkfont.Font(family="DS-Digital", size=120, weight="bold")


time_label=tk.Label(root, font=custom_font, background='#0C359E', foreground='white')
time_label.pack(expand=True, fill='both')

update_time()
root.mainloop()