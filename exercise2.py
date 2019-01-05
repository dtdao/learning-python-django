def odd_or_even(num):
	odd_or_even = int(num % 2)

	if (odd_or_even == 0) and (num%4 == 0) :
		print("Your first number  is even and a multiple of 4!")
	elif odd_or_even == 0:
		print("Your number is an Even number!")
	else: 
		print("Your number is an odd number!")

def two_numbers(num1, num2):
	evenly_divide = (num1%num2)

	if(evenly_divide == 0):
		print(f"{num2} divides evenly into {num1}")
	else:
		print(f"{num2} does not divide evenly into {num1}")



while True:
	try:
		number1 = int(input("Pleae give us a number >>>> "))
		assert(number1 > 0)
		odd_or_even(number1)

		number2 = int(input("Please give us a second number >>>> "))
		assert(number2 > 0)
		two_numbers(number1, number2)
		break
	except:
		print("You entered a string, please only enter positive integers")
