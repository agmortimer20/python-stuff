# 3:28

from tkinter import *
from tkinter import ttk

def mouse_press(event):
    canvas.config(background="green")

def mouse_release(event):
    canvas.config(background="white")

root = Tk()

canvas = Canvas(root, width=640, height=480, background='white')
canvas.pack()

canvas.bind('<ButtonPress>', mouse_press)
canvas.bind('<ButtonRelease>', mouse_release)

root.mainloop()