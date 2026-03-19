#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 22 08:21:23 2026

@author: zhuang@pedagogique.local
"""
import matplotlib.pyplot as plt
import numpy as np
import cmath

filepath = "/run/user/759617665/gvfs/smb-share:server=192.168.3.200,share=zhuang$/Python/TP/TD13fichiers/"

#%%

fichier = open(filepath+"notes.txt","r")
contenu = fichier.read()
fichier.close()

contenu = contenu.split("\n")
notes = []
for note in contenu:
    notes.append(note.split("\t"))
    
notes.remove(notes[0])
for note in notes:
    note[1] = float(note[1].replace(",", "."))
    
somme  = 0

for note in notes:
    somme += note[1]
    
print("Moyenne: ", round(somme/len(notes), 1))


#%% ===========================================================================

fichier = open(filepath+"data_airports.txt","r")
contenu = fichier.read()
fichier.close()

airports = []
long = []
lat = []
temp = []
for ligne in contenu.split("\n")[1:]:
    lignedonne = ligne.split("\t")
    airports.append({
        'long':float(lignedonne[0]),
        'lat':float(lignedonne[1]),
        'temp':float(lignedonne[2])
    })

for airport in airports:
    long.append(airport['long'])
    lat.append(airport['lat'])
    temp.append(airport['temp'])

plt.scatter(long, lat, c=temp, s=20, cmap="coolwarm")
plt.show()


# %% ==========================================================================

#Ouverture du fichier Filtre_passe_bande2016.txt
#Instanciation de l'objet Fichier de la classe file

# Question 3 : à ccompléter 

fichier = open(filepath+"Filtre_passe_bande.txt","r")
chaine = fichier.read()
fichier.close()

#Question 4 : à commenter

tableau = chaine.split('\n')[1:] # liste de str
                    
for i  in range(len(tableau)):
    tableau[i] = tableau[i].strip().split('\t') # [f, H, gain, phase] en str


#Question 4 : à commenter et à compléter (Phase)
nb_ligne = len(tableau)
nb_colonne = len(tableau[0])

f = [tableau[ligne][0] for ligne in range(nb_ligne)] # liste de str         
H = [tableau[ligne][1] for ligne in range(nb_ligne)] # liste de str
phase = [tableau[ligne][3] for ligne in range(nb_ligne)]

f = [float(elem) for elem in f] # liste de float (f en Hz)
H = [elem.replace(',','.') for elem in H] # liste de str
phase = [float(e.replace(',','.')) for e in phase] 

H = [float(elem) for elem in H] # liste de float

G = [20*np.log10(elem) for elem in H] # liste de float (gain en dB)

#Questions 6 à 9 - à compléter.

resId = 0
for i in range(nb_ligne):
    if G[i] > G[resId]:
        resId = i
f0 = f[resId] # Hz
Gmax = G[resId] # dB

Gc = Gmax - 3 # dB
c1 = 0
c2 = 0
for i in range(nb_ligne):
    if G[i] > Gc and G[i-1] < Gc:
        c1 = f[i]
    if G[i] < Gc and G[i-1] > Gc:
        c2 = f[i]
deltaf = c2 - c1 # Hz
Q = f0 / deltaf

R = 100 # ohm
L = 50e-3 # H
C = 47e-9 # F
omega0theo = 1 / ((L * C)**(0.5))
Qtheo = (1/R) * ((L/C)**(0.5))

asympBF = [Gmax - 20*np.log10(Q) + 20*np.log10(curf/f0) for curf in f]
asympHF = [Gmax - 20*np.log10(Q) - 20*np.log10(curf/f0) for curf in f]

diff = abs(asympBF[0] - asympHF[0])
asympResId = 0
for i in range(nb_ligne):
    if abs(asympBF[i] - asympHF[i]) < diff:
        asympResId = i
        diff = abs(asympBF[i] - asympHF[i])

asympf0 = f[asympResId]
asympQ = 10**((Gmax - ((asympBF[asympResId] + asympHF[asympResId])/2) ) /20)

plt.figure(1)
plt.semilogx(f, G)
plt.semilogx(f[:asympResId], asympBF[:asympResId], linestyle="--", color='green') # asymp BF
plt.semilogx(f[asympResId:], asympHF[asympResId:], linestyle="--", color='green') # asymp HF
plt.semilogx(f, [20*np.log10(1 / (np.sqrt( 1 + ( Qtheo * ((2*np.pi*curf / omega0theo) - (omega0theo / (2*np.pi*curf)) ) )**2 ) )) for curf in f]) # courbe theorique
plt.grid(which="both", color="0.65", linestyle="-")

plt.figure(2)
plt.semilogx(f, phase)
plt.semilogx(f, [cmath.phase(1 / ( 1 + complex(0, 1)*( Qtheo * ((2*np.pi*curf / omega0theo) - (omega0theo / (2*np.pi*curf)) )  ) ) ) for curf in f]) # courbe theorique
plt.grid(which="both", color="0.65", linestyle="-")

plt.show()
















































