from tkinter import *
from tkinter import ttk

root = Tk()
entree = StringVar()

entree1 = ttk.Radiobutton(root, text="Fish", variable=entree, value="fish")
entree1.pack()

entree2 = ttk.Radiobutton(root, text="Chicken", variable=entree, value="chicken")
entree2.pack()

entree3 = ttk.Radiobutton(root, text="Wagyu", variable=entree, value="wagyu")
entree3.pack()

root.mainloop()