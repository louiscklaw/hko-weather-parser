#!/usr/bin/env python3
import re


# district_name
DISTRICT_HONG_KONG_OBSERVATORY='Hong Kong Observatory'
DISTRICT_KING_S_PARK='King\'s Park'
DISTRICT_WONG_CHUK_HANG='Wong Chuk Hang'
DISTRICT_TA_KWU_LING='Ta Kwu Ling'
DISTRICT_LAU_FAU_SHAN='Lau Fau Shan'
DISTRICT_TAI_PO='Tai Po'
DISTRICT_SHA_TIN='Sha Tin'
DISTRICT_TUEN_MUN='Tuen Mun'
DISTRICT_TSEUNG_KWAN_O='Tseung Kwan O'
DISTRICT_SAI_KUNG='Sai Kung'
DISTRICT_CHEK_LAP_KOK='Chek Lap Kok'
DISTRICT_TSING_YI='Tsing Yi'
DISTRICT_SHEK_KONG='Shek Kong'
DISTRICT_TSUEN_WAN_HO_KOON='Tsuen Wan Ho Koon'
DISTRICT_TSUEN_WAN_SHING_MUN_VALLEY='Tsuen Wan Shing Mun Valley'
DISTRICT_HONG_KONG_PARK='Hong Kong Park'
DISTRICT_SHAU_KEI_WAN='Shau Kei Wan'
DISTRICT_KOWLOON_CITY='Kowloon City'
DISTRICT_HAPPY_VALLEY='Happy Valley'
DISTRICT_WONG_TAI_SIN='Wong Tai Sin'
DISTRICT_STANLEY='Stanley'
DISTRICT_KWUN_TONG='Kwun Tong'
DISTRICT_SHAM_SHUI_PO='Sham Shui Po'
DISTRICT_KAI_TAK_RUNWAY_PARK='Kai Tak Runway Park'
DISTRICT_YUEN_LONG_PARK='Yuen Long Park'
DISTRICT_TAI_MEI_TUK='Tai Mei Tuk'

# name used in extracted report
DICT_RAIN_NAME = 'rain'
DICT_TEMP_NAME = 'temp'

str_temp = ''

class hkoCurrentWeatherReport:
    str_rss = '';

    def _readRssFile(self,filepath):
        with open(filepath,'r') as f:
            return ''.join(f.readlines())

    def __init__(self, filepath):
        self.str_rss = self._readRssFile(filepath)

    def getDistrictRain(self, district, str_input):
        try:
            rain_mask = '.+'+district+'.+<td width="100" align="right">(.+)</td>.*'
            ms=re.findall(rain_mask, str_input)
            return ms[0]
            pass
        except Exception as e:
            print(str_input)
            pass


    def getDistrictTemp(self, district, str_input):
        try:
            temp_mask = '.+'+district+'.+?(\d+) degrees'
            ms=re.findall(temp_mask, str_input)
            return ms[0]
        except Exception as e:
            print(str_input)
            print(district)
            raise e


    def getDistrictReport(self, district):
        info_mask = '<tr>.+'+district+'.+</tr>'
        ms=re.findall(info_mask, self.str_rss)

        return(self.getDistrictRain(district,ms[1]), self.getDistrictTemp(district,ms[0]))

    def getDistrictReports(self):
        district_list = [DISTRICT_TAI_PO, DISTRICT_SHA_TIN]
        district_report = {}
        for target_district in district_list:
            (rain, temp) = self.getDistrictReport(target_district)
            temp_d = {}
            temp_d[DICT_RAIN_NAME] = rain
            temp_d[DICT_TEMP_NAME] = temp
            district_report[target_district]=temp_d

        return district_report

    def helloworld(self):
        pass




test_rss_report = './dummy-html/currentweather.xml'

report = hkoCurrentWeatherReport(test_rss_report)

from pprint import pprint
pprint(report.getDistrictReports())
