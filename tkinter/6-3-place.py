from tkinter import *
from tkinter import ttk

root = Tk()

root.geometry("640x480")
# root.resizable(False, False)

ttk.Label(root, text="yellow", background="yellow").place(
x=100, y=50, width=100, height=50
)
ttk.Label(root, text="blue", background="blue").place(
    relx=0.5, rely=0.5, anchor="center", relwidth=0.5, relheight=0.5
) # 50% relative to parent size
ttk.Label(root, text="green", background="green").place(
    relx=0.5, x=100, rely=0.5, y=50
)
ttk.Label(root, text="orange", background="orange").place(
    relx=1.0, x=-5, y=5, anchor="ne"
)
btn = ttk.Button(root, text="Click me")
btn.place(
    x = 500, y= 300, width=100, height=100
)


print(btn.place_info())

root.mainloop()