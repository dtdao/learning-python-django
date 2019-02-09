import random
# This function will generate a random word for you to solve
def generate_word():
	with open('sowpods.txt') as file:
		wordlist = file.readlines()

	return random.choice(wordlist).rstrip()

# Print out the word for you
def print_out(word):
	for x in range(len(word)):
		print(word[x], end=" " if x < len(word)-1 else "\n")

# This checks and compare the word
# returns your guess with changes if you made the correct selection or not
def check_and_compare_word(answer, guess, guess_letter):
	print(f"You guess the letter: {guess_letter}")
	if answer.count(guess_letter) > 0:
		print("\nYour guess is correct!!\n")
		index_list = [index for index in range(len(answer)) if answer[index] == guess_letter]
		if len(index_list):
			for index in index_list:
				guess[index] = guess_letter
			return guess
	else:
		print("\nYour guess is incorrect!! \n\nTry again. \n")
		return guess

# Main game
def guess_the_word():
	word_to_guess = list(generate_word())
	# use list comprehension to fill my guess.
	my_guess = ["_" for val in word_to_guess]
	# Holder to hold your already guess words
	already_guess_letters = []

	print("*********** Welcome to HangMan ****************\n")
	# Current word to be guess
	while word_to_guess != my_guess:
		print_out(my_guess)
		while True:
			player_letter = input("Please input a letter to guess >>> ").upper()
			try:
				assert(already_guess_letters.count(player_letter) == 0)
				already_guess_letters.append(player_letter)
				break
			except:
				print("\nYou alaready guess that letter! \nTry again!\n")

		my_guess = check_and_compare_word(word_to_guess, my_guess, player_letter)

	completed_word = "".join(my_guess)
	print(f"Congratuations!! You solved the puzzle! \nThe word is {completed_word}")

if __name__ == '__main__':
	# print_out(check_and_compare_word(test, test_guess, test_leter))
	guess_the_word()