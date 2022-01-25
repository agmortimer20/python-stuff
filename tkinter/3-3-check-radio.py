from tkinter import *
from tkinter import ttk
root = Tk()

def get_check():
    print(is_spam.get())

is_spam = BooleanVar()
check = ttk.Checkbutton(root, text="SPAM!", variable=is_spam, onvalue=True)
check.pack()

breakfast = StringVar()
eggsRadio = ttk.Radiobutton(root, text="Eggs", variable=breakfast, value="Eggs")
pancackesRadio = ttk.Radiobutton(root, text="Pancakes", variable=breakfast, value="Pancakes")
toastRadio = ttk.Radiobutton(root, text="Toast", variable=breakfast, value="Toast")
eggsRadio.pack()
pancackesRadio.pack()
toastRadio.pack()

root.mainloop()