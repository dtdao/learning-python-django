player_one = input("What is your name player one? >>> ")
player_two = input("What is your name player two? >>> ")

play_game = input("Do you want to play? (yes/no)").lower()

def winner_check(action, action2):
	if(action == 'rock' and action2 == 'scissors' and action2 != 'paper'):
		print(player_one, " is the winner!")
	elif(action == 'scissors' and action2 == 'paper' and action2 != 'rock'):
		print(player_one," is the winner!")
	elif(action == 'paper' and action2 == 'rock' and action2 != 'scissors'):
		print(player_one," is the winner!")
	elif(action == action2):
		print("its a draw")
	else:
		print(player_two, " is the winner")

while play_game != "no" and (play_game in ['yes', 'no']):
	while True:
		try:
			player_one_move = input("What is your move player 1? rock, paper, or scissors? >>> ").lower()
			player_two_move = input("What is your move player 2? rock, paper, or scissors? >>> ").lower() 
			if(player_one_move not in ['rock', 'paper', 'scissors'] or player_two_move not in ['rock', 'paper', 'scissors']):
				raise ValueError("Invalid Choice for Move")
		except ValueError:
			print("Please enter valid choices for rock, paper, or scissors")
			continue
		else:
			break

	winner_check(player_one_move, player_two_move)

	play_game = input("Do you want to player again? (yes/no)").lower()

else: 
	print("GoodBye!!")



