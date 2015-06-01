from django.shortcuts import render_to_response 
from data_hospital.models import FoodCount, GlucoseCount, Demographics, RegionDoctors
import csv 
import json
from collections import Counter
# this puts info in database 

# def home(request): 
# 	arr = []
# 	with open('food_count.csv', 'rU') as csvfile:
# 		foodreader = csv.reader(csvfile)	
# 		for row in foodreader:
# 			arr.append(row)
# 	for each in arr:
# 		tmp = FoodCount()
# 		tmp.username = each[0]
# 		tmp.user_id = each[1]
# 		tmp.num_days = each[2]
# 		tmp.save()
# 	return render_to_response('home.html', locals())


def home(request):
	food_obj = FoodCount.objects.order_by('num_days')
	glucose_obj = GlucoseCount.objects.order_by('num_values')
	food_unfiltered_arr = []
	glucose_arr = []

	for i in range(0, len(food_obj)): 
		food_unfiltered_arr.append(food_obj[i].num_days)

	for i in range(0, len(glucose_obj)):
		glucose_arr.append(glucose_obj[i].num_values)

	food_labels = []
	food_counts = []

	for item in food_unfiltered_arr: 
		if item not in food_labels: 
			food_labels.append(item)
			food_counts.append(1)
		else:
			instance = food_labels.index(item)
			food_counts[instance] = food_counts[instance] + 1

	average_glucose = sum(glucose_arr) / len(glucose_arr)

	glucose_val = []
	for item in glucose_arr:
		instance = next((val for val in glucose_val if val["label"] == item), None)
		if instance not in glucose_val: 
			glucose_val.append({'label' : item, 'value' : 1})
		else:
			new_val = instance["value"] + 1
			index = glucose_val.index(instance)
			glucose_val[index] = {'label' : item, 'value' : new_val}


	# for item in unfiltered_arr:
	# 	instance = next((val for val in dict_array if val["key"] == item), None)
	# 	if instance not in dict_array:
	# 		dict_array.append({'key' : item, 'value' : 1 })  
	# 	else:
			
			# new_val = instance["value"] + 1
			# index = dict_array.index(instance) 
			# dict_array[index] = {'key': item, 'value' : new_val}

	return render_to_response('home.html', {'unfiltered_array' : food_unfiltered_arr, 'food_labels' : food_labels, 'food_counts' : food_counts, 'glucose' : glucose_val, 'avg_glu' : average_glucose})


def example(request):
	all_people = Demographics.objects.all()
	all_males = Demographics.objects.filter(gender='M')
	all_females = Demographics.objects.filter(gender='F')

	male_bmi = []
	female_bmi = []
	male_age = []
	female_age = []

	for item in all_males:
		male_bmi.append( item.weight / ((item.height / 100.)**2) )
		male_age.append(item.age)

	for item in all_females:
		female_bmi.append( item.weight / ((item.height / 100.)**2) )
		female_age.append(item.age) 


	all_bmi = female_bmi + male_bmi 

	female_age = filter(lambda x : x >= 18 and x < 100, female_age)
	male_age = filter(lambda x : x >= 18 and x < 100, male_age)
	all_age = dict(Counter(female_age + male_age))
	new_all_age = []
	for item in all_age:
		 new_all_age.append({"label": item, "value" : all_age[item]}) 


	under_bmi = filter(lambda x: x < 18.5, all_bmi)
	obese_bmi = filter(lambda x: x > 30, all_bmi)
	normal_bmi = filter(lambda x: x >= 18.5 and x < 25, all_bmi)
	over_bmi = filter(lambda x: x >= 25 and x < 30, all_bmi)



	males = {'num': len(all_males), 'bmi' : male_bmi}
	females = {'num' : len(all_females), 'bmi' : female_bmi}
	all_info = {'bmi' : all_bmi, 'over_bmi' : over_bmi, 'normal_bmi' : normal_bmi, 'under_bmi' : under_bmi, 'obese_bmi' : obese_bmi, 'all_age' : new_all_age}

	return render_to_response('demographics.html', {'males' : males, 'females' : females, 'all' : all_info})



def demographics(request):
	all_people = Demographics.objects.all()
	all_males = Demographics.objects.filter(gender='M')
	all_females = Demographics.objects.filter(gender='F')
	key_doctor_arr = Demographics.objects.values('key').distinct()
	key_doctor = []
	for item in key_doctor_arr:
		key_doctor.append(item['key'])


	male_bmi_arr = []
	female_bmi_arr = []
	male_age = []
	female_age = []
	male_bmi = {}
	female_bmi = {}

	for item in all_males:
		male_bmi_arr.append( item.weight / ((item.height / 100.)**2) )
		male_age.append(item.age)

	for item in all_females:
		female_bmi_arr.append( item.weight / ((item.height / 100.)**2) )
		female_age.append(item.age) 

	all_bmi = female_bmi_arr + male_bmi_arr 

	female_age = filter(lambda x : x >= 18 and x < 100, female_age)
	avg_fem_age = sum(female_age) / float(len(female_age))
	male_age = filter(lambda x : x >= 18 and x < 100, male_age)
	avg_male_age = sum(male_age) / float(len(male_age))
	all_age = dict(Counter(female_age + male_age))
	avg_age = sum(all_age) / float(len(all_age))
	new_all_age = []
	for item in all_age:
		 new_all_age.append({"label": item, "value" : all_age[item]}) 

	male_bmi.update({'under': filter(lambda x: x < 18.5, male_bmi_arr)})
	male_bmi.update({'obese': filter(lambda x: x > 30, male_bmi_arr)})
	male_bmi.update({'normal': filter(lambda x: x >= 18.5 and x < 25, male_bmi_arr)})
	male_bmi.update({'over': filter(lambda x: x >= 25 and x <30, male_bmi_arr)})

	female_bmi.update({'under': filter(lambda x: x < 18.5, female_bmi_arr)})
	female_bmi.update({'obese': filter(lambda x: x > 30, female_bmi_arr)})
	female_bmi.update({'normal': filter(lambda x: x >= 18.5 and x < 25, female_bmi_arr)})
	female_bmi.update({'over': filter(lambda x: x >= 25 and x <30, female_bmi_arr)})

	under_bmi = filter(lambda x: x < 18.5, all_bmi)
	obese_bmi = filter(lambda x: x > 30, all_bmi)
	normal_bmi = filter(lambda x: x >= 18.5 and x < 25, all_bmi)
	over_bmi = filter(lambda x: x >= 25 and x < 30, all_bmi)
	all_bmi = filter(lambda x: x < 60 and x > 10, all_bmi)

	avg_bmi = sum(all_bmi) / (len(all_bmi))
	male_bmi_arr = filter(lambda x: x < 60, male_bmi_arr)
	female_bmi_arr = filter(lambda x: x < 60, female_bmi_arr)
	avg_male_bmi = sum(male_bmi_arr) / len(male_bmi_arr)
	avg_female_bmi = sum(female_bmi_arr) / len(female_bmi_arr)

	males = {'num': len(all_males), 'bmi' : male_bmi, 'avg_age' : avg_male_age, 'avg_bmi': avg_male_bmi}
	females = {'num' : len(all_females), 'bmi' : female_bmi, 'avg_age' : avg_fem_age, 'avg_bmi' : avg_female_bmi}
	all_info = {'avg_bmi' : avg_bmi, 'bmi' : all_bmi, 'over_bmi' : over_bmi, 'normal_bmi' : normal_bmi, 'under_bmi' : under_bmi, 'obese_bmi' : obese_bmi, 'all_age' : new_all_age, 'avg_age' : avg_age}

	regiondoctorstm = {}

	for i in key_doctor: 
		regiondoctorstm[i] = [RegionDoctors.objects.get(key=i).tm, RegionDoctors.objects.get(key=i).location]



	return render_to_response('demographics.html', {'regiondoctorstm': regiondoctorstm, 'key_list' : key_doctor, 'males' : males, 'females' : females, 'all' : all_info})








