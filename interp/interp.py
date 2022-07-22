import numpy as np

from interp.comb import allCombs


def dist(p1s, p2s):
    return np.sum((p1s - p2s) ** 2, axis=2) ** 1


def getDists(pointSet1, pointSet2):
    return allCombs(pointSet1, pointSet2, dist)


def interpIDW(samplesPoints, sampleValues, xmin, xmax, xn, ymin, ymax, yn):
    xis = np.linspace(xmin, xmax, xn)
    yis = np.linspace(ymin, ymax, yn)
    (XIS, YIS) = np.meshgrid(xis, yis)
    iPoints = np.transpose(np.vstack((XIS.ravel(), YIS.ravel())))
    iDists = getDists(samplesPoints, iPoints) + 1e-9
    inv = 1 / iDists
    zCol = np.reshape(sampleValues, (sampleValues.size, 1))
    num = np.matmul(inv, zCol)
    den = np.matmul(inv, np.ones((sampleValues.size, 1)))
    zis = num / den
    return (XIS, YIS, np.reshape(zis, XIS.shape))
