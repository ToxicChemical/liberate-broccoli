import turtle
x = -400
y = 0
Vx = 10
dt = 0.1
Vy = 10
ay = -1
turtle.speed(1)
for i in range(1000):
    x += Vx*dt
    y += Vy*dt + ay*dt**2/2
    if y <= 0 and Vy < 0:
        Vy = -Vy
        ay -= 1
        if (ay <= -8):
            break
    Vy += ay*dt
    turtle.goto(x, y)
