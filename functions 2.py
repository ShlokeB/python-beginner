from turtle import *
speed(0)
color = input("Which colour do you want")
size = int(input("What size do you want"))
sides = int(input("How many sides do you want"))

def shapes(color, size, sides):
    fillcolor(color)
    begin_fill()
    for i in range(sides):
        forward(size)
        left(360/sides)
    end_fill()

    mainloop()


shapes(color, size, sides)

