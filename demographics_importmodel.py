from django.db import models
import datetime

# Create your models here.
class FoodCount(models.Model): 
	username = models.CharField(max_length=30)
	user_id =  models.IntegerField(primary_key=True)
	num_days = models.IntegerField()

	def __unicode__(self):
		return self.username

class GlucoseCount(models.Model):
	username = models.CharField(max_length = 30)
	user_id = models.IntegerField(primary_key=True)
	num_values = models.IntegerField()

	def __unicode__(self):
		return self.username

class Demographics(models.Model):
	email = models.CharField(max_length = 50)
	user_id = models.IntegerField(primary_key = True)
	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length=30)
	username = models.CharField(max_length=30)
	key = models.CharField(max_length=30)
	date_created = models.DateField()
	date_joined = models.DateField()
	age = models.IntegerField()
	weight = models.FloatField()
	height = models.IntegerField()
	gender = models.CharField(max_length = 10)
	first_login = models.DateField()
	last_activity = models.DateField(blank=True, null=True)



