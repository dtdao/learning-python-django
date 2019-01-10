

how_many_times = int(input("How many Fibonacci number to generate? >>>> "))
count = 0
holder = [1]

def fibonacci_number_please(holder):
	if len(holder) == 1:
		return [1, 1]
	return holder.append(holder.pop() + holder[len(holder) - 2])

while True:
	if count <= how_many_times:
		count += 1
		print(fibonacci_number_please(holder));
	else:
		break
		print("finished")




