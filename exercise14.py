a = [1,2,3,4,5,6,1,2,3,4,5,6,1,2,3,4,5,6]

def remove_using_loops(list):
	count = 0
	holder = []
	for item in list:
		if item not in holder:
			holder.append(item)
	return print(holder)

def remove_using_sets(list):
	return print(set(list))


remove_using_loops(a)
remove_using_sets(a)