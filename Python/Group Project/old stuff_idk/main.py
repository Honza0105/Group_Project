from tkinter import *
from math import cos, sin, pi


class Koch():
    def third_point(self, base):
        x_diff = base[1] - base[0]
        y_diff = base[3] - base[2]
        angle = 5 * pi / 3
        x2 = cos(angle) * x_diff - sin(angle) * y_diff + base[0]
        y2 = sin(angle) * x_diff + cos(angle) * y_diff + base[2]
        return x2, y2
    def middle_points(self,x0, y0, x1, y1):
        x_first = (x1 - x0) * 1 / 3 + x0
        y_first = (y1 - y0) * 1 / 3 + y0
        x_second = (x1 - x0) * 2 / 3 + x0
        y_second = (y1 - y0) * 2 / 3 + y0
        return x_first, y_first, x_second, y_second
    # starting points
    root = Tk()
    root.geometry("800x600")
    root.title("Our project")
    canvas = Canvas(root, bg="orange", width=500, height=500)
    x0, y0 = 200, 300
    x1, y1 = 300, 300
    base = x0, y0, x1, y1
    canvas.create_polygon(base, third_point(list(base)), outline="yellow", fill="red", width=3)
    canvas.pack()
    root.mainloop()

#rotates the base by 60 deg
#proposal - we could make it possible to modify the inital shift
#my comment: Could be COOL
#Conclusion: ???




'''
#canvas.create_line(coordinates,fill= "black", width = 4)
#canvas.create_line(x0,y0,third_point(x0,y0,x1,y1), fill= "black", width = 4)
'''
#canvas.create_polygon(base,third_point(list(base)),outline="yellow", fill="red",width=3)
'''
#print(tuple(base.values()))
print(base,third_point_dict(base), "Here")
print(middle_points(x0,y0,x1,y1))
'''


