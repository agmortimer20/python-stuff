from tkinter import *
from tkinter import ttk

root = Tk()

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=3)
root.columnconfigure(0, weight=1)
# root.columnconfigure()

ttk.Label(root, text="Yellow", background="Yellow").grid(
    row=0, column=2, rowspan=2, stick="nsew"
)
ttk.Label(root, text="Blue", background="Blue").grid(
    row=1, column=0, columnspan=2, stick="nsew"
)
ttk.Label(root, text="Green", background="Green").grid(
    row=0, column=0, stick="nsew"
)
ttk.Label(root, text="Orange", background="Orange").grid(
    row=0, column=1, stick="nsew"
)


root.mainloop()
