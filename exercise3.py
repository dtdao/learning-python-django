number_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]



def print_out_less_than_five(array):

	while True:
		try: 
			number = int(input("Please give me a number >>>>> "))
			assert(number > 0)
			break
		except: 
			print("You provided a string and non zero number, try again.")

	new_array = []

	for num in array:
		if(num < number):
			print(num)
			new_array.append(num)

	print("This is a new list: ", new_array)


print_out_less_than_five(number_list)