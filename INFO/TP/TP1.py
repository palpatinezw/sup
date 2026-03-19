# -*- coding: utf-8 -*-
"""
TP1 je galère à cause du clavier
"""
import numpy as np
import matplotlib.pyplot as plt

# n = np.floor(7/3)
# s = np.sin(256/360 * 2 * np.pi)

# x = 2.1388
# assert(np.cos(2*x) == (np.cos(x))**2 - (np.sin(x))**2)

# =============================================================

# R = 2e-1

# def aire_sphere(r):
#     return 4*np.pi*(r**2)

# print('Aire: ', round(aire_sphere(R), 3), ' m^2')

# =============================================================

# def fibo(n):
#     u = [1, 1]
#     for i in range(2, n):
#         u.append(u[i-1] + u[i-2])
#     return u

# for i in fibo(30):
#     print(i)

# =============================================================

# omega = 2*np.pi
# A = 1
# t = np.linspace(0, 40, 10000)
# plt.plot(t, A*(np.cos(omega * t) + np.cos(0.9 * omega * t)), 'k')
# plt.plot(t, 2*A*np.cos((1 - 0.9)/2 * omega * t), 'r')
# plt.plot(t, -2*A*np.cos((1 - 0.9)/2 * omega * t), 'b')
# # plt.plot(x, x**3, '--r')
# plt.show()

# =============================================================

f = 50 # Hz

T = 1/f
fe = 2*f

ts = np.linspace(0, 20*T, round(20*T*fe)+1)

plt.plot(ts, np.cos(2*np.pi*f*ts))
plt.grid()
plt.show()






























































