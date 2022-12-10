import turtle 
turtle.shape('turtle')
turtle.speed(speed=0.5)

n = 100
d = 360/n
for i in range(n):
    turtle.right(d)
    turtle.forward(10)
