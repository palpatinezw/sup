def estPresentDansListe(elt, L):
    """
        In: elt (int), L (liste d'entiers)
        Out: Bool
    """
    for x in L:
        if x == elt:
            return True
    return False

def positionDansListe(elt, L):
    """
        In: elt (int), L (liste d'entiers)
        Out: entier
    """
    for i in range(len(L)):
        if L[i] == elt:
            return i
    return -1

def estSansRepetition(L):
    """
        In: L (liste d'entiers)
        Out: Bool
    """
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[j] == L[i]: 
                return False
            
    return True

def Retire(A, x):
    """
        In: A (liste d'entiers), x (entier)
        Out: liste d'entiers
    """
    res = []
    for e in A:
        if e != x:
            res.append(e)
    return res

def Complementaire(n, B):
    """
        In: n (entier), B (liste d'entiers)
        Out: liste d'entiers
    """
    res = []
    for i in range(1, n+1):
        if not estPresentDansListe(i, B):
            res.append(i)
    return res

S1 = [
    [0,6,0,0,0,0,2,0,5],
    [4,0,0,9,2,1,0,0,0],
    [0,7,0,0,0,8,0,0,1],
    [0,0,0,0,0,5,0,0,9],
    [6,4,0,0,0,0,0,7,3],
    [1,0,0,4,0,0,0,0,0],
    [3,0,0,7,0,0,0,6,0],
    [0,0,0,1,4,6,0,0,2],
    [2,0,6,0,0,0,0,1,0]
]

def Colonne(S, j):
    """
        In: S (liste n x n), j (entier)
        Out: liste d'entiers
    """
    res = []
    for i in range(len(S)):
        res.append(S[i][j])
    return res

def Carre(S, k):
    """
        In: S (liste n x n), k (entier)
        Out: liste d'entiers
    """
    res = []
    for i in range(3 * (k//3), 3 * (k//3) + 3):
        for j in range(3 * (k % 3), 3 * (k % 3) + 3):
            res.append(S[i][j])
    return res

def LigneBienRemplie(S, i):
    """
        In: S (liste n x n), i (entier)
        Out: Bool
    """
    ligne = S[i]
    return len(Complementaire(9, ligne)) == 0

def ColonneBienRemplie(S, j):
    colonne = Colonne(S, j)
    return len(Complementaire(9, colonne)) == 0

def CarreBienRempli(S, k):
    carre = Carre(S, k)
    return len(Complementaire(9, carre)) == 0

def SudokuBienRempli(S):
    """
        In: S (liste n x n), i0 entier, j0 entier
        Out: bool
    """
    for i in range(9):
        if not (LigneBienRemplie(S, i) and ColonneBienRemplie(S, i) and CarreBienRempli(S, i)):
            return False
    return True

def ChiffresDansLigne(S, i0, j0):
    """
        In: S (liste n x n), i0 entier, j0 entier
        Out: liste d'entiers
    """
    res = []
    for j in range(9):
        if j == j0: 
            continue
        if S[i0][j] != 0:
            res.append(S[i0][j])
    return res

def ChiffresDansColonne(S, i0, j0):
    """
        In: S (liste n x n), i0 entier, j0 entier
        Out: liste d'entiers
    """
    res = []
    for i in range(9):
        if i == i0: 
            continue
        if S[i][j0] != 0:
            res.append(S[i][j0])
    return res

def ChiffresDansCarre(S, i0, j0):
    """
        In: S (liste n x n), i0 entier, j0 entier
        Out: liste d'entiers
    """
    res = []
    k = (i0//3)*3 + (j0//3)
    for i in range(3 * (k//3), 3):
        for j in range(3 * (k % 3), 3):
            if i == i0 and j == j0:
                continue
            if S[i0][j0] != 0:
                res.append(S[i0][j0])
    return res

def ChiffresOk(S, i0, j0):
    """
        In: S (liste n x n), i0 entier, j0 entier
        Out: liste d'entiers
    """

    return Complementaire(9, ChiffresDansLigne(S, i0, j0) + ChiffresDansColonne(S, i0, j0) + ChiffresDansCarre(S, i0, j0))

def NombrePossible(S, i0, j0):
    """
        In: S (liste n x n), i0 entier, j0 entier
        Out: entier
    """
    
    return len(ChiffresOk(S, i0, j0))

def unTour(S):
    modifie = False
    for i in range(9):
        for j in range(9):
            if NombrePossible(S, i, j) == 0:
                modifie = True
                S[i][j] = ChiffresOk[0]
    return (modifie, S)

def complete(S):
    (modifie, S0) = unTour(S)
    while modifie and not SudokuBienRempli(S0):
        (modifie, S0) = unTour(S)
    return S0



