import tkinter as t 
from tkinter import ttk
window=t.Tk()
my_var=t.BooleanVar()
my_checkbutton=ttk.Checkbutton(text="Check if true",variable=my_var)
my_checkbutton.pack()
window.mainloop()