from not_shared.constants import key
import requests
import json
from os.path import exists
from file_name.file_name_utils import getFileName


def fetchAndSaveWeatherData(zip, startDate, endDate, aqi):
    sharedParams = {"q": zip, "dt": startDate, "end_dt": endDate, "aqi": aqi}

    params = {**sharedParams, "key": key}
    url = "http://api.weatherapi.com/v1/history.json"

    fileName = getFileName(sharedParams)

    if exists(fileName):
        print("raw data already obtained in " + fileName)
        return

    resp = requests.get(url=url, params=params)
    out_file = open(fileName, "w")
    data = resp.json()
    json.dump(data, out_file)
    print("raw data fetched and saved to " + fileName)
