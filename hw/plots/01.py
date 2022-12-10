import math
def loga(a, b): #log_a(b)
    return math.log(b)/math.log(a)
def y(x):
    return loga(1 + x ** 2, (math.e ** (1/(math.sin(x) + 1)) / (5/4 + 1/(x**15))))
#x = float(input())
print(y(1)) 
print(y(10)) 
print(y(100)) 
# не понимаю, что имеется ввиду под 1_5 в формуле, поэтому интерпретировала это как 15
