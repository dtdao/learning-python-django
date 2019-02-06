# Tic Tac Toe game
# Make for the practicepython.org website Exercise 29


# This function does the checking to see if a List of 3 items in the board is a winner or not
def checking_(array):

	if all(x == "X" for x in array):
		# 1 is player 1 is the winner
		return 1
	elif all(o == "O" for o in array):
		# 2 is player 2 is the winner
		return 2
	else:
		# No winner
		return 0

# This will break and board into various parts for the analyze function to check.
def board_analyze(board_state):
	winner = 0
	# This will send horizontal parts to be check
	for val in range(3):
		winner = checking_(board_state[val])
		if winner == 1 or winner == 2:
			return winner

	# This will send the vertical parts to be check
	for x in range(3):
		vertical_holder = []
		for y in range(3):
			vertical_holder.append(board_state[y][x])
		winner = checking_(vertical_holder)
		if winner == 1 or winner == 2:
			return winner
	
	# This checks the two horizontals
	diagonal1 = checking_([board_state[1][1], board_state[0][0], board_state[2][2]])
	diagonal2 = checking_([board_state[1][1], board_state[0][2], board_state[2][0]])

	if diagonal1 != 0:
		return diagonal1
	elif diagonal2 != 0:
		return diagonal2

	# Ultimate returns the winner 0 if nobody wins
	return winner

# This handles the moves and draw the boards for the player
def do_move(board_state, player_move, move_counter):
	symbol = ("X" if move_counter % 2 == 1 else "O")
	move = player_move.strip().split(",")
	board = board_state
	try: 
		assert(board_state[int(move[0])][int(move[1])] == 0)
		board_state[int(move[0])][int(move[1])] = symbol
	except:
		print("*************INVALID MOVE************")
		return board_state, move_counter
	move_counter += 1
	return board_state, move_counter

# the internal data structureis [[0,0,0],[0,0,0],[0,0,0]]
# Draws the board
def draw_game_box(internal_board_state_array):
	for x in range(3):
		print(" ----- "*3)
		for y in range(3):
			print(f" | {'-' if internal_board_state_array[x][y] == 0 else internal_board_state_array[x][y]} |", end=(" " if y < 2 else "\n"))
		print(" ----- "*3)

# Main game
def tic_tac_toe():
	total_moves = 1
	winner = 0
	# Initial board state
	game_board = [[0,0,0],[0,0,0],[0,0,0]]

	print("Welcome to the Tic-Tac-Toe Game!")
	player1_name = input("What is the first player name? >>>> ").strip()
	player2_name = input("What is the second player name? >>>> ").strip()

	print(f"\n******* {player1_name} VS {player2_name} ******* ")


	draw_game_box(game_board)
	# Runs infinitely until all valid moves are done.
	while total_moves <= 9:
		# Moves must be inputed as >>>> 1,2 [row,col]
		move = input("Where would you like to move? Please input the coordinates as >>>> row, col ")
		game_board, total_moves = do_move(game_board, move, total_moves)
		draw_game_box(game_board)
		winner = board_analyze(game_board)
		if winner == 1:
			print(f"***************Congratulations {player1_name} you won!!!********************")
			break
		if winner == 2:
			print(f"***************Congratulations {player2_name} you won!!!********************")
			break

	if winner == 0:
		print("Nobody won!")
		exit()

if __name__ == '__main__':
	tic_tac_toe()