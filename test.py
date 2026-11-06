from turtle import *
bgcolor("red")
pencolor("orange")
pensize(5)
speed(0)

fillcolor("blue")
begin_fill()
for i in range(3):

  forward (100)
  left(120)

end_fill()


#square
fillcolor("navy")
begin_fill()
for i in range (4):

    forward(100)
    right(90)




end_fill()




#door



penup()
goto (35,-100)
pendown()
fillcolor("yellow")
begin_fill()
left(90)
for i in range(2):
    
    forward(50)
    right(90)
    forward(33)
    right(90)



end_fill()








#window
penup()
goto (12,-12)
pendown()
fillcolor("purple")
begin_fill()
for i in range(4):

    right(90)
    forward(25)



end_fill()

penup()
goto (62,-12)
pendown()
fillcolor("purple")
begin_fill()
for i in range(4):

    right(90)
    forward(25)



end_fill()


penup()



goto (0,200)
pendown()
pencolor("green")
write ("House", align="center", font=("arial", 50, "bold"))

hideturtle()



































mainloop()
