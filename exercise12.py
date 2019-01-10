a = [1,2,3,4,5,6]
def first_and_last_of_list(list):
	if len(list) < 1:
		print(list)
		return
	print([list[0], list.pop()])
	return

first_and_last_of_list(a)