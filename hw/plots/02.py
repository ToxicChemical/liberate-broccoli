import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set()

def f(x):
    return x**2 - x - 6

x = np.linspace(-5.0, 5, 100)
plt.axhline(y = 0, c = 'black')
plt.plot(x, f(x), color = 'red')
plt.show()