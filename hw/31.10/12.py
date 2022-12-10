import turtle
turtle.shape('turtle')
turtle.speed(speed = 5)

def drawduga(n, flip = False):
    if (flip):
        turtle.setheading(-90)

    for i in range(n - 1):
        turtle.setheading(90)
        if (flip):
            turtle.setheading(-90)
        turtle.circle(-50, 180)
        turtle.circle(-10, 180)
    turtle.circle(-50, 180)

def go(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

turtle.circle(150)
go(-50, 150)
turtle.circle(10)
go(50, 150)
turtle.circle(10)
go(0, 120)
turtle.setheading(90)
turtle.backward(50)
go(40, 60)
drawduga(1, True)
