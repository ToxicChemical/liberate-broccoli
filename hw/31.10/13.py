import turtle
turtle.shape('arrow')
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
def draw(n):
    k = -1
    for k1 in range(2, n):
        if gcd(k1, n) == 1:
            k = k1
            break
    for i in range(n):
        turtle.forward(60)
        turtle.right(180 - 180*(n-2*k)/n)
draw(100)