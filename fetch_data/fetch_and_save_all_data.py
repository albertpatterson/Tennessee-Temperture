from constants.zip_codes import tnZipCodes
from fetch_data.fetch_and_save import fetchAndSaveWeatherData
import time


def fetch_and_save_all():
    startDate = "2022-07-15"
    endDate = "2022-07-20"
    aqi = "yes"

    for zip in tnZipCodes:
        fetchAndSaveWeatherData(str(zip), startDate, endDate, aqi)
        time.sleep(1)
