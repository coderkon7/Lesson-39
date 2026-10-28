from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Virus Scanner")
root.geometry("200x200")

def msg():
    messagebox.showwarning("Alert", "A virus was detected. Take action immediately")

button = Button(root, text="Scan for Virus", command=msg)
button.place(x=40, y=80)

root.mainloop()