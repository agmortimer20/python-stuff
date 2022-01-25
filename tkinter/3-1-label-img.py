from tkinter import *
from tkinter import ttk
from tkinter import font

root = Tk()
label = ttk.Label(root, text="Hello Tkinter!")
label.pack()
label.config(text="Howdy!")
label.config(wraplength=150)
label.config(justify=CENTER)
label.config(foreground='blue', background='yellow')
label.config(font=("Courier", 18))

# logo = PhotoImage(file="C:\\Users\\amortimer.SEHSLT-47-21\\source\\repos\python-stuff\\tkinter\\python_logo.gif")
label.img = PhotoImage(file="C:\\Users\\amortimer.SEHSLT-47-21\\source\\repos\python-stuff\\tkinter\\python_logo.gif")
label.config(image=label.img)
label.config(compound="text")
label.config(compound="right")


root.mainloop()