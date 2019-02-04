def checking_(array):
	if all(x == "X" for x in array):
		return 1
	elif all(o == "O" for o in array):
		return 2

def board_analyze(board_state):
	winner = 0
	for val in range(3):
		winner = checking_(board_state[val])
		if winner == 1 or winner == 2:
			print("Vertical check")
			return winner

	for x in range(3):
		vertical_holder = []
		for y in range(3):
			vertical_holder.append(board_state[y][x])
		winner = checking_(vertical_holder)
		if winner == 1 or winner == 2:
			print("horizontal check")
			return winner

	diagonal1 = checking_([board_state[1][1], board_state[0][0], board_state[2][2]])
	diagonal2 = checking_([board_state[1][1], board_state[0][2], board_state[2][0]])
	if diagonal1 != 0:
		return diagonal1
	elif diagonal2 != 0:
		return diagonal2
	# if (board_state[1][1] == (board_state[0][0] and board_state[2][2])) or (board_state[1][1] == (board_state[0][2] and board_state[2][0])):
	# 	return (1 if board_state[1][1] == "X" else 2)

	return winner

def do_move(board_state, player_move, move_counter):
	symbol = ("X" if move_counter % 2 == 1 else "O")
	move = player_move.strip().split(",")
	board = board_state
	try: 
		assert(board_state[int(move[0])][int(move[1])] == 0)
		board_state[int(move[0])][int(move[1])] = symbol
		print(board_state)
	except:
		print("*************INVALID MOVE************")
		return board_state, move_counter
	move_counter += 1
	return board_state, move_counter

# the internal data structureis [[0,0,0],[0,0,0],[0,0,0]]
def draw_game_box(internal_board_state_array):
	for x in range(3):
		print(" ----- "*3)
		for y in range(3):
			print(f" | {internal_board_state_array[x][y]} |", end=(" " if y < 2 else "\n"))
		print(" ----- "*3)

def tic_tac_toe():
	total_moves = 1
	winner = 0
	game_board = [[0,0,0],[0,0,0],[0,0,0]]
	print("Welcome to the Tic-Tac-Toe Game!")
	player1_name = input("What is the first player name? >>>> ").strip()
	player2_name = input("What is the second player name? >>>> ").strip()

	print(f"\n******* {player1_name} VS {player2_name} ******* ")

	draw_game_box(game_board)
	while total_moves <= 9:
		move = input("Where would you like to move? Please input the coordinates as >>>> row, col ")
		game_board, total_moves = do_move(game_board, move, total_moves)
		draw_game_box(game_board)
		winner = board_analyze(game_board)
		print(winner)
		if winner == 1:
			print(f"***************Congratulations {player1_name} your won!!!********************")
			break
		if winner == 2:
			print(f"***************Congratulations {player2_name} your won!!!********************")
			break

	if winner == 0:
		print("No body won!")
		exit()


if __name__ == '__main__':
	tester_array = [[0,'X',0],[0,'y',0],[0,'z',0]]
	# draw_game_box(tester_array)
	tic_tac_toe()