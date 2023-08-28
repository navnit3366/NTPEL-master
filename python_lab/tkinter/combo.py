import tkinter as t 
from tkinter import ttk
window=t.Tk()
my_str_var=t.StringVar()
myComboBox=ttk.Combobox(window,textvariable=my_str_var,values=['C','Python','C++','Java'])
myComboBox.pack()
window.mainloop()