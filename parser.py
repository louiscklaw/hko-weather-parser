#!/usr/bin/env python3
import os,sys
import re

import html

from config import *


str_temp = ''

class hkoCurrentWeatherReport:
    str_rss = '';

    def _readRssFile(self,filepath):
        with open(filepath,'r') as f:
            return ''.join(f.readlines())

    def __init__(self, filepath):
        self.str_rss = self._readRssFile(filepath)

    def html_unescape(self, html_text):
        output = html_text.replace("&nbsp;",' ')
        return output

    def getDistrictRain(self, district, str_input):
        try:
            rain_mask = '.+'+district+'.+<td width="100" align="right">(.+)</td>.*'
            ms=re.findall(rain_mask, str_input)
            return self.html_unescape(ms[0])

        except Exception as e:
            print(str_input)
            raise e


    def getDistrictTemp(self, district, str_input):
        try:
            temp_mask = '.+'+district+'.+?(\d+) degrees'
            ms=re.findall(temp_mask, str_input)
            return self.html_unescape(ms[0])
        except Exception as e:
            print(str_input)
            print(district)
            raise e


    def getDistrictList(self):
        info_mask = '<tr><td><font size="-1">(.+)</font></td>.+</tr>'
        ms=re.findall(info_mask, self.str_rss)

        ms = sorted(ms)

        return ms

    def getDistrictReport(self, district):
        info_mask = '<tr>.+'+district+'.+</tr>'
        ms=re.findall(info_mask, self.str_rss)

        if len(ms)>1:
            return(self.getDistrictRain(district,ms[1]), self.getDistrictTemp(district,ms[0]))
        else:
            return('No rain', self.getDistrictTemp(district,ms[0]))

    def getDistrictReports(self):
        district_list = self.getDistrictList()

        district_report = {}
        for target_district in district_list:
            try:
                (rain, temp) = self.getDistrictReport(target_district)
                temp_d = {}
                temp_d[DICT_RAIN_NAME] = rain
                temp_d[DICT_TEMP_NAME] = temp
                district_report[target_district]=temp_d
                pass
            except Exception as e:
                print(target_district)
                raise(e)
                sys.exit()
                pass

        return district_report

    def helloworld(self):
        pass




test_rss_report = './dummy-html/currentweather.xml'

report = hkoCurrentWeatherReport(test_rss_report)

from pprint import pprint
pprint(report.getDistrictReports())
