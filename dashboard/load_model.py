csv_filepathname="/Users/Joanne/Desktop/summer2015/me+programming/janacare/dashboard/food_count.csv"
your_djangoproject_home="/Users/Joanne/Desktop/summer2015/me+programming/janacare/dashboard"

import sys,os 
sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'dashboard.settings' 

from data_hospital.models import FoodCount

import csv

dataReader = csv.reader(open(csv_filepathname, 'rU'), delimiter=',')

for row in dataReader:
	foodcount = FoodCount()
	foodcount.username = row[0]
	foodcount.user_id = row[1]
	foodcount.num_days = row[2]
	foodcount.save()