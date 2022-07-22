import csv
from os import times
from datetime import datetime
from matplotlib import pyplot as plt

locDataPath = "parsed_data/locations.csv"
tempDataPath = "parsed_data/temperature.csv"

locs = []
times = []
temps = []

with open(locDataPath, "r") as locDataFile:
    reader = csv.reader(locDataFile)
    isHeader = True
    for row in reader:
        if isHeader:
            isHeader = False
            continue
        locRow = list(map(float, row))
        locs.append(locRow)


with open(tempDataPath, "r") as tempDataFile:
    reader = csv.reader(tempDataFile)
    isHeader = True
    for row in reader:
        if isHeader:
            isHeader = False
            timeStrs = row
            times = list(
                map(lambda s: datetime.strptime(s, "%Y-%m-%d %H:%M:%S"), timeStrs)
            )
            continue

        tempRow = list(map(float, row))

        temps.append(tempRow)
