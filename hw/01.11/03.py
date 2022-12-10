import turtle

a = 20
b = a * 2 ** 0.5
turtle.speed(speed = 1)
turtle.penup()

def go():
    turtle.pendown()
    turtle.forward(a)
    turtle.penup()

def Go():
    turtle.pendown()
    turtle.forward(b)
    turtle.penup()

def execute(s, x, y):
    ar = s.split()
    turtle.penup()
    print(ar)
    for c in ar:
        if (c =='goto'):
            turtle.goto(x, y)
            continue
        if (c == '+'):
            x += a * 2
            print(x)
            continue
        f = c[0]
        if f == 'g':
            go()
            continue
        if f == 'G':
            Go()
            continue
        if f == 'r':
            turtle.right(int(c[1:]))
            continue
        if f == 'l':
            turtle.left(int(c[1:]))
            continue
        if f == 'h':
            print(c[1:], int(c[1:]))
            turtle.setheading(int(c[1:]))
            continue
        if f == 'f':
            if c[1] == 'a':
                turtle.forward(a)
            else:
                turtle.forward(b)
            continue
    return (x, y)
f = []
with open('file') as file:
    for line in file:
         print('line: "', line, '"')
         s = line[2:]
         f.append(s)
query = '123456789'
X = 0
Y = 0
for c in query:
    x = ord(c) - ord('0')
    X, Y = execute(f[x], X, Y)
