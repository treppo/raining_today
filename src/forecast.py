import os
from datetime import datetime

import forecastio

def is_precip_type_rain(data_point):
    return data_point.precipType == 'rain'

def is_raining_in_any(data_points):
    return len(filter(is_precip_type_rain, data_points)) > 0

def remove_past(data_points):
    return data_points[datetime.now().hour - 1:]

def hourly_weather_for(location):
    api_key = os.environ['FORECASTIO_KEY']
    forecast = forecastio.load_forecast(api_key, location.lat, location.lon, datetime.today())
    return remove_past(forecast.hourly().data)

def is_raining(location):
    return is_raining_in_any(hourly_weather_for(location))
