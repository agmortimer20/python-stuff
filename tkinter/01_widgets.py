from tkinter import *
from tkinter import ttk

def say_hello():
    button.config(text="Hello!")

root = Tk()
button = ttk.Button(root, text='Click Me', command=say_hello)
button.pack()
ttk.Label(root, text="Hello TKinter!").pack()
# button.config(text = "Hi")

root.mainloop()