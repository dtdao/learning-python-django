number_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def print_out_less_than_five(array):

	new_array = []

	for num in array:
		if(num < 5):
			print(num)
			new_array.append(num)

	print("This is a new list: ", new_array)


print_out_less_than_five(number_list)