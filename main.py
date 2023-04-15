from tkinter import *
from tkinter import ttk
root = Tk()
root.title("SDM File Download")
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Button(frm, text = "Quit", command = root.destroy).grid(column = 1, row = 1)
ttk.Button(frm, text = "List Ports",).grid(column = 0, row = 0)
ttk.Button(frm, text = "Download").grid(column = 1, row = 0)
root.mainloop()

