import tkinter as tk
parent = tk.Tk()
parent.title("Radio Button")
str=['First','Second','Third']
for i in range(3):
    radio=tk.Radiobutton(parent,text=str[i],value=i)
    radio.grid(column=i,row=0)
parent.mainloop()
