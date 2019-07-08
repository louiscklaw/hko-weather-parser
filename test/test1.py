#!/usr/bin/env python3

import os, sys

from test_config import *
from hkoCurrentWeatherReport import *
from hkoWeatherForecast import *

test_result = TEST_OK

def test_get_district_weather():
    report = hkoCurrentWeatherReport(test_rss_report)
    if current_weather == report.getDistrictReports():
        print('test 1 ok')
    else:
        print('test 1 fail')

def test_get_humidity():
    report = hkoCurrentWeatherReport(test_rss_report)
    expected_humidity = '82'
    result = report.getHumidity()
    if expected_humidity == result:
        print('test getHumidity ok')
    else:
        print('test getHumidity fail')
        print(result)

def test_get_air_temperature():
    report = hkoCurrentWeatherReport(test_rss_report)
    expected_air_temp = '29'
    result = report.getAirTemperature()
    if expected_air_temp == result:
        print('test getAirTemperature ok')
    else:
        print('test getAirTemperature fail')
        print(result)

def test_get_uv():
    report = hkoCurrentWeatherReport(test_uv_report)
    expected_UV_reading = '6'
    result = report.getUVReading()
    if expected_UV_reading == result:
        print('test getUVReading ok')
    else:
        print('test getUVReading fail')
        print(result)

def test_get_uv_intensity():
    report = hkoCurrentWeatherReport(test_uv_report)
    expected_UV_reading = 'high'
    result = report.getUVIntensity()
    if expected_UV_reading == result:
        print('test getUVIntensity ok')
    else:
        print('test getUVIntensity fail')
        print(result)

def test_get_uv_without_uv_in_xml():
    report = hkoCurrentWeatherReport(test_uv_without_uv_xml)
    expected_UV_reading = 'very high'
    result = report.getUVIntensity()
    if expected_UV_reading == result:
        print('test test_get_uv_without_uv_in_xml ok')
    else:
        print('test test_get_uv_without_uv_in_xml fail')
        print(result)

def test_get_last_update():
    report = hkoCurrentWeatherReport(test_uv_report)
    expected_last_update = '11 a.m.'
    result = report.getLastUpdate()
    if expected_last_update == result:
        print('test getLastUpdate ok')
    else:
        print('test getLastUpdate fail')
        print(result)

class weather_forecast:
    def _get_new_hko_obj():
        return hkoWeatherForecast('./dummy-html/weatherforecast_1.xml')

    def test_helloworld():
        hkoWeatherForecast('./dummy-html/weatherforecast_1.xml').helloworld()

    def test_read_file():
        hko=hkoWeatherForecast('./dummy-html/weatherforecast_1.xml')
        if (len(hko.str_rss) >100):
            print("test_read_file ok")
        else:
            raise e

    def test_extract_content():
        hko=weather_forecast._get_new_hko_obj()
        if hko.extract_content().find('CDATA')>1:
            print("test_extract ok")
        else:
            raise e

    def test_extract_date():
        hko=weather_forecast._get_new_hko_obj()
        if len(hko.extract_date()) ==9:
            print("test extract date ok")
        else:
            raise e

current_weather_report_test_list =[
    test_get_district_weather,
    test_get_humidity,
    test_get_air_temperature,
    test_get_uv,
    test_get_uv_intensity,
    test_get_last_update,
    test_get_uv_without_uv_in_xml,
]

weather_forecast_list = [
    weather_forecast.test_helloworld,
    weather_forecast.test_read_file,
    weather_forecast.test_extract_content,
    weather_forecast.test_extract_date,
]

try:
    print("\n\ntesting current weather report:")

    for test_func in current_weather_report_test_list:
        test_func()

    print("\n\ntesting weather forecast")
    for test_func in weather_forecast_list:
        test_func()

except Exception as e:
    raise e
