import numpy as np
from interp.comb import allCombs


def dist(p1s, p2s):
    return np.sqrt(np.sum((p1s - p2s) ** 2, axis=2))


def getDists(pointSet1, pointSet2):
    return allCombs(pointSet1, pointSet2, dist)
