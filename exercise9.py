import random

<<<<<<< HEAD
totalGuess = 0
game_on = ""

def guess(answer):
	global game_on, totalGuess
	while True:
		try:
			my_guess = int(input(">>>>> "))
			totalGuess += 1
		except:
			totalGuess += 1
			print("You entered a invalid value")
			break

		if int(my_guess) < answer :
			print(answer)
			print("**** Your guess is too low ****")
			continue
		elif int(my_guess) > answer :
			print(answer)
			print("**** Your guess is too high ****")
			continue
		else:
			print("**** Your guess is correct! *****")
			break
	game_on = str(input("Do you want to exit? >>>> "))	

while game_on != "exit":
	random_number = random.randint(1, 9)
	print("Please guess a number between 1 and 9")
	guess(random_number)
else:
	print(f"You guessed a total of {totalGuess} times")
	print("Game over")


=======
print("Let's play a guessing game!!")

def guess():
    randomGenerate()

def randomGenerate():
    return random.randint(1,9)


if not isinstance(x, int)
>>>>>>> 4fb26198de918fcee0e9a987e79c834974f70d8d
