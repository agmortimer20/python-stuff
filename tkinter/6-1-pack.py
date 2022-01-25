"""Pack
Default - Pack to top
Stack starts at center of packing side

"""
from tkinter import *
from tkinter import ttk

root = Tk()

Button(root, text="hello tkinter", background="yellow").pack(expand=True)
Button(root, text="hello tkinter", background="green").pack(expand=True)
Button(root, text="hello tkinter", background="green").pack()
Button(root, text="hello tkinter", background="green").pack()



# ttk.Label(root, text="hello tkinter", background="yellow").pack(fill=BOTH, expand=True)
# ttk.Label(root, text="hello tkinter", background="green").pack(fill=BOTH, expand=True)
# ttk.Label(root, text="hello tkinter", background="blue").pack(fill=BOTH)

# ttk.Label(root, text="hello tkinter", background="yellow").pack(side=LEFT)
# ttk.Label(root, text="hello tkinter", background="green").pack(side=LEFT)
# ttk.Label(root, text="hello tkinter", background="blue").pack(side=LEFT)

# ttk.Label(root, text="hello tkinter", background="yellow").pack(side=LEFT, anchor="nw")
# ttk.Label(root, text="hello tkinter", background="green").pack(side=LEFT)
# ttk.Label(root, text="hello tkinter", background="blue").pack(side=LEFT)

# ttk.Label(root, text="hello tkinter", background="yellow").pack(side=LEFT, anchor="nw")
# ttk.Label(root, text="hello tkinter", background="green").pack(side=LEFT, padx=10, pady=10)
# ttk.Label(root, text="hello tkinter", background="blue").pack(side=LEFT, ipadx=10, ipady=10)
# print(root.pack_slaves())

# for widget in root.pack_slaves():
#     print(widget.pack_info())
#     widget.pack_configure(fill=BOTH, expand=True)
#     # widget.pack_forget() Unpack widget from pack


root.mainloop()
