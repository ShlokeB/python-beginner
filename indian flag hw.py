
from turtle import *
speed(0)

penup()
goto(-150, 100)
pendown()
color("orange", "orange")
begin_fill()
for i in range(2):
    forward(300)
    right(90)
    forward(66)
    right(90)
end_fill()

penup()
goto(-150, 34)
pendown()
color("white", "white")
begin_fill()
for i in range(2):
    forward(300)
    right(90)
    forward(66)
    right(90)
end_fill()

penup()
goto(-150, -32)
pendown()
color("darkgreen", "darkgreen")
begin_fill()
for i in range(2):
    forward(300)
    right(90)
    forward(66)
    right(90)
end_fill()

penup()
goto(0, -30)
pendown()
color("navy")
pensize(2)
circle(30)


penup()
goto(0, 0)
pendown()
for i in range(24):
    forward(30)
    backward(30)
    left(15)

hideturtle()
done()

