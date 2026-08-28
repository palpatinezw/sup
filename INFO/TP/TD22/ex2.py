import numpy as np

l = 1
r = 2
N = 1000

x = l
h = (r-l)/N

s = 0
for i in range(N):
    s += (1/(x + h/2)) * h
    x += h
print(s)