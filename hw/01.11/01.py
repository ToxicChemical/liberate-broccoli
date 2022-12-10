import turtle
import math
from random import *
n = randint(10, 100)
turtle.speed(10)
for i in range(n):
    l = random() * randint(30, 50)
    a = randint(0, 360)
    turtle.right(a)
    turtle.forward(l)
