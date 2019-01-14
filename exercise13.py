def fibonacci_number_please(number):
	if number is 0:
		return print([0])
	elif number is 1:
		return print([0,1])
	else:
		holder = [0,1]
		for x in range(1,number):
			holder.append(holder[-1] + holder[-2])

		return print(holder)
while True:
	try:
		fibonacci_number_please(int(input("How many Fibonacci number to generate? >>>> ")))
		break
	except:
		print("Input is not an integer")