
filepathname="/Users/Joanne/desktop/summer2015/me+programming/janacare/food_count.csv"
djangoproject = "/Users/Joanne/desktop/summer2015/me+programming/janacare/dashboard"

import sys,os
sys.path.append(djangoproject)

from data_hospital.models import FoodCount
import csv
dataReader = csv.reader(open(filepathname), delimiter=',', quotechar='"')
for row in dataReader:
	if row[0] != 'username': # Ignore the header row, import everything else
		foodcount = FoodCount()
		foodcount.username = row[0]
		foodcount.user_id = row[1]
		foodcount.numdays = row[2]
		foodcount.save()

