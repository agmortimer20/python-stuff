from tkinter import *
from tkinter import ttk

root = Tk()

progressbar = ttk.Progressbar(root, orient=HORIZONTAL, length=200)
progressbar.pack()

# Determinant mode vs indeterminate mode
progressbar.config(mode='indeterminate')
progressbar.start()
progressbar.stop()

progressbar.config(mode='determinate', maximum=11.0, value=1)
progressbar.step()

value = DoubleVar()
progressbar.config(variable=value)

scale = ttk.Scale(root, orient=HORIZONTAL, length=400, variable=value, from_=0.0, to=11.0)
scale.pack()

root.mainloop()