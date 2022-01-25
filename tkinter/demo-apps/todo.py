from tkinter import *
from tkinter import ttk


root = Tk()

def addTodo():
    newTodo = Label(todoList, text=f"✅{entry.get()}")
    newTodo.pack()
    entry.delete(0, END)

todoList = Frame(root, width=15, height=15, padx=15, pady=15, bg="blue")
todoList.pack()

entry = Entry(root)
entry.pack()

button = Button(root, text="+ Add Todo", command=addTodo)
button.pack()

root.mainloop()