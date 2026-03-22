from analyse_img import extraction_intensite
from traitement import calibration
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

bande = (40, 100) # bande d'extraction par defaut

m = 0
c = 0

def pixelToLongueur(pxl):
    return m*pxl + c

def ajusterBande(l, h, sample=None):
    """
        Ajuster la bande d'extraction (1). 

        :param l: pixel limite bas (en haute position)
        :param h: pixel limite haut (en basse position)
        :param sample: image example pour visualiser la nouvelle bande
    """
    global bande 
    bande = (l, h)
    if sample:
        extraction_intensite(sample, l, h, debug=True)
    print(f"Bande: [ {l} , {h} ]")

# e.g. calibrer("img/samplecalib.png", [405, 532, 650])
def calibrer(img, pics):
    """
        Calibration des longueurs d'onde en fonction des pixels. Calibration effectuée à partir de la bande (1)

        :param img: chemin de l'image de calibratoin
        :param pics: liste des longueurs d'onde des pics attendus
    """
    intensite, r, g, b = extraction_intensite(img, bande[0], bande[1])
    res = calibration(pics, intensite)
    global m
    global c
    m = res[0]
    c = res[1]
    print(f"Calibration effectuée: {m}*x + {c}")

def analyse(img):
    """
        Analyse simple d'un seul spectre

        :param img: chemin de l'image à analyser
    """
    if m == 0:
        print("Analyse non effectuée - erreur de calibration")
        return
    intensite, r, g, b = extraction_intensite(img, bande[0], bande[1])
    now = datetime.now()
    resultatstr = f"Extraction [ {img} ] effectuee {str(now)}\n"
    resultatstr += f"Calibration: {m}*x + {c}\n\n"
    resultatstr += f"pixel, longueur d'onde, intensite, r, g, b\n"
    for i in range(len(intensite)):
        resultatstr += f"{i}, {pixelToLongueur(i)}, {intensite[i]}, {r[i]}, {g[i]}, {b[i]}\n"
    with open(f"out/resultat_{now.strftime("%Y%m%d-%H%M%S")}.txt", "w") as f:
        f.write(resultatstr)

    print(f"Analyse simple effectuée [ out/resultat_{now.strftime("%Y%m%d-%H%M%S")}.txt ]")

def parse(filename):
    """
    Reads a spectrum output file and returns structured numpy arrays.

    :param filename: path to the .txt file
    :return: dict with keys {intensities, r, g, b, longueurs}
    """
    intensities = []
    r_vals = []
    g_vals = []
    b_vals = []
    longueur = []

    with open(filename, "r") as f:
        lines = f.readlines()

    # Find the start of the data table
    start_idx = None
    for i, line in enumerate(lines):
        if line.strip().startswith("pixel"):
            start_idx = i + 1
            break

    if start_idx is None:
        raise ValueError("Invalid file format: no data header found")

    # Parse data lines
    for line in lines[start_idx:]:
        line = line.strip()
        if not line:
            continue

        parts = [p.strip() for p in line.split(",")]
        if len(parts) != 6:
            continue  # skip malformed lines

        _, wavelength, intensity, r, g, b = parts

        longueur.append(float(wavelength))
        intensities.append(float(intensity))
        r_vals.append(float(r))
        g_vals.append(float(g))
        b_vals.append(float(b))

    return {
        "intensities": np.array(intensities),
        "r": np.array(r_vals),
        "g": np.array(g_vals),
        "b": np.array(b_vals),
        "longueurs": np.array(longueur),
    }