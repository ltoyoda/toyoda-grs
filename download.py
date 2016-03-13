# Script created to get files from the internet
# Luciana Toyoda - TU Delft
# To be used in the master thesis, March 2016

# import urllib2
# response = urllib2.urlopen('https://data.knmi.nl/portal/KNMI-DataCentre.html#tab-detail=webservices')
# html = response.read()
# print html

import urllib
#
# testfile = urllib.URLopener()
# testfile.retrieve("http://randomsite.com/file.gz", "file.gz")
import os
import shutil
import wget
# wget.download('url')

text_file = open("weather_stations2.txt", "r")
# lines = text_file.readlines()
lines = text_file.read().split('\n')
# print lines
for station in lines:
    new_station = station.replace("\xb0", " ")
    new_station = new_station.replace("\x92", " ")


# print lines
print len(lines)
text_file.close()