import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set()   

def pow_fast(x, k):
    if (k == 0):
        return 1
    if (k == 1):
        return x 
    if (k % 2 == 0):
        return (pow_fast(x, k // 2)) ** 2
    return pow_fast(x, k - 1) * x
def f(x, m, a, b):
    ans = 0
    pr_b = 1;
    pr_a = 1;
    for n in range(m):
        ans += pow_fast(b, n) * np.cos(pow_fast(a, n) * np.pi * x)
    return ans
m = 200
a = 17
b = 0.239

x = np.linspace(-100.0, 100, 100)
plt.axhline(y = 0, c = 'black')
plt.plot(x, f(x, m, a, b), color = 'red')
plt.show()