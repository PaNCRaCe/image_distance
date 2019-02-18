"""
Calcul d'une image renvoyant pour chaque pixel la distance à un segment
"""

import numpy as np
from skimage import draw
import matplotlib.pyplot as plt


def _sqr_distance_pt(pt, grid_y, grid_x):
    """
    calcul du carré de la distance à un point pour chaque pixel
    """
    return (grid_y - pt[0]) ** 2 + (grid_x - pt[1]) ** 2


def distance_segment(pt0, pt1, image_shape):
    """
    calcul de la distance minimale à un segment (en pixels) pour
    chaque pixel de l'image
    - pt0, pt1 : extrémités du segment
    - image_shape : dimensions de l'image

    resultat : image (float)
    """

    i_rows, i_cols = draw.line(pt0[1], pt0[0], pt1[1], pt1[0])
    resultat = np.full(image_shape, np.inf)
    height, width = image_shape

    # images des abcisses et ordonnées
    grid_y, grid_x = np.mgrid[0:height, 0:width]

    # pour chaque pt du segment, calcul des distances et de la distance minimale
    for pt in zip(i_rows, i_cols):
        image_dist = _sqr_distance_pt(pt, grid_y, grid_x)
        resultat[resultat > image_dist] = image_dist[resultat > image_dist]

    return np.sqrt(resultat)


if __name__ == "__main__":

    I_shape = (50, 100)
    segment_0 = (60, 5)
    segment_1 = (20, 40)
    resultat = distance_segment(segment_0, segment_1, I_shape)

    plt.figure()
    plt.imshow(resultat)
    plt.colorbar()
    plt.title("distance au segment %s - %s" % (segment_0, segment_1))
    plt.show()

