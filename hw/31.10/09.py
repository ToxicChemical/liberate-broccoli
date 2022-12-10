import turtle
import math 

def draw(n, len):
    d = 360/n
    for i in range(n):
        turtle.forward(len)
        if (i != n-1):
            turtle.right(d)
    turtle.left(90 - d/2)
turtle.shape('turtle')
turtle.speed(speed=0)

x = y = 0
pr = 0
for i in range(10):
    a = 10 * (i + 1)
    n = i + 3
    r = a / (2.0 * math.sin(math.pi/n))
    l = r - pr
    alpha = 90*(n + 2) / n
    turtle.penup()
    turtle.forward(l)
    turtle.right(alpha)
    turtle.pendown()
    draw(n, a)    
    pr = r
    