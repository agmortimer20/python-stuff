from tkinter import *
from tkinter import ttk

def render_text(*args):
    label.config(text=f"Slider value: {round(slider.get())}")

root = Tk()
slider = ttk.Scale(root, from_=0, to=10, orient=HORIZONTAL, command=render_text)
slider.pack()
label = ttk.Label(root, text=f"Slider value: {round(slider.get())}")
label.pack()

root.mainloop()