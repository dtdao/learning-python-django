import random

def check_bull_and_cow(the_number, input_guess):
	guess = [int(i) for i in input_guess]
	cows = [i for i in the_number if i in guess and the_number.index(i) == guess.index(i)]
	bulls = [i for i in the_number if i in guess and the_number.index(i) != guess.index(i)]
	# This gives me the cows
	# print(f"Cows: {len(cows)}")
	# # This gives me the bulls
	# print(f"Bulls: {len(bulls)}")
	return {"Cows": len(cows), "Bulls": len(bulls)}

def cows_and_bulls_game():
	game = 1
	count = 0
	the_number = random.sample([0,1,2,3,4,5,6,7,8,9], 4)

	# def check_bull_and_cow(the_number, guess):

	print("""

		   Lets play the cow and bull game!
		Please enter your 4 digit number please.
		    (They all must be unique)

		You exit anytime just press type "exit"
			""")
	while game == 1:
		while True:
			try:
				user_guess = input(">>> ")
				if(user_guess.lower() == "exit"):
					break
				else:
					user_guess = [int(i) for i in user_guess]
					assert(len(user_guess) == 4)
					break
			except:
				print("invalid input")
		if user_guess == "exit":
			print("Thank you for playing")
			break
		else:		
			result = check_bull_and_cow(the_number, user_guess)
			count +=1
			for x,y in result.items():
				print(x, y)
			if result["Cows"] == 4:
				print("Congratulations you won!")
				print(f"You guessed a total of: {count} times")
				break
			else:
				print(f"Current total guess: {count}")
			

		
if __name__ == "__main__":
	cows_and_bulls_game()

