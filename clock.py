from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Clock By GGP")

def time():
    string = strftime('%I:%M:%S')
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=("ds-digital", 80), background = "black", foreground = "hot pink")
label.pack(anchor='center')
time()

mainloop()
