from tkinter import *

root = Tk()
number = IntVar()

def increment():
    value = number.get() + 1
    number.set(value)


label = Label(root, textvariable=number).pack()
plus_button = Button(root, text="Increment", command=increment).pack()

root.mainloop()