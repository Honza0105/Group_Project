from tkinter import *
from math import *

'''
tkinter setting:
'''
root = Tk()
height = 400
width = 500
canvas = Canvas(root, width=width, height=height, bg="grey")
canvas.grid(row=0, column=0, columnspan=3)

'''
general variables:
'''
generation = 1
gen_up = StringVar(value=str(generation + 1))
gen_down = StringVar(value=str(generation - 1))

is_Koch = False
is_Tree = False
is_Triangle = False

'''
Tree variables:
'''
angleFactor = pi / 5
sizeFactor = 0.58

'''
Koch variables:
'''
koch_length = 100
koch_x = width / 4
koch_y = height * (3 / 4)

'''
Triangle variables:
'''
margin_s = 10
width_s = 400
height_s = int(round(width_s * sqrt(3.0) / 2.0))
lines_Sierpinski = []

'''
Triangle functions:
'''


def draw_sierpinski(generation_local, canvas_sierpinski):
    if is_Triangle is False:
        global generation
        generation = 1
        generation_local = 1
        gen_up.set(str(generation + 1))
        gen_down.set(str(generation - 1))
        myButton_generation_up['state'] = NORMAL
        myButton_generation_down['state'] = DISABLED
    canvas_sierpinski.delete("all")
    current_fractal("Triangle")
    global lines_Sierpinski
    for line in lines_Sierpinski:
        canvas_sierpinski.delete(line)
    lines_Sierpinski = []
    x1 = margin_s + 0
    y1 = margin_s + height_s
    x2 = margin_s + width_s / 2
    y2 = margin_s + 0
    x3 = margin_s + width_s
    y3 = margin_s + height_s

    recursion_sierpinski(generation_local, x1, y1, x2, y2, x3, y3)
    return


def recursion_sierpinski(generation_sierpinski, x1, y1, x2, y2, x3, y3):
    if generation_sierpinski <= 1:
        lines_Sierpinski.append(canvas.create_line(x1, y1, x2, y2))
        lines_Sierpinski.append(canvas.create_line(x2, y2, x3, y3))
        lines_Sierpinski.append(canvas.create_line(x3, y3, x1, y1))
    else:
        generation_sierpinski = generation_sierpinski - 1

        middle_x1 = (x1 + x2) / 2
        middle_y1 = (y1 + y2) / 2

        middle_x2 = (x2 + x3) / 2
        middle_y2 = (y2 + y3) / 2

        middle_x3 = (x3 + x1) / 2
        middle_y3 = (y3 + y1) / 2
        recursion_sierpinski(generation_sierpinski, x1, y1, middle_x1, middle_y1, middle_x3, middle_y3)
        recursion_sierpinski(generation_sierpinski, middle_x1, middle_y1, x2, y2, middle_x2, middle_y2)
        recursion_sierpinski(generation_sierpinski, middle_x3, middle_y3, middle_x2, middle_y2, x3, y3)
    return


'''
Koch's functions:
'''


def koch(x, y, angle, length, generation_local):
    if is_Koch is False:
        global koch_length
        global generation
        koch_length = 100
        length = 100
        generation = 1
        generation_local = 1
        gen_up.set("2")
        gen_down.set("0")
        myButton_generation_up['state'] = NORMAL
        myButton_generation_down['state'] = DISABLED
    current_fractal("Koch")
    canvas.delete("all")
    length //= 3
    for i in range(3):
        for n in range(generation_local):
            x, y = draw_lines_koch(canvas, x, y, length / generation_local, radians(angle), 4)
            angle += 60
            x, y = draw_lines_koch(canvas, x, y, length / generation_local, radians(angle), 4)
            angle -= 120
            x, y = draw_lines_koch(canvas, x, y, length / generation_local, radians(angle), 4)
            angle += 60
            x, y = draw_lines_koch(canvas, x, y, length / generation_local, radians(angle), 4)
        angle -= 120


def draw_lines_koch(canvas_koch, x0, y0, length, angle, recursion):
    if recursion == 0:
        return x0, y0
    else:
        x1, y1 = x0 + length * cos(angle), y0 - length * sin(angle)
        canvas_koch.create_line(x0, y0, x1, y1)
        if recursion % 2 == 0:
            angle += pi / 3
        elif recursion == 3:
            angle -= 2 * pi / 3
        return draw_lines_koch(canvas_koch, x1, y1, length, angle, recursion - 1)


'''
Triangle's functions:
'''


def draw_line_tree(x1, y1, x2, y2):
    canvas.create_line(x1, y1, x2, y2, tags="line")


def display():
    global generation
    if is_Tree is False:
        generation = 0
        gen_up.set("2")
        gen_down.set("0")
        myButton_generation_up['state'] = NORMAL
        myButton_generation_down['state'] = DISABLED
    current_fractal("Tree")
    canvas.delete("all")
    depth = generation

    return paint_branch(depth, width / 2, height, height / 3, pi / 2)


def paint_branch(depth, x1, y1, length, angle):
    if depth >= 0:
        depth -= 1
        x2 = x1 + int(cos(angle) * length)
        y2 = y1 - int(sin(angle) * length)

        draw_line_tree(x1, y1, x2, y2)

        paint_branch(depth, x2, y2, length * sizeFactor, angle + angleFactor)

        paint_branch(depth, x2, y2, length * sizeFactor, angle - angleFactor)


'''
General functions:
'''


def current_fractal(name):
    global is_Koch
    global is_Tree
    global is_Triangle
    is_Koch = True
    is_Tree = False
    is_Triangle = False
    if name == "Tree":
        is_Koch = False
        is_Tree = True
        is_Triangle = False
    elif name == "Koch":
        is_Koch = True
        is_Tree = False
        is_Triangle = False
    elif name == "Triangle":
        is_Koch = False
        is_Tree = False
        is_Triangle = True


def my_click():
    canvas.delete("all")
    my_testing_label = Label(root, text="Will display desired fractal.")
    my_testing_label.grid(row=2, column=3, columnspan=1)


def zoom_in_koch():
    global koch_length
    global generation
    if is_Koch is True:
        koch_length *= 2
        koch(koch_x, koch_y, 60, koch_length, generation)


def zoom_out_koch():
    global koch_length
    global generation
    if is_Koch is True:
        koch_length /= 2
        koch(koch_x, koch_y, 60, koch_length, generation)


def generation_up():
    global koch_length
    global generation
    global canvas
    generation += 1
    if is_Koch:
        koch(koch_x, koch_y, 60, koch_length, generation)
    if is_Triangle:
        draw_sierpinski(generation, canvas)
    if is_Tree:
        display()
    if generation == 34:
        gen_up.set(str(generation + 1))
        myButton_generation_up['state'] = DISABLED
    else:
        gen_up.set(str(generation + 1))
        myButton_generation_up['state'] = NORMAL

    gen_down.set(str(generation - 1))
    myButton_generation_down['state'] = NORMAL


def generation_down():
    global koch_length
    global generation
    global canvas
    generation -= 1
    if is_Koch:
        koch(koch_x, koch_y, 60, koch_length, generation)
    if is_Triangle:
        draw_sierpinski(generation, canvas)
    if is_Tree:
        display()
    gen_up.set(str(generation + 1))
    myButton_generation_up['state'] = NORMAL
    if generation == 1:
        gen_down.set(str(generation - 1))
        myButton_generation_down['state'] = DISABLED
    else:
        gen_down.set(str(generation - 1))
        myButton_generation_down['state'] = NORMAL


'''
Buttons to show each fractal.
'''
myButton_1st = Button(root, text="Fractal Tree", padx=50, command=display)
myButton_2nd = Button(root, text="Koch's inspired", padx=50,
                      command=lambda: koch(koch_x, koch_y, 60, koch_length, generation))
myButton_3rd = Button(root, text="Sierpinski triangle", padx=50, command=lambda: draw_sierpinski(generation, canvas))

myButton_1st.grid(row=1, column=0)
myButton_2nd.grid(row=1, column=1)
myButton_3rd.grid(row=1, column=2)

'''
GUI labels:
'''
myLabel_zoom = Label(root, text="Zoom", padx=50)
myLabel_zoom.grid(row=2, column=0)

myLabel_generation = Label(root, text="Generation", padx=50)
myLabel_generation.grid(row=3, column=0)

'''
GUI buttons
'''
# tree_button = Button(root, text="Display Fractal Tree",command=display).grid(row=4, column=0)
myButton_zoom_in = Button(root, text="+", padx=75, command=zoom_in_koch)
myButton_zoom_out = Button(root, text="-", padx=75, command=zoom_out_koch)
myButton_zoom_in.grid(row=2, column=1)
myButton_zoom_out.grid(row=2, column=2)

myButton_generation_up = Button(root, textvariable=gen_up, padx=75, state=DISABLED, command=generation_up)
myButton_generation_up.grid(row=3, column=1)
myButton_generation_down = Button(root, textvariable=gen_down, padx=75, state=DISABLED, command=generation_down)
myButton_generation_down.grid(row=3, column=2)

root.mainloop()
