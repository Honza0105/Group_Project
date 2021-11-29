from tkinter import *
from math import sin, cos, pi, radians

def draw_lines( canvas, x0, y0, length, angle ):
    length //= 3
    x1, y1 = x0 + length*cos( angle ),y0 - length*sin( angle )
    canvas.create_line( x0,y0, x1, y1 )
    angle += pi/3
    x0, y0 = x1,y1
    x1, y1 = x1 + length*cos( angle ), y1 - length*sin( angle )
    canvas.create_line( x0,y0, x1, y1 )
    angle -= 2*pi/3
    x0, y0 = x1,y1
    x1, y1 = x1 + length*cos( angle ), y1 - length*sin( angle )
    canvas.create_line( x0,y0, x1, y1 )
    angle += pi/3
    x0, y0 = x1,y1
    x1, y1 = x1 + length*cos( angle ), y1 - length*sin( angle )
    canvas.create_line( x0,y0, x1, y1 )
    return x1,y1

def Koch(x, y, angle, lenght,generation):
    for i in range(3):
        for i in range(generation):
            x, y = draw_lines(canvas, x, y, length/generation, radians(angle))
            angle += 60
            x, y = draw_lines(canvas, x, y, length / generation, radians(angle))
            angle -= 120
            x, y = draw_lines(canvas, x, y, length / generation, radians(angle))
            angle += 60
            x, y = draw_lines(canvas, x, y, length / generation, radians(angle))
        angle -= 120

eu
root = Tk()
root.geometry("700x700")
canvas = Canvas(root, width = 500,height = 500)

x = 200
y = 300
angle = 60
length = 100
generation = 5

Koch(x,y,angle,length,generation)

canvas.pack()
root.mainloop()