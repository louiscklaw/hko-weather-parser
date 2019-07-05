#!/usr/bin/env python3

import os, sys

PWD = os.path.dirname(os.path.abspath(__file__))
PROJ_HOME = os.path.join(PWD,'..')

SRC_PATH = os.path.join(PROJ_HOME,'src')
TEST_PATH = os.path.join(PROJ_HOME,'test')
DUMMY_HTML_PATH = os.path.join(PROJ_HOME, 'dummy-html')

sys.path.append(SRC_PATH)

from hkoCurrentWeatherReport import *

test_rss_report = os.path.join(DUMMY_HTML_PATH,'currentweather.xml')

current_weather = {'Chek Lap Kok': {'rain': 'No rain', 'temp': '30'}, 'Happy Valley': {'rain': 'No rain', 'temp': '29'}, 'Hong Kong Observatory': {'rain': 'No rain', 'temp': '29'}, 'Hong Kong Park': {'rain': 'No rain', 'temp': '29'}, 'Kai Tak Runway Park': {'rain': 'No rain', 'temp': '29'}, "King's Park": {'rain': 'No rain', 'temp': '28'}, 'Kowloon City': {'rain': '0 to 1 mm;', 'temp': '28'}, 'Kwun Tong': {'rain': 'No rain', 'temp': '29'}, 'Lau Fau Shan': {'rain': 'No rain', 'temp': '28'}, 'Sai Kung': {'rain': 'No rain', 'temp': '30'}, 'Sha Tin': {'rain': '0 to 1 mm;', 'temp': '29'}, 'Sham Shui Po': {'rain': '0 to 1 mm;', 'temp': '28'}, 'Shau Kei Wan': {'rain': 'No rain', 'temp': '29'}, 'Shek Kong': {'rain': 'No rain', 'temp': '29'}, 'Stanley': {'rain': 'No rain', 'temp': '29'}, 'Ta Kwu Ling': {'rain': 'No rain', 'temp': '28'}, 'Tai Mei Tuk': {'rain': 'No rain', 'temp': '27'}, 'Tai Po': {'rain': '0 to 1 mm;', 'temp': '28'}, 'Tseung Kwan O': {'rain': 'No rain', 'temp': '28'}, 'Tsing Yi': {'rain': 'No rain', 'temp': '28'}, 'Tsuen Wan Ho Koon': {'rain': 'No rain', 'temp': '27'}, 'Tsuen Wan Shing Mun Valley': {'rain': 'No rain', 'temp': '28'}, 'Tuen Mun': {'rain': 'No rain', 'temp': '29'}, 'Wong Chuk Hang': {'rain': 'No rain', 'temp': '29'}, 'Wong Tai Sin': {'rain': 'No rain', 'temp': '29'}, 'Yuen Long Park': {'rain': 'No rain', 'temp': '29'}}


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
        print('test humidity ok')
    else:
        print('test humidity fail')
        print(result)

test_get_district_weather()
test_get_humidity()
