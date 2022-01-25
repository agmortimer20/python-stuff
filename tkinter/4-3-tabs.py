from tkinter import *
from tkinter import ttk

root = Tk()

notebook = ttk.Notebook(root)
notebook.pack()

f1 = ttk.Frame(notebook)
f2 = ttk.Frame(notebook)
notebook.add(f1, text="One")
notebook.add(f2, text="Two")

ttk.Button(f1, text="click me").pack()

f3 = ttk.Frame(notebook)
notebook.insert(1, f3, text="Three")

notebook.select(2) # select tab index 2
print(notebook.index(notebook.select())) # get selected tab
# notebook.tab(1, state='disabled') # or hidden or normal

root.mainloop()