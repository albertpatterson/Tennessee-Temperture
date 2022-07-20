from curses import raw
from datetime import datetime

from matplotlib import pyplot as plt
from file_name.file_name_utils import getParams
import json

fileName = "raw_data/history/q=38281&dt=2022-07-15&end_dt=2022-07-20&aqi=yes.json"

params = getParams(
    "raw_data/history/q=38281&dt=2022-07-15&end_dt=2022-07-20&aqi=yes.json"
)
file = open(fileName, "r")
rawData = json.load(file)


def parseRawHourData(rawHourData):
    parts = [
        "time",
        "temp_f",
        # "wind_mph",
        # "wind_degree",
        # "pressure_in",
        # "precip_in",
        # "humidity",
        # "dewpoint_f",
        # "chance_of_rain",
    ]

    parsed = {}
    for part in parts:
        parsed[part] = rawHourData[part]

    return parsed

    # time = rawHourData['time']
    # temp_f = rawHourData['temp_f']
    # wind_mph = rawHourData['wind_mph']
    # pressure_in = rawHourData['pressure_in']
    # precip_in = rawHourData['precip_in']
    # humidity = rawHourData['humidity']
    # dewpoint_f = rawHourData['dewpoint_f']
    # chance_of_rain = rawHourData['chance_of_rain']


def forcastToHour(dayData):
    rawHourData = dayData["hour"]
    hourData = list(map(parseRawHourData, rawHourData))
    return hourData


def getHourlyData(rawData):
    forecastDayData = rawData["forecast"]["forecastday"]
    daysData = list(map(forcastToHour, forecastDayData))
    return [datum for dayData in daysData for datum in dayData]


data = {
    "location": {
        "lat": rawData["location"]["lat"],
        "lon": rawData["location"]["lon"],
    },
    "data": getHourlyData(rawData),
}

print(data["data"])


def createDate(dateStr):
    print(dateStr)
    (date, time) = dateStr.split(" ")
    (year, month, day) = date.split("-")
    (hour, minute) = time.split(":")
    return datetime(int(year), int(month), int(day), int(hour), int(minute))


time = list(map(lambda datum: createDate(datum["time"]), data["data"]))
temp_f = list(map(lambda datum: datum["temp_f"], data["data"]))

plt.scatter(time, temp_f)
plt.show()
# print(time, temp_f)

# print(params)


# print(data)
