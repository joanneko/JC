csv_filepathname="/Users/Joanne/Desktop/summer2015/me+programming/janacare/dashboard/glucose.csv"
your_djangoproject_home="/Users/Joanne/Desktop/summer2015/me+programming/janacare/dashboard"

import sys,os 
sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'dashboard.settings' 

from data_hospital.models import GlucoseCount

import csv

dataReader = csv.reader(open(csv_filepathname, 'rU'), delimiter=',')

for row in dataReader:
	if row[0] != 'username': # Ignore the header row, import everything else
		foodcount = GlucoseCount()
		foodcount.username = row[0]
		foodcount.user_id = row[1]
		foodcount.num_values = row[2]
		foodcount.save()