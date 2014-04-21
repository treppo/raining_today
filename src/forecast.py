import os

from datetime import datetime

import forecastio

def is_precip_type_rain(data_point):
    return data_point.precipType == 'rain'

def is_raining_in_any(data_points):
    len(filter(is_precip_type_rain, data_points)) > 0

def is_raining(coordinates):
    api_key = os.environ['FORECASTIO_KEY']
    lat, lng = coordinates.split(',')
    forecast = forecastio.load_forecast(api_key, lat, lng, datetime.today())

    return is_raining_in_any(forecast.hourly().data)
