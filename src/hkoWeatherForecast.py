#!/usr/bin/env python3

import os,sys
import re

import html

from config import *

str_temp=''

class hkoWeatherForecast:
    str_rss=''

    def _readRssFile(self, filepath):
        with open(filepath, 'r') as f:
            return ''.join(f.readlines())

    def __init__(self, filepath):
        self.str_rss = self._readRssFile(filepath)

    def helloworld(self):
        print("helloworld")
        return "helloworld"

    def extract_by_key(self, str_input, str_key):
        try:
            pattern = "%s(.+?)<br/>" % str_key
            ms = re.findall(pattern, str_input, re.DOTALL)
            return ms[0].strip()
        except Exception as e:
            raise e

    def extract_content(self):
        ms = re.findall("<description>(.+?)</description>", self.str_rss, re.DOTALL)
        return ms[1]

    def extract_date(self):
        ms = re.findall("Date/Month.+?Cent<br/>", self.str_rss, re.DOTALL)
        return ms

    def get_wind(self, date_advance):
        str_temp = self.get_indiviual_date(date_advance)
        return self.extract_by_key(str_temp, "Wind:")

    def get_weather(self, date_advance):
        str_temp = self.get_indiviual_date(date_advance)
        return self.extract_by_key(str_temp, "Weather:")

    def get_temp_range(self, date_advance):
        str_temp = self.get_indiviual_date(date_advance)
        str_temp = self.extract_by_key(str_temp, "Temp range:").replace("C","").replace("\n\t\t","").replace(" ","")
        return str_temp

    def get_rh_range(self, date_advance):
        str_temp = self.get_indiviual_date(date_advance)
        str_temp = self.extract_by_key(str_temp, "R.H. range:").replace("\n\t\t","")
        str_temp = str_temp.replace("per Cent",'').replace(" ",'').strip()
        # print(str_temp)
        # sys.exit()
        return str_temp

    def get_indiviual_date(self, date_advance):
        return self.extract_date()[date_advance]
