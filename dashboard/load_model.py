csv_filepathname="/Users/Joanne/Desktop/summer2015/me+programming/janacare/dashboard/Demographics_BIOCON.csv"
your_djangoproject_home="/Users/Joanne/Desktop/summer2015/me+programming/janacare/dashboard"

import sys,os 
import datetime
sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'dashboard.settings' 

from data_hospital.models import Demographics
from django.core.exceptions import ValidationError

import csv

dataReader = csv.reader(open(csv_filepathname, 'rU'), delimiter=',')

for row in dataReader:
	print row
	if row[13] != '':
		row[13] = datetime.datetime.strptime(row[13], "%m/%d/%y").date()#.strftime("%Y-%m-%d")
	creation = datetime.datetime.strptime(row[6], "%m/%d/%y").date()#.strftime("%Y-%m-%d")
	join = datetime.datetime.strptime(row[7], "%m/%d/%y").date()#.strftime("%Y-%m-%d")
	login = datetime.datetime.strptime(row[12], "%m/%d/%y").date()#.strftime("%Y-%m-%d")
	foodcount = Demographics()
	foodcount.email = row[0]
	foodcount.user_id = row[1]
	foodcount.first_name = row[2]
	foodcount.last_name = row[3]
	foodcount.username = row[4]
	foodcount.key= row[5]
	foodcount.date_joined = join
	foodcount.age = row[8]
	foodcount.weight = row[9]
	foodcount.height = row[10]
	foodcount.gender = row[11]
	foodcount.first_login = login
	foodcount.last_activity = row[13]
	foodcount.date_created = creation
	try:
		foodcount.save()
	except ValidationError as e:
		pass 