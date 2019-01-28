import urllib.request

# Given two .txt files that have lists of numbers in them,
# find the numbers that are overlapping.

# IS it betrer to use a function to convert a list to an array of number
def file_reader(file_to_read):
	with urllib.request.urlopen(file_to_read) as file:
		line = file.readline()
		file_to_read_holder = []
		while line:
			file_to_read_holder.append(line.strip().decode("utf-8"))
			line = file.readline()

	return file_to_read_holder
	
# Using list comprehension
def check_for_overlapping(list1, list2):
	return print([val for val in list1 if val in list2])


if __name__ == '__main__':
	url1 = "http://www.practicepython.org/assets/primenumbers.txt"
	url2 = "http://www.practicepython.org/assets/happynumbers.txt"
	check_for_overlapping(file_reader(url1), file_reader(url2))
