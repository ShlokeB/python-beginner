from turtle import *
import colorsys

speed(0)

bgcolor("black")
width(2)
#t.tracer(10)

hue = 0.0

for i in range(500):
    color = colorsys.hsv_to_rgb(hue , 1 , 1)
    pencolor(color)
    hue += 0.007
    right(i)
    circle(50 , i)
    forward(i)
    left(91)

hideturtle()
done()