#https://python-course.eu/tkinter_canvas.php/

from tkinter import *
 
root = Tk()
root.geometry("700x700") 
canvas = Canvas(root,bg='orange', width = 500,height = 500)

x1 = 200
y1 = 50
x2 = 220
y2 = 250
x3 = 280
y3 = 150
canvas.create_line(x1,y1,x2,y2,fill="black",width=20)
#canvas.create_polygon(x1,y1,x2,y2,x3,y3,outline="yellow", fill="red",width=3)

coordinates = 300, 300, 460, 460
canvas.create_arc(coordinates, start=0, extent=180, fill="blue")
#canvas.create_arc(coordinates, start=250, extent=50, fill="red")
#canvas.create_arc(coordinates, start=300, extent=60, fill="yellow")
 
canvas.pack()

root.title("Shapes") 
root.mainloop()
