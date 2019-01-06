
# Will only test numbers from 1 to 100000
number_range = range(1, 100001)
holder = []

while True: 
	try:
		test_number = int(input("Please put in a positive number please. >>>> "))
		assert(test_number > 0)
		break
	except:
		print("That is a String") 

def divisor(number): 
	for num in number_range:
		if (number % num == 0):
			holder.append(num)
	print(holder)

divisor(test_number)