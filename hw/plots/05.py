import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set()   

def avg(X):
    return sum(X)/len(X)
#результат правильный, но он рисует параболу как прямую по понятным причинам

f = open("data2", "r", encoding="utf-8")
ar = list(map(lambda x: x.rstrip().split(), f.readlines()))
f.close()
X = []
Y = []
erX = []
erY = []
erT = 0.1
erA = 0.05 * 0.01
erx = 0.05 * 0.01

plt.ylabel('$T \cdot x_{ц},\:м\cdot с$')
plt.xlabel('$a^2$, $м^2$') 

for [a, x_c, T] in ar:
    a, x_c, T = float(a), float(x_c), float(T)
    a = a / 1000 # m
    x_c = x_c / 1000 # m
    u = x_c * (T**2)
    Y.append(u)
    erY.append(T*(T*erx + 2 * erT * x_c))
    X.append(a**2)
    erX.append(2 * erA * a)

s1 = xa = ya = x2 = y2 = 0

n = len(X)

plt.scatter(X, Y, color = 'blue')

def abline(k, b):
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = b + k * x_vals
    plt.plot(x_vals, y_vals, '--')
def abpar(a, b, c):
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = a * x_vals ** 2 + b * x_vals + c
    plt.plot(x_vals, y_vals, '--', color = 'black')
    
p, v = np.polyfit(X, Y, deg=1, cov=True)
abline(p[0], p[1])
p, v = np.polyfit(X, Y, deg=2, cov=True)
abpar(p[0],p[1],p[2])

plt.errorbar(X, Y, xerr=erX, yerr=  erY , fmt="o", color = 'blue')

plt.show() 