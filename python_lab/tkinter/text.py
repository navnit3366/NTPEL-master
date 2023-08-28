import tkinter as tk
parent = tk.Tk()
mytext=tk.Text(parent)
mytext.insert('1.0','Hi NHCE')
mytext.insert('1.2', ' Python')
mytext.delete('1.0')
mytext.delete('1.12') #or 
mytext.delete('end -2chars')
mytext.pack()
parent.mainloop()