import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x - 0.5*np.sin(x) - 1

x = np.linspace(1,2,1000)
y = f(x)

plt.plot(x, y)
plt.show()

l = 1
r = 2

while r-l > 1e-3:
    m = (l+r)/2
    if f(m) > 0:
        r = m
    else:
        l = m

print(l)