import random 

def list_overlap(list1, list2):
	holder = []
	for val in list1:
		if val in list2 and (val not in holder):
			holder.append(val)

	print(f""" 
	List1: {list1} 
	List2: {list2}
		""")
	print(holder)

a = []
b = []

def random_number_list():
	for x in range(20):
		a.append(random.randint(1, 51))
		b.append(random.randint(1, 51))

random_number_list()
list_overlap(a, b)