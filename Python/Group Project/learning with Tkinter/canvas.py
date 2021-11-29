from tkinter import *
from math import *

root = Tk()
canvas = Canvas(root,width="500", height="400",bg="orange")
canvas.grid(row=0,column=0,columnspan=3)
global generation
generation = 1

class Triangle(Tk):

    def __init__(fract):
        Tk.__init__(fract)

        fract.title("Sierpinski")

        fract.width = 512
        fract.height = int(round(fract.width*sqrt(3.0)/2.0))
        fract.margin = 10

        fract.canvas = Canvas(fract, width=fract.width+(2*fract.margin), height=fract.height+(2*fract.margin), bg="white")
        fract.canvas.pack()

        fract.btn = Button(fract, text="Make", command=fract.draw)
        fract.btn.pack(side=LEFT)

        fract.label = Label(fract, text="Size")
        fract.label.pack()

        fract.level = Entry(fract, width=3, justify=CENTER)
        fract.level.insert(INSERT, "1")
        fract.level.pack()

        fract.mainloop()        

    def draw(fract):
        fract.canvas.delete("all")

        level = int(fract.level.get())

        x1 = fract.margin + 0 
        y1 = fract.margin + fract.height
        x2 = fract.margin + fract.width/2
        y2 = fract.margin + 0
        x3 = fract.margin + fract.width
        y3 = fract.margin + fract.height

        fract.recursion(level, x1, y1, x2, y2, x3, y3)

    def recursion(fract, level, x1, y1, x2, y2, x3, y3):
        print("level:", level)

        if level <= 1:
            fract.canvas.create_line(x1, y1, x2, y2)
            fract.canvas.create_line(x2, y2, x3, y3)
            fract.canvas.create_line(x3, y3, x1, y1)
        else:
            level = level - 1

            middle_x1 = (x1 + x2)/2
            middle_y1 = (y1 + y2)/2

            middle_x2 = (x2 + x3)/2
            middle_y2 = (y2 + y3)/2

            middle_x3 = (x3 + x1)/2
            middle_y3 = (y3 + y1)/2

            fract.recursion(level, x1, y1, middle_x1, middle_y1, middle_x3, middle_y3)
            fract.recursion(level, middle_x1, middle_y1, x2, y2, middle_x2, middle_y2)
            fract.recursion(level, middle_x3, middle_y3, middle_x2, middle_y2, x3, y3)

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

def Koch(x, y, angle, length,generation):
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

class Tree:
    def __init__(self):
        window = Tk()
        window.title("Fractal Tree")

        self.width = 400
        self.height = 400
        self.canvas = Canvas(window,
                             width=self.width, height=self.height, bg="grey")
        self.canvas.pack()

        frame1 = Frame(window)
        frame1.pack()

        Label(frame1,
              text="Enter the depth: ").pack(side=LEFT)
        self.depth = StringVar()
        Entry(frame1, textvariable=self.depth,
              justify=RIGHT).pack(side=LEFT)
        Button(frame1, text="Display Recursive Tree",
               command=self.display).pack(side=LEFT)

        self.angleFactor = pi / 5
        self.sizeFactor = 0.58

        window.mainloop()

    def drawLine(self, x1, y1, x2, y2):
        self.canvas.create_line(x1, y1, x2, y2, tags="line")

    def display(self):
        self.canvas.delete("line")
        depth = int(self.depth.get())
        return self.paintBranch(depth, self.width / 2, self.height, self.height / 3, pi / 2)

    def paintBranch(self, depth, x1, y1, length, angle):
        if depth >= 0:
            depth -= 1
            x2 = x1 + int(cos(angle) * length)
            y2 = y1 - int(sin(angle) * length)

            # Draw the line
            self.drawLine(x1, y1, x2, y2)

            # Draw the left branch
            self.paintBranch(depth, x2, y2, length * self.sizeFactor, angle + self.angleFactor)
            # Draw the right branch
            self.paintBranch(depth, x2, y2, length * self.sizeFactor, angle - self.angleFactor)


def myClick():
    myLabel = Label(root, text="Will display desired fractal.")
    myLabel.grid(row=2,column=0,columnspan=3)

'''
Buttons to show each fractal.
'''
myButton_1st = Button(root, text="Tree", padx=50, command=Tree)
myButton_2nd = Button(root, text="Koch's inspired", padx=50, command=lambda:Koch(200,300,60,100,generation))
myButton_3rd = Button(root, text="Sierpinski triangle", padx=50, command=Triangle)
myButton_1st.grid(row=1,column=0)
myButton_2nd.grid(row=1,column=1)
myButton_3rd.grid(row=1,column=2)


root.mainloop()
