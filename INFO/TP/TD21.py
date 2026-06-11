#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 08:20:26 2026

@author: zhuang@pedagogique.local
"""

inf = float('inf')

G = [
    [0, 1, 7, 3],
    [1, 0, 1, 5],
    [7, 1, 0, inf],
    [3, 5, inf, 0]
]

G2 = [
    [0, 3, 1, inf, inf, inf],
    [3, 0, 1, 2, inf, inf],
    [1, 1, 0, 3, 5, inf],
    [inf, 2, 3, 0, 1, 3],
    [inf, inf, 5, 1, 0, 1],
    [inf, inf, inf, 3, 1, 0]
]

def Floyd(G):
    dist = [[G[i][j] for j in range(len(G[i]))] for i in range(len(G))]

    for k in range(len(G)):
        for a in range(len(G)):
            for b in range(len(G)):
                if dist[a][k] + dist[k][b] < dist[a][b]:
                    dist[a][b] = dist[a][k] + dist[k][b]

    return dist

def Floyd_suivant(G):
    suivant = [[j for j in range(len(G[i]))] for i in range(len(G))]
    dist = [[G[i][j] for j in range(len(G[i]))] for i in range(len(G))]

    for k in range(len(G)):
        for a in range(len(G)):
            for b in range(len(G)):
                if dist[a][k] + dist[k][b] < dist[a][b]:
                    dist[a][b] = dist[a][k] + dist[k][b]
                    suivant[a][b] = suivant[a][k]

    return suivant

def Floyd_chemin(G, depart, arrivee):
    cur = depart
    suivant = Floyd_suivant(G)
    chemin = [depart]

    while suivant[cur][arrivee] != arrivee:
        s = suivant[cur][arrivee]
        chemin.append(s)
        cur = s

    chemin.append(arrivee)

    return chemin


def init(G, dep):
    return [G[dep][i] for i in range(len(G))]

def trouve_min(dist, Lsommets):
    smin = Lsommets[0]
    dmin = dist[smin]

    for sommet in Lsommets:
        if dist[sommet] < dmin:
            dmin = dist[sommet]
            smin = sommet
    return smin

def maj_distance(G, dist, a, b, Provenances):
    ndist = dist[a] + G[a][b]
    if ndist < dist[b]:
        dist[b] = ndist
        Provenances[b] = a


def Dijkstra(G, dep):
    dist = init(G, dep)
    Provenances = [-1 if G[dep][i] == inf else dep for i in range(len(G))]
    Q = [i for i in range(len(G))]
    while len(Q) > 0:
        a = trouve_min(dist, Q)
        Q.remove(a)
        for s in Q:
            if G[a][s] < inf:
                maj_distance(G, dist, a, s, Provenances)
    return dist, Provenances

def Dijkstra_chemin(G, dep, arrivee):
    dist, Provenances = Dijkstra(G, dep)
    chemininv = [arrivee]
    cur = arrivee
    while Provenances[cur] != dep:
        chemininv.append(Provenances[cur])
        cur = Provenances[cur]
    chemininv.append(dep)

    return [chemininv[i] for i in range(len(chemininv) - 1, -1, -1)]
































