import turtle 
turtle.shape('turtle')
turtle.speed(speed=0.5)

n = 50
d = 360/n
len = 100
for i in range(n):
    turtle.forward(len)
    turtle.stamp()
    turtle.right(180)
    turtle.forward(len)
    turtle.right(180)
    turtle.right(d)
