'''
Third point is broken
- needs a fix
- a different approach is acceptable

'''


from tkinter import *
from math import cos, sin, pi
def main():
    root = Tk()
    root.geometry("800x600")

    label1 = Label(root, text="Here will be the table.")
    label1.pack()
    root.title("Our project")


    canvas = Canvas(root, bg="orange", width = 500, height= 500)

    #starting points
    x0, y0 = 200, 300
    x1, y1 = 300, 300
    base = x0,y0,x1,y1
    create_triangle(canvas, base)
    generation(canvas, x0,y0,*third_point(base))
    #create_line(canvas, x0, y0, *third_point(base))
    root.mainloop()

def create_line(canvas,x0,y0,x1,y1):
    canvas.create_line(x0,y0,x1,y1,fill="black", width=3)
def create_triangle(canvas,base):
    canvas.create_polygon(base,third_point(list(base)),outline="yellow", fill="red",width=3)

    print(middle_points(base))
    canvas.pack()
def generation(canvas, x0,y0,x1,y1):
    '''
    it  gets the base- then middle points, then it takes the first and middle, makes line, takes middle and last makes line and then deletes the part of base
    base is going to be the tripoints
    always saving new sides - rn x0,y0,x1,y1 are the old sides
    '''
    base = [x0,y0,x1,y1]
    base = middle_points(base)
    canvas.create_polygon(base,third_point(list(base)),outline="green", fill="red",width=1)
    #canvas.create_line(base[0], base[1], *third_point(base), outline="yellow", width=3)
    #create_line(canvas,base[0],base[1],*third_point(base))
    create_line(canvas,*tuple(base))
    print(third_point(base))




#rotates the base by 60 deg
#proposal - we could make it possible to modify the inital shift
#my comment: Could be COOL
#Conclusion: ???
def third_point(base):
    x_diff = base[1] - base[0]
    y_diff = base[3] - base[2]
    angle = pi / 3
    x2 = cos(angle) * x_diff - sin(angle) * y_diff + base[0]
    y2 = sin(angle) * x_diff + cos(angle) * y_diff + base[2]
    return x2,y2
def middle_points(base):
    x0 = base[0]
    y0 = base[1]
    x1 = base[2]
    y1 = base[3]
    x_first = (x1 - x0)*1/3 + x0
    y_first = (y1 - y0)*1/3 + y0
    x_second = (x1 - x0)*2/3 + x0
    y_second = (y1 - y0)*2/3 + y0
    return x_first, y_first, x_second, y_second


main()