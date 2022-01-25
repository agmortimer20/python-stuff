from tkinter import *
from tkinter import ttk

root = Tk()

def key_press(event):
    print(f"type: {event.type}")
    print(f"widget: {event.widget}")
    print(f"char: {event.char}")
    print(f"keysym: {event.keysym}") #symbol
    print(f"keycode: {event.keycode}")

def getmsg(msg):
    print(msg)

# root.bind("<KeyPress>", key_press)
# root.bind('<Key>', key_press)
root.bind('a', key_press)

root.mainloop()