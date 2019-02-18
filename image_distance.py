"""
Calcul d'une image renvoyant pour chaque pixel la distance à une ligne
"""

import numpy as np
from skimage import draw
import matplotlib.pyplot as plt

def distance(pt, grid_y, grid_x):
    return np.sqrt((grid_y - pt[0]) ** 2 + (grid_x - pt[1]) ** 2)

if __name__ == "__main__":
    i_rows, i_cols = draw.line(40, 5, 5, 75)
    resultat = np.full((50, 100), np.inf)
    height, width = resultat.shape
    grid_y, grid_x = np.mgrid[0:height, 0:width]
    
    for pt in zip(i_rows, i_cols):
        image_dist = distance(pt, grid_y, grid_x)
        resultat[resultat > image_dist] = image_dist[resultat > image_dist]

    plt.figure()
    plt.imshow(resultat)
    plt.show()

