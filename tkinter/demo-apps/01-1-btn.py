from tkinter import *
from tkinter import ttk

click_count = 0

def show_message():
    global click_count
    click_count += 1

    if click_count >= 3:
        button.config(text="Okay, calm down...")
    else:
        button.config(text="Hey buddy!")

root = Tk()

button = ttk.Button(root, text="Click me", command=show_message)
button.pack()


root.mainloop()