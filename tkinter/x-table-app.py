from tkinter import *

root = Tk()

data = ["apple", "banana", "cherry", "date", "elderberry"]

for item in data:
    Label(text=item).pack()


root.mainloop()