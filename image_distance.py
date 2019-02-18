"""
Calcul d'une image renvoyant pour chaque pixel la distance à une ligne
"""

import numpy as np
from skimage import draw
import matplotlib.pyplot as plt

def _sqr_distance_pt(pt, grid_y, grid_x):
    return (grid_y - pt[0]) ** 2 + (grid_x - pt[1]) ** 2

def distance_segment(pt0, pt1, image_shape):
    i_rows, i_cols = draw.line(pt0[1], pt0[0], pt1[1], pt1[0])
    resultat = np.full((50, 100), np.inf)
    height, width = resultat.shape
    grid_y, grid_x = np.mgrid[0:height, 0:width]
    
    for pt in zip(i_rows, i_cols):
        image_dist = _sqr_distance_pt(pt, grid_y, grid_x)
        resultat[resultat > image_dist] = image_dist[resultat > image_dist]
    
    return np.sqrt(resultat)

if __name__ == "__main__":
    
    I_shape = (50, 100)
    segment_0 = (40, 5)
    segment_1 = (5, 75)
    resultat = distance_segment(segment_0, segment_1, I_shape)

    plt.figure()
    plt.imshow(resultat)
    plt.show()

