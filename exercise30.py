
import random

def random_word_picker():
	file_length = len(list(open("sowpods.txt")))
	with open('sowpods.txt', 'r+', encoding="utf-8", newline=None) as f:
		wordlist = f.readlines()

	return print(random.choice(wordlist).rstrip())

if __name__ == '__main__':
	random_word_picker()