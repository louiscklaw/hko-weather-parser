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

    def extract_content(self):
        ms = re.findall("<description>(.+?)</description>", self.str_rss, re.DOTALL)
        return ms[1]

    def extract_date(self):
        ms = re.findall("Date/Month.+?Cent<br", self.str_rss, re.DOTALL)
        return ms

    def get_indiviual_date(self, date_advance):
        return self.extract_date()[date_advance]
