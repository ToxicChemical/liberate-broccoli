import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set()

def loga(a, b): #log_a(b)
    return np.log(b)/np.log(a) #log == натуральный логарифм.

def f(x):
    return loga(1 + np.tan(1/ (1 + np.sin(x) ** 2)), (x**2 + 1)*np.e**(-abs(x)/10.0))

x = np.linspace(-100.0, 100, 100)
plt.axhline(y = 0, c = 'black')
plt.plot(x, f(x), color = 'red')
plt.show()