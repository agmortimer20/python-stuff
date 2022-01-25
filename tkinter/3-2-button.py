from tkinter import *
from tkinter import ttk

def callback():
    print('clicked!')

root = Tk()
button = ttk.Button(root, text="Click Me")
button.pack()
button.config(command=callback)
button.img = PhotoImage(file="C:\\Users\\amortimer.SEHSLT-47-21\\source\\repos\python-stuff\\tkinter\\python_logo.gif")
button.config(image=button.img)
button.config(compound="text")
button.config(compound="left")

# button.invoke() # Programmatically invoke button
button.state(['disabled']) # Disable
# button.state(['!disabled']) # Enable
# print(button.instate(['!disabled']))
root.mainloop()