"""
Demo de  libImagedistance.py
"""

import matplotlib.pyplot as plt
from PIL import Image
from numpy import uint8 as np_uint8
from numpy import round as np_round
from libImageDistance import distance_segment


def _convert_8bits(img):
    """
    Convertit le résultat en array uint8 avec des valeurs
    comprises entre 0 et 255
    """
    res_8b = np_round(resultat).astype(np_uint8)
    res_8b[res_8b > 255] = 255
    return res_8b


if __name__ == "__main__":

    I_shape = (50, 100)
    segment_0 = (60, 5)
    segment_1 = (20, 40)
    resultat = distance_segment(segment_0, segment_1, I_shape)

    # affichage du résultat sur une figure matplotlib
    plt.figure()
    plt.imshow(resultat)
    plt.colorbar()
    plt.title("distance au segment %s - %s" % (segment_0, segment_1))
    plt.show()

    # enregistrement du résultat en images 8 et 16 bits
    Image.fromarray(resultat).save("distance_16b.tif")
    Image.fromarray(_convert_8bits(resultat)).save("distance_8b.tif")
