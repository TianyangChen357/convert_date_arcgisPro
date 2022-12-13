'''
This script is to convert arcgis pro date time to excel date integer (starting from 1899/12/30, 0 )
'''

from datetime import datetime

def convert_txt_date(s):
    date_string = s
    date = datetime.strptime(date_string, '%Y/%m/%d’)
    return date

def convert_txt_date_int(s):
    date_string = s
    date = datetime.strptime(date_string, '%Y/%m/%d')
    delta= (date-datetime(1899,12,30)).days
    return delta

