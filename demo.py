"""
Demo de  libImagedistance.py
"""

import matplotlib.pyplot as plt
from libImageDistance import distance_segment

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

