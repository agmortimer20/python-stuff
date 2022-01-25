from tkinter import *
from tkinter import ttk

def change_text():
    label_text.set("Clicked!")

root = Tk()

label_text = StringVar(value="No clickety")
label = ttk.Label(root, textvariable=label_text)
label.pack()

Button(text="Click me", command=change_text).pack()

root.mainloop()