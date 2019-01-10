# Made two prime or not functions
# Both work diferently

# This is using the trial division algorithm 
def prime_or_not(number):
	if number <= 3:
		if number > 1 :
			return "Prime Number"
		else:
			return "Not a Prime Number"
	elif number % 2 == 0 or number % 3 == 0:
		return "Not a Prime Number"
	i = 5
	while i * i <= number:
		if number%i == 0 or number%(i + 2) == 0:
			return "Not a Prime Number"
		i =  i + 6
	return "Prime Number"

# This function is made using the divisor list creater from Exercise 4 modded 
# The number range is limited to 10000
def prime_or_no_prime(number):
	count = 0
	holder = []
	if number <= 3:
		if number > 1 :
			return "Prime Number"
		else: 
			return "Not a Prime Number"

	for num in range(1, 10000):
		count += 1
		if (number % num == 0):
			holder.append(num)
	if len(holder) > 2:
		return "Not a Prime Number"
	return "Prime Number"

while True:
	try: 
		print(prime_or_no_prime(int(input("Please enter a number please >>>>> "))))
		break
	except:
		print("Invalid Value, Try Again!")

