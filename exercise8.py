player_one = input("What is your name player one? >>> ")
player_two = input("What is your name player two? >>> ")

play_game = input("Do you want to play? (yes/no)").lower()

while play_game != "no":
	def winner_check(action, action2):
		if(action == 'rock' and action2 == 'scissors' and action2 != 'paper'):
			print(player_one, " is the winner!")
		elif(action == 'scissors' and action2 == 'paper' and action2 != 'rock'):
			print(player_one," is the winner!")
		elif(action == 'paper' and action2 == 'rock' and action2 != 'scissors'):
			print(player_one," is the winer!")
		elif(action == action2):
			print("its a draw")
		else:
			print(player_two, " is the winer")
	player_one_move = input("What is your move player 1? rock, paper, or scissors?")
	player_two_move = input("What is your move player 2? rock, paper, or scissors?")

	winner_check(player_one_move, player_two_move);

	play_game = input("Do you want to player again? (yes/no)").lower()



