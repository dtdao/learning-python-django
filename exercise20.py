

def number_is_hear_boolean(list_to_search, number_to_search_for):
	sorted_list = list_to_search.sort()
	first_element = 0
	last_element = len(list_to_search) - 1
	element_found = False
	# this is looping to find the number
	for num in list_to_search:
		if number_to_search_for == num:
			element_found = True

	return element_found
	# This is binary search
	# print((first_element + last_element)//2)

	# Not working binary

	# while first_element <= last_element :
	# 	mid = (first_element + last_element)//2


	# 	if list_to_search[mid] == number_to_search_for:
	# 		element_found = True
	# 		break
	# 	else:
	# 		if number_to_search_for < list_to_search[mid]:
	# 			last_element = mid 
	# 		else:
	# 			first_element = mid 

	# return element_found



if __name__  == "__main__":
	testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
	print(number_is_hear_boolean(testlist, 54))
