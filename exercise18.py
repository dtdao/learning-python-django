import random

def checking_the_game(the_number, guess=input(">>> ")):
	print(the_number == guess)
	return False


def cows_and_bulls_game():
	game = True
	the_number = random.sample([0,1,2,3,4,5,6,7,8,9], 4)
	print("""Lets play the cow and bull game!
			Please enter your 4 digit number please.
			(They all must be unique""")

	while game:
		game = checking_the_game(the_number)



# if __name__ == "__main__":
# 	cows_and_bulls_game()


cows_and_bulls_game()