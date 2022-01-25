from tkinter import *
from tkinter import ttk

def quit():
    root.destroy() # close window

root = Tk()
root.title("Main")

window = Toplevel(root)
window.title("New Window")
window.state("withdrawn") 

# Window size
root.geometry("640x480+10+10")
root.resizable(False, False)
# root.maxsize(x, y)
# root.minsize(x, y)

btn = ttk.Button(root, text="Close", command=quit).pack()

root.mainloop()


"""
    Window States:
    'normal'
    'zoomed' - maximized
    'withdrawn' - hidden
    'iconic' - minimized
"""