import random

# Draw the hang man
def draw_the_hangman(remaining_life):
	print(f"""
________
|    |
|    {'@' if remaining_life <= 5 else ''}
|  {'__' if remaining_life <= 4 else ''}{'|__/' if remaining_life <= 3 else ''} 
| {'/  ' if remaining_life <= 4 else ''}{'|' if remaining_life <= 2 else ''}
|   {'_' if remaining_life <= 1 else ''}{'|' if remaining_life <= 1 else ''}{'_' if remaining_life < 1 else ''}
|  {'|' if remaining_life <= 1 else ''}   {'|' if remaining_life < 1 else ''}
| {'_|' if remaining_life <= 1 else ''}   {'|_' if remaining_life < 1 else ''}	
|  
|_____________
		""")
	print(f"You have {remaining_life} left.")

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
		return False

# Main game
def guess_the_word():
	remaining_guess = 6
	word_to_guess = list(generate_word())
	# use list comprehension to fill my guess.
	my_guess = ["_" for val in word_to_guess]
	# Holder to hold your already guess words
	already_guess_letters = []

	print("*********** Welcome to HangMan ****************\n")
	# Current word to be guess
	while remaining_guess != 0:
		print_out(my_guess)
		while True:
			player_letter = input("Please input a letter to guess >>> ").upper()
			try:
				assert(already_guess_letters.count(player_letter) == 0)
				already_guess_letters.append(player_letter)
				break
			except:
				print("\nYou alaready guess that letter! \nTry again!\n")

		# This actually return my_guess without assigning it to my_guess
		if check_and_compare_word(word_to_guess, my_guess, player_letter) == False:
			remaining_guess -= 1
		draw_the_hangman(remaining_guess)


	if my_guess != word_to_guess: 
		print("***********SORRY YOU LOST!***************")
	else:
		completed_word = "".join(my_guess)
		print(f"Congratuations!! You solved the puzzle! \nThe word is {completed_word}")

	if input("Would you like to play again? (Y/N)? >>>>>> ").lower() == 'y':
		guess_the_word()
	else:
		return print("Thank you for playing! Good Bye")

if __name__ == '__main__':
	# print_out(check_and_compare_word(test, test_guess, test_leter))
	guess_the_word()