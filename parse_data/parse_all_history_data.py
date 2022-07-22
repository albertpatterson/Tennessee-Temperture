from parse_data.parse_history_data import getLocTimeTempData
import os
import csv


def timesSame(t1s, t2s):
    if len(t1s) != len(t2s):
        return False

    for index in range(len(t1s)):
        if t1s[index] != t2s[index]:
            return False

    return True


dataFolder = "./raw_data/history"
historyDataPaths = os.listdir(dataFolder)

locs = []
times = []
data = []

for path in historyDataPaths:
    (lat, lon, time, temp_f) = getLocTimeTempData(dataFolder + "/" + path)
    locs.append([lon, lat])
    if len(times) == 0:
        times = time

    if not timesSame(times, time):
        print(times)
        print(time)
        raise Exception("time mismatch")

    if not len(times) == len(temp_f):
        print(times)
        print(temp_f)
        raise Exception("time temp count mismatch")

    data.append(temp_f)

locDataPath = "parsed_data/locations.csv"
with open(locDataPath, "w+") as locDataFile:
    writer = csv.writer(locDataFile)
    writer.writerow(["lon", "lat"])
    for loc in locs:
        print(loc)
        writer.writerow(loc)


tempDataPath = "parsed_data/temperature.csv"
with open(tempDataPath, "w+") as tempDataFile:
    writer = csv.writer(tempDataFile)
    writer.writerow(times)
    for datum in data:
        writer.writerow(datum)
