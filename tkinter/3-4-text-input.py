from tkinter import *
from tkinter import ttk

print_content = lambda : print(entry.get())
clear_text = lambda : entry.delete(0, END)

root = Tk()
root.geometry("300x300")
entry = ttk.Entry(root, width=30)
entry.pack()

password = ttk.Entry(root, width=30, show="*")
password.pack()

button = ttk.Button(root, text="Get Message", command=clear_text)
button.pack()


root.mainloop()