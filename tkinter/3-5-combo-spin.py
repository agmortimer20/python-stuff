from tkinter import *
from tkinter import ttk

root = Tk()
month = StringVar()

combobox = ttk.Combobox(root, textvariable=month)
combobox.pack()
combobox.config(values=[
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
])

year = StringVar()
spinbox = ttk.Spinbox(root, from_=1990, to=2021, textvariable=year)
spinbox.pack()

root.mainloop()