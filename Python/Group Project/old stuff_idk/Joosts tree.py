from turtle import *
from tkinter import *
from pcinput import *

fractal_number = getInteger("give me the number of fractals: ")
fractal_color = getString("give me the collor of the fractal: ")

speed("fastest")

def tree(size, levels, angle):
   if levels == 0:
       color(fractal_color)
       return

   forward(size)
   right(angle)

   tree(size * 0.8, levels - 1, angle)

   left(angle * 2)

   tree(size * 0.8, levels - 1, angle)

   right(angle)
   backward(size)

left(90)
tree(70, fractal_number, 30)

mainloop()
