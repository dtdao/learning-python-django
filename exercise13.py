

how_many_times = int(input("How many Fibonacci number to generate? >>>> "))
count = 0
holder = [1]

# def fibonacci_number_please(num):
# 	if num == 1:
# 		print("thi")
# 		return [1, 1]
# 	return holder.append(holder[len(holder)] + holder[len(holder) - 1])

# while True:
# 	if count <= how_many_times:
# 		count += 1
# 		print(fibonacci_number_please(int(how_many_times)));
# 	else:
# 		break
# 		print("finished")

def do_fibonacci():
	print(holder[len(holder)])
	print(holder[len(holder) - 2])
	return holder.append(holder[len(holder) -1] + holder[len(holder) - 2])

def fibonacci(times):
	for num in range(1, int(times)):
		print(do_fibonacci())
		

fibonacci(how_many_times)