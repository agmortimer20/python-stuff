from tkinter import *
from tkinter import ttk

# Create main window
window = Tk()


# Create label widget
hello_label = Label(window, text="Hello Tkinter!")
hello_label.pack() # Attach to window using pack

hello_label2 = Label(window, text="Helo again...")
hello_label2.pack()

hello_label3 = Label(window, text="Hello one more time.")
hello_label3.pack()


# Start main window
window.mainloop()