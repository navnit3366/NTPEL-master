import tkinter as tk

# windows is an instance of tkinter class's Tk()
window=tk.Tk()
window.title("Python")

'''
greeting=t.Label(text='Hello')
greeting.pack()
'''

my_button = tk.Button(window,text='Quit',height=1,width=35,command=window.destroy)
my_button.pack()

window.mainloop() # to get the shell prompt after closing the window
