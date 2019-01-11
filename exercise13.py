

how_many_times = int(input("How many Fibonacci number to generate? >>>> "))
count = 0
holder = [1,2,3,4,5,6]

new_number = holder[len(holder) - 2]
last_number = holder.pop()

new = last_number + new_number
print(last_number)
print(new_number)

print(new)



print(holder)


# def fibonacci_number_please(holder):
# 	if len(holder) == 1:
# 		return [1, 1]
# 	if len(holer) >= 1:
# 		print(holder)
# 		fibonacci_number_please(holder.append(holder.pop() + holder[len(holder) - 2]))
# 	else:
# 		return holder
#
# while True:
# 	if count <= how_many_times:
# 		count += 1
# 		print(fibonacci_number_please(holder));
# 	else:
# 		print("finished")
# 		break
