import csv
from os import times
from datetime import datetime
from matplotlib import pyplot as plt
from load_data.load_data import temps, times

for tempRow in temps:
    plt.scatter(times, tempRow)
plt.show()
