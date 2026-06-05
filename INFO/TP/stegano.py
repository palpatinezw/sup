#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 08:27:04 2026

@author: zhuang@pedagogique.local
"""

import matplotlib.pyplot as plt
import numpy as np

def poids_fort(n):
    return n&0b11110000

def fort_vers_faible(n):
    return n >> 4

def image_fort(img):
    nouvimg = np.zeros_like(img)
    for i in range(len(img)):
        for j in range(len(img[i])):
            for k in range(3):
                nouvimg[i,j,k] = poids_fort(img[i,j,k])
    return nouvimg

def image_faible(img):
    nouvimg = np.zeros_like(img)
    for i in range(len(img)):
        for j in range(len(img[i])):
            for k in range(3):
                nouvimg[i,j,k] = fort_vers_faible(img[i,j,k])
    return nouvimg

def concatenantion(imgtronquee, imgdecalee):
    return imgtronquee + imgdecalee

def decryptage(img):
    nouvimg = np.zeros_like(img)
    for i in range(len(img)):
        for j in range(len(img[i])):
            for k in range(3):
                nouvimg[i,j,k] = img[i,j,k] << 4
    return nouvimg

# image_public = plt.imread("stegano/public.bmp")
# image_trunc = image_fort(image_public)

# image_secret = plt.imread("stegano/secret.bmp")
# secret_deca = image_faible(image_secret)

# image_finale = concatenantion(image_trunc, secret_deca)
# image_decrypte = decryptage(image_finale)

# plt.imsave("stegano/public_trunc.png", image_trunc)
# plt.imsave("stegano/secret_deca.png", secret_deca)
# plt.imsave("stegano/image_finale.png", image_finale)
# plt.imsave("stegano/image_decrypte.png", image_decrypte)

# ginettesecret = plt.imread("stegano/25_HuangZiwen.bmp")
# ginette_decrypte = decryptage(ginettesecret)
# plt.imsave("stegano/decrypte.png", ginette_decrypte)

image_public = plt.imread("stegano/sec/26_LaunayHenri.bmp")
image_dec = decryptage(image_public)
plt.imsave("stegano/sec/26_LaunayHenri.png", image_dec)

plt.show()






































