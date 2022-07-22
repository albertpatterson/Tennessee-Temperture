import numpy as np
from load_data.load_data import temps, times, locs
from interp.interp import interpIDW
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.image as mpimg

nInterp = 100

points = np.array(list([np.array(r) for r in locs]))
lons = points.transpose()[0]
lats = points.transpose()[1]
values = np.array(temps).transpose()

minLon = -90.3
maxLon = -81.4
minLat = 34.85
maxLat = 36.75

minTemp = np.min(values)
maxTemp = np.max(values)

tenImg = mpimg.imread("images/ten.png")


def update(index):
    (XIS, YIS, ZIS) = interpIDW(
        points,
        values[index],
        minLon,
        maxLon,
        nInterp,
        minLat,
        maxLat,
        nInterp,
    )
    plt.clf()
    ax = plt.subplot(111, aspect=1)
    plt.imshow(tenImg, extent=[minLon, maxLon, minLat, maxLat], zorder=0)
    p = plt.pcolormesh(
        XIS, YIS, ZIS, vmin=minTemp, vmax=maxTemp, zorder=1, alpha=0.5, cmap="bwr"
    )
    stations = plt.scatter(
        lons, lats, marker=".", c="k", s=1, label="Stations", zorder=2, alpha=0.5
    )
    plt.legend(handles=[stations], loc="lower left", bbox_to_anchor=(0.8, 1))
    plt.title(times[index])
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    c = plt.colorbar(p, orientation="horizontal")
    c.set_label("Temperature")
    ax.set_position((0.1, 0.4, 0.85, 0.6))
    plt.gcf().set_size_inches(8, 3.3)


ani = FuncAnimation(plt.gcf(), update, frames=len(times))
ani.save("images/tn_temp.gif")
plt.show()
