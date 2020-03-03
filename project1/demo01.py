import turtle
turtle.pensize(5)
turtle.pencolor("yellow")
turtle.fillcolor("red")
turtle.begin_fill()
while True:
    turtle.forward(200)
    turtle.right(144)
    if abs(turtle.pos()) < 1:
        break
turtle.end_fill()
turtle.mainloop()


