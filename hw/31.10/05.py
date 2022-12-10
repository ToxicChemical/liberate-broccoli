import turtle 
turtle.shape('turtle')
turtle.speed(speed=0.5)
x = y = 0
dx = dy = 10
for i in range(10):
    for j in range(4):
        turtle.forward(20*(i+1))
        turtle.right(90)
    x -= dx
    y += dy
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
