#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 08:21:34 2026

@author: zhuang@pedagogique.local
"""

import matplotlib.pyplot as plt
import numpy as np

imgpath ="/run/user/759617665/gvfs/smb-share:server=192.168.3.200,share=zhuang$/Python/TP/images"

picasso = plt.imread(imgpath + "/picasso.png")
matisse = plt.imread(imgpath + "/matisse.png")

def symetrie(img):
    """
        In: tableau image
        Out: tableau image
    """
    newimg = []
    for row in img:
        nrow = []
        for i in range(len(row) - 1, -1, -1):
            nrow.append(row[i])
        newimg.append(nrow)

    return np.array(newimg)
    
def rotationQT(img):
    """
        In: tableau image
        Out: tableau image
    """
    newimg = np.zeros((img.shape[1], img.shape[0], img.shape[2]))
    p = img.shape[0]
    q = img.shape[1]
    for x in range(p):
        for y in range(q):
            newimg[y][p - x - 1] = img[x][y]
    return newimg

def blit(img):
    """
        In: tableau image carre
        Out: tableau image
    """
    h = img.shape[0]
    l = img.shape[1]
    if h == 1 and l == 1:
        return img
    newimg = np.zeros_like(img)
    
    blocA = img[:(h//2),:(l//2)]
    blocB = img[:(h//2),(l//2):]
    blocC = img[(h//2):,:(l//2)]
    blocD = img[(h//2):,(l//2):]
    
    blocAblit = blit(blocA)
    blocBblit = blit(blocB)
    blocCblit = blit(blocC)
    blocDblit = blit(blocD)
    
    newimg[:(h//2),:(l//2)] = blocBblit
    newimg[:(h//2),(l//2):] = blocDblit
    newimg[(h//2):,:(l//2)] = blocAblit
    newimg[(h//2):,(l//2):] = blocCblit
    
    return newimg

def ordre(fct, img):
    """
        In: fonction; tableau image
        Out: entier
    """
    c = 1
    newimg = fct(img)
    while not (img == newimg).all():
        newimg = fct(newimg)
        c += 1
    return c

def photomaton(img):
    """
        In: tableau image carre
        Out: tableau image
    """
    newimg = np.zeros_like(img)
    p = img.shape[0]
    q = img.shape[1]
    for x in range(p):
        for y in range(q):
            newimg[x//2 + (p//2)*(x%2)][y//2 + (q//2)*(y%2)] = img[x][y]
    return newimg

def periode_photomaton(img):
    """
        In: tableau image carre
        Out: entier
    """
    c = 1
    
    p = img.shape[0]
    q = img.shape[1]
    while ((2**c - 1) % (p-1) != 0) or ((2**c - 1) % (q-1) != 0):
        c+=1
        
    return c

def photomaton2(img, n):
    """
        In: tableau image; n
        Out: tableau image
    """
    npic = np.copy(img)
    for i in range(n):
        npic = photomaton(npic)
    return npic

def aplatie(img):
    """
        In: tableau image
        Out: tableau image
    """
    p = img.shape[0]
    q = img.shape[1]
    newimg = np.zeros((p//2, 2*q, img.shape[2]))
    
    for x in range(p):
        for y in range(q):
            newimg[x//2][y*2 + (x%2)] = img[x][y]
    return newimg

def boulanger(img):
    """
        In: tableau image
        Out: tableau image
    """
    p = img.shape[0]
    q = img.shape[1]
    newimg = np.zeros_like(img)
    
    inter = aplatie(img)
    pg = inter[:,:q]
    pd = inter[:,q:]
    pd = rotationQT(pd)
    pd = rotationQT(pd)
    
    newimg[:(p//2), :] = pg
    newimg[(p//2):, :] = pd
    
    return newimg

def coord_boul(x, y, p, q):
    """
        In: x entier; y entier; p entier; q entier
        Out: (entier, entier)
    """
    x1 = x//2
    y1 = y*2 + (x%2)
    
    if y1 < q:
        return (x1, y1)
    else:
        return (p - x1 - 1, 2 * q - y1 - 1)


plt.imshow(picasso)
transf = boulanger(picasso)
for i in range(17):
    transf = boulanger(transf)    
    plt.figure()
    plt.imshow(transf)




































































