from tkinter import *
from tkinter import ttk

def callback(num):
    print("In the callback")


root = Tk()

ttk.Button(root, text="Click me 1", command=callback).pack()
ttk.Button(root, text="Click me 1", command=callback).pack()
ttk.Button(root, text="Click me 1", command=callback).pack()

root.mainloop()

# Widgets with command callbacks
# Button, check, radio, spinbox, scale, scrollbar 