import random

def generate_word():
	with open('sowpods.txt') as file:
		wordlist = file.readlines()

	return random.choice(wordlist).rstrip()

def guess_the_word():
	word_to_guess = list(generate_word())
	# use list comprehension to fill my guess.
	my_guess = ["_" for val in word_to_guess]

	print("*********** Welcome to HangMan ****************\n")

	for x in range(len(word_to_guess)):
		print("_", end=(" " if x < len(word_to_guess)-1 else "\n"))


if __name__ == '__main__':
	guess_the_word()