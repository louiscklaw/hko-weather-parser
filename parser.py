#!/usr/bin/env python3

import xml.etree.ElementTree as ET
tree = ET.parse('./dummy-html/currentweather.xml')
root = tree.getroot()

description_cdata = root.findall('channel')[0].findall('item')[0].findall('description')[0].text
print(description_cdata)
