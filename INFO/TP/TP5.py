#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  3 14:02:50 2025

@author: zhuang@pedagogique.local
"""

import random

#%% Ex 1

n = 7
fact = 1

for i in range(1, n+1):
    fact *= n
    
print(fact)

#%% Ex 2

u = 760
up = u
N = 0

while u >= 0:
    up = u
    N += 1
    u = u/2 - 3*N
    # print(f"{N} : {u}")
    
print(f"{N-1} : {up}")

#%% Ex 3

n = 100
ls = []

for i in range(1, n):
    if n % i == 0 and i % 2 == 0: ls.append(i)
    
print(ls)
    
#%% Ex 4

n = 3
somme = 0

for i in range(1, n+1):
    for j in range(1, n+1):
        somme += abs(i-j)
    
print(somme)


#%% Ex 5

s = 5
n = 20

for i in range(s, n+1):
    print(f"{i} * 7 = {i*7}")

#%% Ex 6

x = 25

if x < 0: 
    print("Impossible de calculer")
else: 
    print(x ** (0.5))

#%% Ex 7

u = 1
n = 10
r = 3

for i in range(n):
    print(u*(r**i))


#%% Ex 8

reussi = False

while not reussi:
    x = input("Entrer un nombre entre 1 et 10: ")
    try:
        x = float(x)
        
        if x <= 10 and x >= 0: 
            reussi = True
            print("Bravo")
        else:
            print("Essaie encore")
    
    except:
        print("Essaie encore")

#%% Ex 9

n = 15
somme1 = 0

for i in range(1, n+1):
    somme1 += 1/(i**2)

# ==============================

somme2 = 0

for i in range(1, 11):
    for j in range(1, 11):
        somme2 += i*j
    
# ==============================

for n in range(1, 16):    
    somme3 = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            somme3 += i**j
    print(f"{n}: {somme3}")
        
# ==============================

N = 0
M = 12
somme4 = 0

while somme4 < M:
    N += 1
    somme4 = 0
    for i in range(1, N+1):
        somme4 += i**2
        

print(N)

#%% Ex 10

sommeInit = 100
somme = sommeInit
taux = 0.043
annees = 0

while somme < 2*sommeInit:
    annees += 1
    somme += taux*somme
    
print(annees)

#%% Ex 11

x = 0
while x != "":
    x = input("Entrer un nombre: ")
    if x != "":
        x = int(x)
        print("Pair" if x%2==0 else "Impair")

#%% Ex 12

for i in range(64):
    print(f"Cas {i+1}: {2**i}")

#%% Ex 13

nb = random.randint(0, 1000)
essais = 10

x = -1
while x != nb and essais > 0:
    print(f"Il vous reste {essais} essais!")
    x = int(input("Devinez le nombre: "))
    if x > nb: 
        print("Trop grand")
    elif x < nb:
        print("Trop petit")
    
    essais -= 1

if x == nb:
    print("Bravo")
else:
    print(f"Dommage, la reponse etait {nb}")
    
#%% Ex 14


n = 1
diff = n

while diff > 10e-10:
    n += 1
    u = n**0.5
    v = (2*n+1)**0.5
    for i in range(n-1, 0, -1):
        u = (i+u)**0.5
        v = (i+v)**0.5
    diff = v - u
    
print(n)

#%% Ex 15

Ls = [2, -9, 7, 54, -8, 0]

nbNuls = 0
nbPos = 0
nbNeg = 0
somme = 0
sommeQuad = 0
emin = Ls[0]
emax = Ls[0]

for e in Ls:
    if e == 0: nbNuls += 1
    if e > 0: nbPos += 1
    if e < 0: nbNeg += 1    
    somme += e
    sommeQuad += e*e
    if e < emin: emin = e
    if e > emax: emax = e
    
print(f"Nuls: {nbNuls}")
print(f"Positifs: {nbPos}")
print(f"Negatifs: {nbNeg}")
print(f"Somme: {somme}")
print(f"Somme quadratique: {sommeQuad}")
print(f"Plus petit: {emin}")
print(f"Plus grand: {emax}")
    




















































