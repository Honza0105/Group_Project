from tkinter import *

root = Tk()

my_Label1 = Label(root, text="Hello World!")
my_Label2 = Label(root, text="My name is Test")

my_Label1.grid(row=0,column=0)
my_Label2.grid(row=1,column=1)

root.mainloop()
