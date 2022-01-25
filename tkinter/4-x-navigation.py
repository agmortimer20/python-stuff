from tkinter import *
from tkinter import ttk


root = Tk()

def navigate1():
    page1.pack_forget()
    page2.pack()


page1 = ttk.Frame(root)
page1.pack()
ttk.Label(page1, text="Page1").pack()

page2 = ttk.Frame(root)
ttk.Label(page2, text="Page2").pack()

button = ttk.Button(root, text="Switch Frames", command=navigate1)
button.pack()

root.mainloop()