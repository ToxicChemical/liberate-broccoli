import math
import turtle
turtle.speed(speed = 1)
for i in range(200):
    theta = i / 20 * math.pi #угол, который изменятся
    x = (1 + 1 * theta) * math.cos(theta) #r = a + b\theta
    y = (1 + 1 * theta) * math.sin(theta)
    turtle.goto(x, y)
turtle.up()