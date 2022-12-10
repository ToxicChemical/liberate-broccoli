from random import randint
import turtle

number_of_turtles = 20
steps_of_time_number = 100


pool = [turtle.Turtle(shape = 'turtle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.shape('circle')
    unit.speed(50)
    unit.goto(randint(-200, 200), randint(-200, 200))

def checkcollision():
    for i in range(len(pool)):
        for j in range (i + 1, len(pool)):
            [ax, ay] = pool[i].position()
            [bx, by] = pool[j].position()

            if (((ax-bx)**2 + (ay - by)**2) < 200):
                pool[i].right(360)
                pool[i].forward(10)
                pool[j].right(360)
                pool[j].forward(10)

for i in range(steps_of_time_number):
    for unit in pool:
        unit.right(randint(0, 360))
        unit.forward(20)
    checkcollision()