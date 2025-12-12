import numpy as np
import matplotlib.pyplot as plt

j = complex(0, 1)

# ================================================
# Signaux d'entree
fs = 1000 # Hz
# Rang d'harmonique max
nmax = 5000 # Ne pas depasser 10000

# Sinusoide pur avec decalage
sin = {
    'N': np.array([1]),
    'amplitudesEntree': np.array([4]),
    'phasesEntree': np.array([0]),
    'a0': 1,
    'f0':fs
}
    
# Creneau : Que les harmoniques impaires pour le un creneau
Ncre = np.arange(1, nmax, 2)
creneau = {
    'N': Ncre,
    'amplitudesEntree': np.array([4/(np.pi * n) for n in Ncre]),
    'phasesEntree': np.array([3*np.pi/2 for n in Ncre]),
    'a0': 1,
    'f0':fs
}

# Dents de scie 
Nsawth = np.arange(1, nmax)
sawtooth = {
    'N': Nsawth,
    'amplitudesEntree': 4 * np.array([(2/np.pi) * ((-1)**(n+1)) * (1/n) for n in Nsawth]),
    'phasesEntree': np.array([3*np.pi/2 for n in Nsawth]),
    'a0': 0,
    'f0':fs
}

# Triangle : Que les harmoniques impaires pour le un creneau
Ntri = np.arange(1, nmax, 2)
triangle = {
    'N': Ntri,
    'amplitudesEntree': 4 * (8/(np.pi**2)) * np.array([((-1)**((n+1)//2)) * (1/(n**2)) for n in Ntri]),
    'phasesEntree': np.array([3*np.pi/2 for n in Ntri]),
    'a0': 0,
    'f0':fs
}

# =================================================

# Fonction de transferts

# Fonction nulle pour essai
def Hvide(f):
    return 1

# Passe bas 1er ordre
def Hpb1(f):
    # Frequence de coupure
    fc = 5e2 # Hz
    # Hasymp/max
    H0 = 1 
    return H0/(1+j*f/fc)

# Derivateur reel - E7 TD 6.2
def Hder(f):
    # Tests avec fs = 1e3, R = 1000, C=1e-6, r variable entre 0 et 1000
    R = 1000 # ohm
    C = 1e-3 # F
    r = 10 # ohm
    return -(j*R*C*2*np.pi*f)/(j*r*C*2*np.pi*f + 1)

# Rejecteur de bande - E6 TD Q9
def Hrej(f):
    R = 50000
    C = 3.2e-9
    w = 2*np.pi*f
    return (1 - R**2 * C**2 * w**2)/(1 - R**2 * C**2 * w**2 + 4 * j * R * C * w)

# =================================================
# Definir ici les parametres a conserver :
H = Hrej # Fonction de transfert
N, amplitudesEntree, phasesEntree, a0, f0 = (
    creneau[k] for k in ("N", "amplitudesEntree", "phasesEntree", "a0", "f0") # Signal
)

# =================================================
# Signaux d'entree

gain = np.array([np.abs(H(n*f0)) for n in N])
phase = np.array([np.angle(H(n*f0)) for n in N])

amplitudesSortie = gain*amplitudesEntree
phasesSortie = phase + phasesEntree
a0s = np.abs(H(0))*a0

# Graphe
t = np.linspace(0, 4/fs, 50000) # 10000 devrait suffire

e = np.array([a0  + np.sum(amplitudesEntree * np.cos(2 * np.pi * f0 * temps * N + phasesEntree)) for temps in t])
s = np.array([a0s + np.sum(amplitudesSortie * np.cos(2 * np.pi * f0 * temps * N + phasesSortie)) for temps in t])

plt.plot(t, e, 'r', label = 'entree', linewidth = 2)
plt.plot(t, s, 'k', label='sortie')
plt.legend()
plt.xlabel('temps (s)')
plt.ylabel('signaux')
plt.ticklabel_format(axis='x', style='sci', scilimits=(0,0))
plt.grid()
plt.show()
