"""
Demo de  libImagedistance.py
"""

import matplotlib.pyplot as plt
from PIL import Image
from numpy import uint8 as np_uint8
from numpy import round as np_round
from libImageDistance import distance_segment

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
    img_16b = Image.fromarray(resultat)
    img_16b.save("distance_16b.tif")
    res_8b = np_round(resultat).astype(np_uint8)
    res_8b[res_8b > 255] = 255
    img_8b = Image.fromarray(res_8b)
    img_8b.save("distance_8b.tif")
