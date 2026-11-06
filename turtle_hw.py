#draw flag of russia  and japan
from turtle import *
speed(0)
# --- FLAG OF RUSSIA ---

penup()
goto(-250, 100)
pendown()
color("lightgray", "white")
begin_fill()
for i in range(2):
    forward(200)
    right(90)
    forward(40)
    right(90)
end_fill()

penup()
goto(-250, 60)
pendown()
color("blue", "blue")
begin_fill()
for i in range(2):
    forward(200)
    right(90)
    forward(40)
    right(90)
end_fill()

penup()
goto(-250, 20)
pendown()
color("red", "red")
begin_fill()
for i in range(2):
    forward(200)
    right(90)
    forward(40)
    right(90)
end_fill()
# --- FLAG OF JAPAN ---

penup()
goto(50, 100)
pendown()
color("lightgray", "white")
begin_fill()
for i in range(2):
    forward(200)
    right(90)
    forward(120)
    right(90)
end_fill()

penup()
goto(150, 10)
pendown()
color("red", "red")
begin_fill()
circle(30)
end_fill()
hideturtle()
mainloop()