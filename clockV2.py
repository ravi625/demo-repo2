# This is the second version of clock app made earlier in demo-repo

from time import strftime
from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Clock V2")
frm = ttk.Frame(root, padding=100)

frm.grid()
label = ttk.Label(frm, background="black", foreground="white")
label.grid(column=0, row=0)
button = ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=5)

def time():
    labeltext = strftime("%H:%M:%S %p")
    label.config(text=labeltext)
    label.after(1000,time)

time()

root.mainloop()