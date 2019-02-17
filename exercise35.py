import json
import collections
import calendar
import pprint

# This does not the collection.Counter() 
def month_counter():

	months = {}
	with open("birthday.json", "r") as f:
		info = json.load(f)

	month_of_birthday = [int(person["birthday"].split("-")[1]) for person in info["people"]]

	for month in month_of_birthday:
		if calendar.month_name[(month)] in months:
			months[calendar.month_name[(month)]] = months[calendar.month_name[(month)]] + 1
		else:
			months[calendar.month_name[(month)]] = 1

	pprint.pprint(months)
	return False

# This uses the collections.Counter() 
def month_counter_two():

	with open("birthday.json", "r") as f:
		info = json.load(f)

	month_of_birthday = [calendar.month_name[int(person["birthday"].split("-")[1])] for person in info["people"]]

	return print(collections.Counter(month_of_birthday))

if __name__ == '__main__':
	# month_counter()
	month_counter_two()