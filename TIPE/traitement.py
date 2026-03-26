from scipy import stats
from scipy.signal import find_peaks
import numpy as np

def calibration(longueurs, intensites):
    """
    Calibration lineaire des longueurs d'onde selon x. Envoie la fonction lineaire (a, b) pour longueur = a*(pixel) + b
    
    :param longueurs: liste des longueurs d'ondes attendue au pics
    :param intensites: liste des intensites lineaires
    """
    n = len(longueurs)

    min_distance = 20        # minimum separation between peaks (in index units)
    min_prominence = 10      # how "stand-out" a peak must be (tune this)

    peaks, props = find_peaks(intensites, distance=min_distance, prominence=min_prominence)
    if len(peaks) > n:
        order = np.argsort(props["prominences"])[::-1]
        peaks = peaks[order[:n]]

    peaks = np.sort(peaks)
    print(peaks)

    slope, intercept, r, p, se = stats.linregress(longueurs, peaks)

    return slope, intercept # type:ignore