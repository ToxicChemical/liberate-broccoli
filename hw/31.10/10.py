import turtle
import math 
turtle.right(90)
turtle.speed(speed = 0)
for i in range(10):
    turtle.circle((i + 1) * 10)
    turtle.circle(-(i + 1) * 10)