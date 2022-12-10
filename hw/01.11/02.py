import turtle

x = y = 0
a = 20
b = a * 2 ** 0.5
turtle.color('red')
turtle.speed(speed = 2)
turtle.penup()

def go():
    turtle.pendown()
    turtle.forward(a)
    turtle.penup()
def go2():
    go()
    go()
def Go():
    turtle.pendown()
    turtle.forward(b)
    turtle.penup()
def Go2():
    Go()
    Go()    

def f0(): 
    global x
    global y
    turtle.goto(x, y)
    turtle.setheading(0)
    go()
    turtle.right(90)
    go2()
    turtle.right(90)
    go()
    turtle.right(90)
    go2()
    x += a * 2

def f1(): #goto h-90 fa l135 G r135 g2 +
    global x
    global y
    turtle.goto(x, y)
    turtle.setheading(-90)
    turtle.forward(a)
    turtle.left(135)
    Go()
    turtle.right(135)
    go2()
    x += a * 2
def f2(): #2: goto h0 g r90 g r45 G l135 g + 
    global x
    global y
    turtle.goto(x, y)
    turtle.setheading(0)
    go()
    turtle.right(90)
    go()
    turtle.right(45)
    Go()
    turtle.left(135)
    go()
    x += a * 2
def f3(): #3: goto h0 g r135 G l135 g r135 G +
    global x
    global y
    turtle.goto(x, y)
    turtle.setheading(0)
    go()
    turtle.right(135)
    Go()
    turtle.left(135)
    go()
    turtle.right(135)
    Go()
    x += a * 2
def f4(): #4: goto h-90 g l90 g l90 g l180 g2 +
    global x
    global y
    turtle.goto(x, y)
    turtle.setheading(-90)
    go()
    turtle.left(90)
    go()
    turtle.left(90)
    go()
    turtle.left(180)
    go2()
    x += a * 2
def f5(): #5: goto h0 fa r180 g l90 g l90 g r90 g r90 g +
    global x
    global y
    turtle.goto(x, y)
    turtle.setheading(0)
    turtle.forward(a)
    turtle.right(180)
    go()
    turtle.left(90)
    go()
    turtle.left(90)
    go()
    turtle.right(90)
    go()
    turtle.right(90)
    go()
    x += a * 2
def f6(): #6: goto h0 fa r135 G l135 g r90 g r90 g r90 g +
    global x
    global y
    turtle.goto(x, y)
    turtle.setheading(0)
    turtle.forward(a)
    turtle.right(135)
    Go()
    turtle.left(135)
    go()
    turtle.right(90)
    go()
    turtle.right(90)
    go()
    turtle.right(90)
    go()
    x += a * 2
def f7(): #7: goto h0 g r135 G l45 g +
    global x
    global y
    turtle.goto(x, y)
    turtle.setheading(0)
    go() 
    turtle.right(135)
    Go()
    turtle.left(45)
    go()
    x += a * 2
def f8(): #goto h0 g r90 g2 r90 g r90 g r90 g r180 fa r90 g +
    global x
    global y
    turtle.goto(x, y)
    turtle.setheading(0)
    go()
    turtle.right(90)
    go2()
    turtle.right(90)
    go()
    turtle.right(90)
    go()
    turtle.right(90)
    go()
    turtle.right(180)
    turtle.forward(a)
    turtle.right(90)
    go()
    x += 2 * a
def f9(): #9: goto h0 g r90 g r45 G r180 fb l135 g r90 g + 
    global x
    global y
    turtle.goto(x, y)
    turtle.setheading(0)
    go()
    turtle.right(90)
    go()
    turtle.right(45)
    Go()
    turtle.right(180)
    turtle.forward(b)
    turtle.left(135)
    go()
    turtle.right(90)
    go()
    x += 2 * a


#ar[10] = ['123456', '349', '1247', '2789', '1348', '12458', '45689', '269', '1234568', '12378']

f = [f0, f1, f2, f3, f4, f5, f6, f7, f8, f9]
for i in range(10):
    f[i]()
