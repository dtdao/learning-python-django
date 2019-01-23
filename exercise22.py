import urllib.request
import re


def file_reader(url_to_read):
	holder = {}
	with urllib.request.urlopen(url_to_read) as txt:
		line = txt.readline()

		while line:
			line = str(line).strip()[5:-28]
			if line in holder:
				holder[line] += 1
			else:
				holder[line] = 1

			line = txt.readline()

	for item in holder:
		print(item)


if __name__ == '__main__':
	url1 = "http://www.practicepython.org/assets/nameslist.txt"
	url2 = "http://www.practicepython.org/assets/Training_01.txt"
	file_reader(url2)