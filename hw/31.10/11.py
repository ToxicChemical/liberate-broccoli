import turtle
turtle.shape('turtle')
turtle.speed(speed = 1)

def drawduga(n):
    for i in range(n - 1):
        turtle.setheading(-90)
        turtle.circle(-50, 180)
        turtle.circle(-10, 180)
    turtle.circle(-50, 180)
turtle.penup()
turtle.goto(-10, 0)
turtle.pendown()
drawduga(3)